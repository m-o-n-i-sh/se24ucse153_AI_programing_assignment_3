#  AI Programming Assignment – Path Planning & Search Algorithms
##  Overview
This repository contains implementations of fundamental search and path planning algorithms applied to real world problems such as:
- Road network navigation (India cities)
- UGV (Unmanned Ground Vehicle) path planning in static environments
- UGV navigation in dynamic environments
---
## Repository Structure
```
.
├── Q1_Dijkstra_Indian_Cities
│   ├── Dijkstra.py
│   ├── graph_cache.json
│   └── README.md
│
├── Q2_UGV_Pathfinder
│   ├── UGV_Static.py
│   ├── requirements.txt
│   └── README.md
│
├── Q3_UGV_Dynamic
│   ├── UGV_Dynamic.py
│   ├── requirements.txt
│   └── README.md
│
├── .gitignore
└── README.md
```
---
##  Projects Included
---
###  Q1 – Dijkstra on Indian Cities
**Concept:** Uniform Cost Search (Dijkstra’s Algorithm)
- Models cities as graph nodes
- Uses real-world road distances (Google Maps API)
- Computes shortest path between cities
- Supports caching for performance
Folder: `Q1_Dijkstra_Indian_Cities`
---
###  Q2 – UGV Path Planning (Static Environment)
**Concept:** A* Search Algorithm
- Grid-based battlefield (70×70)
- Obstacles known beforehand
- User-defined start and goal
- Finds shortest path avoiding obstacles
- Graph visualization included
 Folder: `Q2_UGV_Pathfinder`
---
###  Q3 – UGV Path Planning (Dynamic Environment)
**Concept:** A* with Replanning
- Obstacles appear dynamically
- UGV continuously replans path
- Simulates real-world navigation
- Measures replanning efficiency
 Folder: `Q3_UGV_Dynamic`
---
##  Installation
### 1. Clone the repository
```bash
git clone https://github.com/m-o-n-i-sh/se24ucse153_AI_programing_assignment_3.git
cd se24ucse153_AI_programing_assignment_3
```
### 2. Install dependencies (for UGV projects)
```
pip install -r Q2_UGV_Pathfinder/requirements.txt
pip install -r Q3_UGV_Dynamic/requirements.txt
```
## How to Run
### Q1 – Dijkstra
```
python Q1_Dijkstra_Indian_Cities/Dijkstra.py
```
### Q2 – Static UGV
```
python Q2_UGV_Pathfinder/UGV_Static.py
```
### Q3 – Dynamic UGV
```
python Q3_UGV_Dynamic/UGV_Dynamic.py
```
## Important points
- Q1 requires a valid Google API Key(more instructions in the README.md file in the folder)
- UGV simulations use random obstacle generation
- Ensure dependencies are installed before running
