import heapq
import random
import time
import matplotlib.pyplot as plt
ROWS, COLS = 70, 70
def get_density(choice):
    if choice.lower() == "low":
        return 0.1
    elif choice.lower() == "medium":
        return 0.2
    elif choice.lower() == "high":
        return 0.3
    else:
        return 0.2
def generate_grid(density):
    grid = [[0]*COLS for _ in range(ROWS)]
    for i in range(ROWS):
        for j in range(COLS):
            if random.random() < density:
                grid[i][j] = 1
    return grid
def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(grid, start, goal):
    pq = []
    heapq.heappush(pq, (0, start))
    came_from = {}
    g = {start: 0}
    nodes_expanded = 0
    while pq:
        _, current = heapq.heappop(pq)
        nodes_expanded += 1
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], nodes_expanded
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
    return None, nodes_expanded
def plot_grid(grid, path, start, goal):
    plt.imshow(grid)
    if path:
        x = [p[1] for p in path]
        y = [p[0] for p in path]
        plt.plot(x, y)
    plt.scatter(start[1], start[0], marker='o')
    plt.scatter(goal[1], goal[0], marker='o')
    plt.title("UGV Path")
    plt.show()
def main():
    density_input = input("Enter obstacle density (low/medium/high): ")
    density = get_density(density_input)
    start = tuple(map(int, input("Enter start (x y): ").split()))
    goal = tuple(map(int, input("Enter goal (x y): ").split()))
    grid = generate_grid(density)
    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        print("Start or Goal is inside obstacle. Try again.")
        return
    start_time = time.time()
    path, nodes = astar(grid, start, goal)
    end_time = time.time()
    plot_grid(grid, path, start, goal)
    print("\n--- RESULTS ---")
    print("Start:", start)
    print("Goal:", goal)
    if path:
        print("Path Length:", len(path))
        print("Nodes Expanded:", nodes)
        print("Time Taken:", round(end_time - start_time, 4), "seconds")
        print("Success: Yes")
    else:
        print("No path found")
        print("Nodes Expanded:", nodes)
        print("Time Taken:", round(end_time - start_time, 4), "seconds")
        print("Success: No")
if __name__ == "__main__":
    main()