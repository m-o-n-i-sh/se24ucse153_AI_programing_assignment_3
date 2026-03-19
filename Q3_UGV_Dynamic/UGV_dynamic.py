import heapq
import random
import time
import matplotlib.pyplot as plt
ROWS, COLS = 30, 30
def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
def generate_grid(density):
    grid = [[0]*COLS for _ in range(ROWS)]
    for i in range(ROWS):
        for j in range(COLS):
            if random.random() < density:
                grid[i][j] = 1
    return grid
def astar(grid, start, goal):
    pq = []
    heapq.heappush(pq, (0, start))
    came_from = {}
    g = {start: 0}
    nodes = 0
    while pq:
        _, current = heapq.heappop(pq)
        nodes += 1
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], nodes
        x, y = current
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == 0:
                new_cost = g[current] + 1
                if (nx, ny) not in g or new_cost < g[(nx, ny)]:
                    g[(nx, ny)] = new_cost
                    f = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(pq, (f, (nx, ny)))
                    came_from[(nx, ny)] = current
    return None, nodes
def add_dynamic_obstacles(grid, probability=0.05):
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 0 and random.random() < probability:
                grid[i][j] = 1
def plot(grid, path, start, goal):
    plt.imshow(grid)
    if path:
        x = [p[1] for p in path]
        y = [p[0] for p in path]
        plt.plot(x, y)
    plt.scatter(start[1], start[0], marker='o')
    plt.scatter(goal[1], goal[0], marker='o')
    plt.title("Dynamic UGV Path Planning")
    plt.pause(0.3)
    plt.clf()
def main():
    density_input = input("Enter density (low/medium/high): ").lower()
    density = {"low":0.1, "medium":0.2, "high":0.3}.get(density_input, 0.2)
    start = tuple(map(int, input("Enter start (x y): ").split()))
    goal = tuple(map(int, input("Enter goal (x y): ").split()))
    grid = generate_grid(density)
    current = start
    total_path = []
    total_nodes = 0
    replans = 0
    start_time = time.time()
    plt.figure()
    while current != goal:
        path, nodes = astar(grid, current, goal)
        total_nodes += nodes
        if not path:
            print("No path possible")
            break
        for step in path[1:]:
            current = step
            total_path.append(current)
            add_dynamic_obstacles(grid, 0.02)
            if grid[current[0]][current[1]] == 1:
                replans += 1
                break
            plot(grid, total_path, start, goal)
            if current == goal:
                break
    end_time = time.time()
    plt.title("Final Path (Goal Reached)")
    plt.imshow(grid)
    if total_path:
        x = [p[1] for p in total_path]
        y = [p[0] for p in total_path]
        plt.plot(x, y)
    plt.scatter(start[1], start[0], marker='o')
    plt.scatter(goal[1], goal[0], marker='o')
    plt.show()
    print("\n--- RESULTS ---")
    print("Start:", start)
    print("Goal:", goal)
    print("Path Length:", len(total_path))
    print("Total Nodes Expanded:", total_nodes)
    print("Replans:", replans)
    print("Time Taken:", round(end_time - start_time, 4), "seconds")
if __name__ == "__main__":
    main()