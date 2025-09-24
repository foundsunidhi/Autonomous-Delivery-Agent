import argparse
from map_loader import load_map
from planners.bfs import bfs
from planners.ucs import ucs
from planners.astar import astar
from planners.hill_climbing import hill_climb
from utils.visualize import visualize_path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--map", required=True, help="Path to map file")
    parser.add_argument("--algo", required=True, choices=["bfs","ucs","astar","hill"])
    args = parser.parse_args()

    grid, start, goal = load_map(args.map)

    if args.algo == "bfs":
        path, cost, nodes, runtime = bfs(grid, start, goal)
    elif args.algo == "ucs":
        path, cost, nodes, runtime = ucs(grid, start, goal)
    elif args.algo == "astar":
        path, cost, nodes, runtime = astar(grid, start, goal)
    elif args.algo == "hill":
        path, cost, nodes, runtime = hill_climb(grid, start, goal)

    if path:
        print(f"Algorithm: {args.algo}")
        print(f"Path length: {len(path)} | Cost: {cost}")
        print(f"Nodes expanded: {nodes} | Time: {runtime:.4f} s")
        visualize_path(grid, path)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
