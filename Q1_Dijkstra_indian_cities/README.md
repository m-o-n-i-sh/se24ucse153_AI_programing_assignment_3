# Dijkstra’s Algorithm on Indian Road Network
## Problem Statement
When actions have different costs in a state-space search problem, an appropriate approach is **Uniform Cost Search (UCS)**, also known as **Dijkstra’s Algorithm** in theoretical computer science.
This project implements Dijkstra’s Algorithm to compute the shortest road distances between major cities in India using real-world distance data.
---
## Objective
- Model cities as nodes in a graph
- Use real road distances as edge weights
- Compute shortest paths using **Dijkstra’s Algorithm**
- Support dynamic addition/removal of cities
- Cache computed graph for faster reuse
---
##  Data Source
- Google Maps APIs:
  - **Geocoding API** → Convert city names to coordinates
  - **Distance Matrix API** → Fetch road distances
---
##  Features
- Add new cities dynamically
- Remove cities
- Rebuild graph using API
- Find shortest path between any two cities
- Display distances from a source city
- Cache graph to avoid repeated API calls
---
##  Project Structure
```text
Q1_Dijkstra_indian_cities
├── Dijkstra.py
├── graph_cache.json
├── .env
├── .gitignore
└── README.md
```
---
##  Setup Instructions
### 1. Clone the repository
```bash
git clone https://github.com/m-o-n-i-sh/se24ucse153_AI_programing_assignment_3.git
cd se24ucse153_AI_programing_assignment_3
```
### 2. Install dependencies
```
pip install python-dotenv
```
### 3. Setup API Key
Get an api key from Google maps platform:<br>https://console.cloud.google.com/project/_/google/maps-apis/credentials?utm_source=Docs_CreateAPIKey&utm_content=Docs_distance-matrix-backend&_gl=1*w791o2*_ga*MTg5MjEzNzUzNi4xNzYwMDg5NjAx*_ga_NRWSTWS78N*czE3NzM5MzgwNjUkbzMkZzEkdDE3NzM5MzgwNzMkajUyJGwwJGgw<br>
**Create a .env file:**
```text
GOOGLE_API_KEY=your_api_key_here
```
Do NOT share this file publicly.

### 4. Run the program
```text
python Dijkstra.py
```
**Menu Options**<br>
1 Add Cities<br>
2 Remove City<br>
3 Refresh Graph<br>
4 Shortest Path<br>
5 All Distances<br>
6 Show Cities<br>
7 Clear Cache<br>
8 Exit<br>
Example<br>
Choice: 4<br>
Source: Delhi<br>
Destination: Chennai<br>
Output:<br>
2200.5 km<br>
Delhi -> Nagpur -> Hyderabad -> Chennai<br>

**Caching**<br>
	•	Graph is stored in graph_cache.json<br>
	•	Avoids repeated API calls<br>
	•	Improves performance<br>

