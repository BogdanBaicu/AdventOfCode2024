import sys

grid = []
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
trails = []


def read_input():
    global grid

    with open('input.txt', 'r') as f:
        grid = f.readlines()
        grid = [x.strip() for x in grid]
        grid = [list(x) for x in grid]
        grid = [[int(x) for x in row] for row in grid]
            

def find_trail(trailhead, current_position):
    global trails
    
    for direction in directions:
        new_position = (current_position[0] + direction[0], current_position[1] + direction[1])
        if 0 <= new_position[0] < len(grid) and 0 <= new_position[1] < len(grid[0]) and grid[new_position[0]][new_position[1]] == 9 and grid[current_position[0]][current_position[1]] + 1 == grid[new_position[0]][new_position[1]]:
            trails.append((trailhead, new_position))
        else:
            if 0 <= new_position[0] < len(grid) and 0 <= new_position[1] < len(grid[0]) and grid[new_position[0]][new_position[1]] == grid[current_position[0]][current_position[1]] + 1:
                find_trail(trailhead, new_position)


def task1():
    global trails

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                find_trail((i, j), (i, j))

    trails = list(set(trails))
    trailheads_counter = []
    for i in range (len(trails)):
        found = False
        for j in range(len(trailheads_counter)):
            if trails[i][0] == trailheads_counter[j][0]:
                trailheads_counter[j][1] += 1
                found = True
                break
        if not found:
            trailheads_counter.append([trails[i][0], 1])
    
    sum = 0
    for i in range(len(trailheads_counter)):
        sum += trailheads_counter[i][1]
    # trailheads_counter = sorted(trailheads_counter, key=lambda x: x[0])
    # trails = sorted(trails, key=lambda x: x[0])
    return sum


def main():
    read_input()
    print(task1())



if __name__ == '__main__':
    main()