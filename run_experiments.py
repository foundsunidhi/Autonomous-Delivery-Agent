"""
Run all planners on provided maps and save results.csv
"""
import argparse, csv, os
from src.map_loader import load_map
from src.planners.bfs import bfs as bfs_pl
from src.planners.ucs import ucs as ucs_pl
from src.planners.astar import astar as astar_pl
from src.planners.hill_climbing import hill_climb as hill_pl


ALGO_MAP = {"bfs": bfs_pl, "ucs": ucs_pl, "astar": astar_pl, "hill": hill_pl}

def run_experiments(maps, algos, out_csv="results.csv"):
    os.makedirs("results", exist_ok=True)
    rows = []
    for m in maps:
        grid, start, goal = load_map(m)
        for a in algos:
            planner = ALGO_MAP[a]
            path, cost, nodes, runtime = planner(grid, start, goal)
            path_len = len(path) if path else None
            rows.append({"map": os.path.basename(m), "algo": a, "path_len": path_len, "cost": cost, "nodes": nodes, "time": runtime})
            print(f"Ran {a} on {m}: path_len={path_len}, cost={cost}, nodes={nodes}, time={runtime:.4f}s")
    # write CSV
    out_path = os.path.join("results", out_csv)
    with open(out_path, "w", newline='') as cf:
        writer = csv.DictWriter(cf, fieldnames=["map","algo","path_len","cost","nodes","time"])
        writer.writeheader()
        for r in rows:
            writer.writerow(r)
    print("Results saved to", out_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--maps", nargs="+", required=True)
    parser.add_argument("--algos", nargs="+", required=True)
    parser.add_argument("--out", default="results.csv")
    args = parser.parse_args()
    run_experiments(args.maps, args.algos, args.out)
