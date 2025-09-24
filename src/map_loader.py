def load_map(filename):
    """Load grid map from a text file into a 2D list."""
    grid = []
    start, goal = None, None
    with open(filename, "r") as f:
        for r, line in enumerate(f.readlines()):
            row = line.strip().split()
            for c, val in enumerate(row):
                if val == "S":
                    start = (r, c)
                    row[c] = "0"
                elif val == "G":
                    goal = (r, c)
                    row[c] = "0"
            grid.append(row)
    return grid, start, goal


def print_grid(grid, path=None):
    """Print grid with optional path overlay."""
    display = [row[:] for row in grid]  # deep copy
    if path:
        for r, c in path:
            if display[r][c] == "0":
                display[r][c] = "."
    for row in display:
        print(" ".join(row))
