import heapq, time

def ucs(grid, start, goal):
    start_time = time.time()
    rows, cols = len(grid), len(grid[0])
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    pq = [(0, start, [start])]
    visited = {}
    nodes_expanded = 0

    while pq:
        cost, (r, c), path = heapq.heappop(pq)
        nodes_expanded += 1
        if (r, c) == goal:
            runtime = time.time() - start_time
            return path, cost, nodes_expanded, runtime
        if (r, c) in visited and visited[(r,c)] <= cost:
            continue
        visited[(r,c)] = cost
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
                # treat "0" as cost 1 (and digits >0 as their numeric cost)
                if grid[nr][nc].isdigit() and int(grid[nr][nc]) > 0:
                    move_cost = int(grid[nr][nc])
                else:
                    move_cost = 1
                heapq.heappush(pq, (cost + move_cost, (nr, nc), path + [(nr, nc)]))
    runtime = time.time() - start_time
    return None, float("inf"), nodes_expanded, runtime
