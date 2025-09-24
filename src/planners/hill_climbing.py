import random, time

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def hill_climb(grid, start, goal, max_restarts=5, max_steps=100):
    start_time = time.time()
    rows, cols = len(grid), len(grid[0])
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    nodes_expanded = 0

    for restart in range(max_restarts):
        current = start
        path = [current]
        for step in range(max_steps):
            nodes_expanded += 1
            if current == goal:
                runtime = time.time() - start_time
                cost = sum(int(grid[x][y]) if grid[x][y].isdigit() and int(grid[x][y])>0 else 1 for x,y in path[1:])
                return path, cost, nodes_expanded, runtime
            neighbors = []
            for dr, dc in directions:
                nr, nc = current[0] + dr, current[1] + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
                    neighbors.append((nr, nc))
            if not neighbors:
                break
            best = min(neighbors, key=lambda n: heuristic(n, goal))
            if heuristic(best, goal) >= heuristic(current, goal):
                break  # stuck
            current = best
            path.append(current)
        # restart if stuck
    runtime = time.time() - start_time
    return None, float("inf"), nodes_expanded, runtime
