import sys

# Define global variables
grid = []
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def read_input():
    global grid
    with open('input.txt', 'r') as f:
        grid = [list(map(int, line.strip())) for line in f.readlines()]

def find_trail(trailhead, current_position, visited):
    x, y = current_position
    visited.add(current_position)
    score = 0

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if (nx, ny) not in visited:
                if grid[nx][ny] == grid[x][y] + 1:
                    if grid[nx][ny] == 9:
                        score += 1
                    else:
                        score += find_trail(trailhead, (nx, ny), visited)

    visited.remove(current_position)
    return score

def task2():
    trailheads_scores = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                trailhead = (i, j)
                visited = set()
                trailheads_scores[trailhead] = find_trail(trailhead, trailhead, visited)

    return sum(trailheads_scores.values())

def main():
    read_input()
    print(task2())

if __name__ == '__main__':
    main()
