
from collections import deque
import time

def bfs(grid, start, goal):
    start_time = time.time()
    rows, cols = len(grid), len(grid[0])
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    queue = deque([(start, [start])])
    visited = set([start])
    nodes_expanded = 0

    while queue:
        (r, c), path = queue.popleft()
        nodes_expanded += 1
        if (r, c) == goal:
            runtime = time.time() - start_time
            cost = sum(int(grid[x][y]) if grid[x][y].isdigit() and int(grid[x][y])>0 else 1 for x,y in path[1:])
            return path, cost, nodes_expanded, runtime
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if grid[nr][nc] != "#":
                    queue.append(((nr, nc), path + [(nr, nc)]))
                    visited.add((nr, nc))
    runtime = time.time() - start_time
    return None, float("inf"), nodes_expanded, runtime
