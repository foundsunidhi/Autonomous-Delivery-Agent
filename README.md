# Autonomous Delivery Agent — Project 1

**Course:** CSA2001 — Fundamentals of AI and ML,
**Project Type:** Project-Based Learning

---

## Project Overview

This project is my implementation of an **autonomous delivery agent** that can navigate a 2D grid city to deliver packages efficiently. The goal was to design an intelligent agent that adapts to different environments, handles obstacles, and optimizes its delivery route using classical and AI-based search algorithms.

The agent is capable of:

* Modeling the environment with **static obstacles, terrain movement costs, and dynamic moving obstacles**.
* Making rational decisions that balance delivery efficiency with constraints such as time and fuel.
* Using multiple planning approaches:

  * **Uninformed search:** Breadth-First Search (BFS) and Uniform-Cost Search (UCS).
  * **Informed search:** A* search with admissible heuristics.
  * **Local search replanning:** Hill-Climbing with random restarts / Simulated Annealing to react to changing environments.

---

## Features

* **Multiple planners** for different scenarios and efficiency trade-offs.
* **Dynamic replanning** when new obstacles appear during execution.
* **Experimental comparisons** of algorithms across several map instances.
* **Well-documented code** with clear instructions to reproduce results.

---

## Project Structure

```
Autonomous-Delivery-Agent/
├─ maps/                # Test maps (small, medium, large, dynamic)
├─ planners/            # Implementations of BFS, UCS, A*, and local search
├─ sim/                 # Simulator for dynamic environments
├─ tests/               # Scripts to run experiments and collect results
├─ logs/                # Output logs for runs and replanning
├─ results/             # CSV files and plots of experiment data
├─ README.md            # Project documentation
└─ final_report_aiml.pdf # Detailed project report
```

---

## Map Format

Maps are text-based grids. Example:

```
S . . 2 #
. 3 . . .
. . # . G
. . . 1 .
# . . . .
```

Legend:

* `S` : Start position
* `G` : Goal position
* `.` : Free cell (cost 1)
* Integer `n` : Terrain with movement cost `n`
* `#` : Static obstacle

Dynamic maps include an additional schedule file defining obstacle movement.

---

## How to Run

### 1. Setup Environment

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### 2. Run a Planner

```bash
# Example: BFS
python planners/bfs.py --map maps/map_small.grid --start 0,0 --goal 4,2 --log logs/bfs_small.log

# Example: A* with Manhattan heuristic
python planners/astar.py --map maps/map_large.grid --start 0,0 --goal 14,14 --heuristic manhattan --log logs/astar_large.log
```

### 3. Dynamic Replanning Example

```bash
python sim/simulator.py --map maps/map_dynamic.grid --planner astar --inject-obstacle 5,10,3 --log logs/dynamic_demo.log
```

The log file will show when an obstacle appears and how the agent replans.

### 4. Run Experiments

```bash
python tests/run_experiments.py --out results/experiment_results.csv
```

---

## Results

* **A*** outperformed UCS in terms of speed while maintaining optimality.
* **UCS** expanded more nodes but always returned the optimal path.
* **BFS** worked well only in uniform-cost maps.
* **Local search** allowed fast reactive replanning in dynamic scenarios but produced slightly higher path costs.

---

## Deliverables

* **Source code:** Python implementations of planners and simulator.
* **Maps:** 4 test maps (small, medium, large, dynamic).
* **Report:** `final_report_aiml.pdf` (contains detailed methodology, results, and analysis).
* **Demo:** Logs and screenshots for replanning demonstration.

---

## Conclusion

Through this project, I explored multiple search strategies and evaluated their strengths and weaknesses in dynamic delivery scenarios. The combination of A* and local search provided a good balance between **optimal planning** and **reactive adaptability**. This work demonstrates how classical AI techniques can be effectively applied to real-world inspired delivery problems.
