import heapq, time

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])  # Manhattan distance

def astar(grid, start, goal):
    start_time = time.time()
    rows, cols = len(grid), len(grid[0])
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    open_set = [(heuristic(start, goal), 0, start, [start])]
    visited = {}
    nodes_expanded = 0

    while open_set:
        f, g, (r, c), path = heapq.heappop(open_set)
        nodes_expanded += 1
        if (r, c) == goal:
            runtime = time.time() - start_time
            return path, g, nodes_expanded, runtime
        if (r, c) in visited and visited[(r,c)] <= g:
            continue
        visited[(r,c)] = g
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
                if grid[nr][nc].isdigit() and int(grid[nr][nc]) > 0:
                    move_cost = int(grid[nr][nc])
                else:
                    move_cost = 1
                new_g = g + move_cost
                heapq.heappush(open_set, (new_g + heuristic((nr, nc), goal), new_g, (nr, nc), path + [(nr, nc)]))
    runtime = time.time() - start_time
    return None, float("inf"), nodes_expanded, runtime
