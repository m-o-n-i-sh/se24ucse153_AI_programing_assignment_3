# UGV Path Planning using A* Algorithm
##  Problem Statement
An Unmanned Ground Vehicle (UGV) is a robot that finds the optimal path from a given user-specified start node to a user-specified Goal node on a map of a small area in a battlefield (Eg 70x70 Kms). There are obstacles known a priority. The density of the obstacles can be generated randomly with three different levels of density. Design an algorithm that makes the UGV to navigate through this grid space avoiding all the known obstacles to reach the goal by the shortest distance. Trace this path along with the Measures of Effectiveness.
---
##  Objective
- Represent battlefield as a **grid (70×70)**
- Generate obstacles based on **density levels**
- Use **A\* Search Algorithm** for optimal pathfinding
- Visualize the path using a **graph**
- Compute performance metrics
---
## Algorithm Used
###  A* Search Algorithm
A* is an informed search algorithm that finds the shortest path using:
\[
f(n) = g(n) + h(n)
\]
Where:
- \( g(n) \): Cost from start to current node  
- \( h(n) \): Heuristic (Manhattan distance)
---
##  Features
- User input for:
  - Obstacle density (low / medium / high)
  - Start coordinates
  - Goal coordinates
- Random obstacle generation
- Shortest path computation
- Graphical visualization using matplotlib
- Performance metrics display
---
##  Project Structure
```
Q2_UGV_Pathfinder
├── UGV_Static.py
├── requirements.txt
└── README.md
```
---
## Installation
### 1. Clone the repository
```bash
git clone https://github.com/m-o-n-i-sh/se24ucse153_AI_programing_assignment_3.git
cd se24ucse153_AI_programing_assignment_3/Q2_UGV_Pathfinder
```
### 2. Install dependencies
```
pip install -r requirements.txt
```
## How to Run
```
python UGV_Static.py
```
### Example Input<br>
Enter obstacle density: medium<br>
Enter start (x y): 0 0<br>
Enter goal (x y): 69 69<br>

<br>
 Output:<br>
Graph Visualization<br>
	•	Grid represents the battlefield<br>
	•	Obstacles shown as blocked regions<br>
	•	Path plotted from start to goal<br>
	•	Start and Goal nodes clearly marked<br>
 Measures of Effectiveness (MoE)<br>
	•	Path Length → Number of steps in final path<br>
	•	Nodes Expanded → Total nodes explored<br>
	•	Time Taken → Execution time<br>
	•	Success Rate → Whether path found<br>
Example:<br>
Start: (0, 0)<br>
Goal: (69, 69)<br>
Path Length: 142<br>
Nodes Expanded: 560<br>
Time Taken: 0.02 seconds<br>
Success: Yes<br>

## Assumptions

- Movement is allowed in 4 directions (up, down, left, right)
- All movements have equal cost
- Obstacles are static (known beforehand)

