"""
Simulate agent moving along a planned path while a moving obstacle appears according to schedule.
When the agent's next step is blocked, replans using the selected algorithm and logs events.
"""
import argparse, copy, time, os
from map_loader import load_map
from planners.bfs import bfs
from planners.ucs import ucs
from planners.astar import astar
from planners.hill_climbing import hill_climb
from utils.visualize import visualize_path

ALGO_MAP = {"bfs": bfs, "ucs": ucs, "astar": astar, "hill": hill_climb}

def simulate(mapfile, algo, obstacle_schedule=None, out_log="logs/dynamic_replan.log"):
    os.makedirs("logs", exist_ok=True)
    grid, start, goal = load_map(mapfile)
    planner = ALGO_MAP[algo]

    # initial plan
    path, cost, nodes, runtime = planner(grid, start, goal)
    current = start
    step_idx = 0
    log_lines = []
    log_lines.append(f"[{time.strftime('%H:%M:%S')}] Initial plan: length={len(path) if path else None}, cost={cost}")

    # obstacle_schedule: list of tuples (step_number, (r,c))
    if obstacle_schedule is None:
        obstacle_schedule = [(3, path[4] if path and len(path)>4 else None)]

    schedule = {s[0]: s[1] for s in obstacle_schedule if s[1] is not None}

    full_path = path[:] if path else []
    # step through path
    while True:
        if current == goal:
            log_lines.append(f"[{time.strftime('%H:%M:%S')}] Reached goal.")
            break
        if step_idx+1 >= len(full_path):
            log_lines.append(f"[{time.strftime('%H:%M:%S')}] No further steps; stopping.")
            break
        next_cell = full_path[step_idx+1]
        # apply scheduled obstacle
        if step_idx in schedule:
            orow, ocol = schedule[step_idx]
            if 0 <= orow < len(grid) and 0 <= ocol < len(grid[0]):
                grid[orow][ocol] = "#"
                log_lines.append(f"[{time.strftime('%H:%M:%S')}] Obstacle appeared at {(orow,ocol)}")
        # if next cell blocked, replan from current
        if grid[next_cell[0]][next_cell[1]] == "#":
            log_lines.append(f"[{time.strftime('%H:%M:%S')}] Next cell {next_cell} blocked, replanning...")
            new_plan, new_cost, new_nodes, new_time = planner(grid, current, goal)
            if new_plan:
                full_path = [current] + new_plan[1:]
                step_idx = 0
                log_lines.append(f"[{time.strftime('%H:%M:%S')}] Replan success: length={len(new_plan)}, cost={new_cost}")
                continue
            else:
                log_lines.append(f"[{time.strftime('%H:%M:%S')}] Replan failed. No path to goal.")
                break
        # move to next cell
        current = next_cell
        step_idx += 1
        # save snapshot file every move
        snapshot = f"logs/snapshot_step_{step_idx}.txt"
        with open(snapshot, "w") as sf:
            for r,row in enumerate(grid):
                rowcopy = row[:]
                for (i,j) in full_path:
                    if r==i:
                        if rowcopy[j] == "0":
                            rowcopy[j] = "."
                sf.write(" ".join(rowcopy) + "\n")
    # write log
    with open(out_log, "w") as lf:
        lf.write("\n".join(log_lines))
    print("Simulation complete. Log saved to", out_log)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--map", required=True)
    parser.add_argument("--algo", required=True, choices=["bfs","ucs","astar","hill"])
    args = parser.parse_args()
    simulate(args.map, args.algo)
