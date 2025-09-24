def visualize_path(grid, path):
    """Print grid with path overlay."""
    grid_copy = [row[:] for row in grid]
    for r, c in path:
        if grid_copy[r][c] == "0":
            grid_copy[r][c] = "."
    for row in grid_copy:
        print(" ".join(row))
