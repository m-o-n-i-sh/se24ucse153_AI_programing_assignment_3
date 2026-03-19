# UGV Path Planning in Dynamic Environment using A* Algorithm
## Problem Statement
In the previous problem, obstacles were considered static and known beforehand. However, in real-world scenarios, obstacles can be dynamic and unknown a priority.  
Design an algorithm that enables an Unmanned Ground Vehicle (UGV) to navigate from a user-defined start node to a goal node in a grid-based battlefield environment while handling dynamic obstacles.The UGV must continuously adapt and find the optimal path** by replanning when obstacles appear.
---
## Objective
- Represent battlefield as a **grid (30×30)**
- Generate initial obstacles using density levels
- Simulate **dynamic obstacles appearing during navigation**
- Use **A\* algorithm with replanning**
- Visualize movement using a **graph**
- Compute performance metrics including replanning
---
## Algorithm Used
### A* Search with Dynamic Replanning
A* is used repeatedly as the UGV moves:
\[
f(n) = g(n) + h(n)
\]
Where:
- \( g(n) \): Cost from start to current node  
- \( h(n) \): Manhattan distance heuristic  
### Dynamic Behavior
- Plan path using A*
- Move step-by-step
- Detect new obstacles
- Replan if path is blocked
---
## Features
- User input for:
  - Obstacle density (low / medium / high)
  - Start coordinates
  - Goal coordinates
- Random obstacle generation
- Dynamic obstacle simulation during movement
- Continuous path replanning
- Graph visualization using matplotlib
- Performance metrics including replans
---
## Project Structure
```
Q3_UGV_Dynamic
├── UGV_Dynamic.py
├── requirements.txt
└── README.md
```
---
## Installation
### 1. Clone the repository

```bash
git clone https://github.com/m-o-n-i-sh/se24ucse153_AI_programing_assignment_3.git
cd se24ucse153_AI_programing_assignment_3/Q3_UGV_Dynamic
```
⸻
### 2. Install dependencies
```
pip install -r requirements.txt
```
⸻
## How to Run
```
python UGV_Dynamic.py
```
**Example Input<br>**
Enter density: medium<br>
Enter start (x y): 0 0<br>
Enter goal (x y): 29 29<br>
<br>
**Output<br>**
Graph Visualization<br>
	•	Grid represents the environment<br>
	•	Obstacles dynamically appear<br>
	•	Path updates in real-time<br>
	•	Start and Goal nodes clearly marked<br>
	•	Final path displayed after reaching goal<br>
Measures of Effectiveness (MoE)<br>
	•	Path Length → Total steps taken<br>
	•	Total Nodes Expanded → Total explored nodes<br>
	•	Replans → Number of times path was recalculated<br>
	•	Time Taken → Execution time<br>
**Example:<br>**
Start: (0, 0)<br>
Goal: (29, 29)<br>
Path Length: 95<br>
Total Nodes Expanded: 1200<br>
Replans: 4<br>
Time Taken: 0.15 seconds<br>

## Assumptions
- Movement is allowed in 4 directions
- All moves have equal cost
- Obstacles can appear dynamically at runtime
- Environment is partially unknown
