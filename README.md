# Pathfinding Algorithms in Python

This project implements classic search algorithms for AI pathfinding, as per university assignment.

## Features
- *BFS (Breadth First Search)* – uninformed, works best on uniform-cost maps
- *UCS (Uniform Cost Search)* – optimal on weighted maps
- *A\** – informed search with Manhattan heuristic
- *Hill Climbing* – local search, not guaranteed to find optimal path
- *Map Loader* – reads text maps with Start (S), Goal (G), obstacles (#), and costs (0,1,2…)
- *Visualizer* – shows solution path over the map in console
- *CLI Tool* – run any algorithm on any map

## Installation
No external libraries required. Just Python 3.x.

```bash
git clone <your_repo>
cd <repo_folder>