import sys
import copy

board = []
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir = 0


def read_input():
    global board
    with open('input.txt', 'r') as f:
        for line in f:
            board.append(list(line.strip()))


def find_start():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '^' or board[i][j] == 'v' or board[i][j] == '<' or board[i][j] == '>':
                return (i, j)


def move(pos):
    global board
    global dir
    x, y = pos
    boarddc = copy.deepcopy(board)
    boarddc[x][y] = 'X'

    x += directions[dir][0]
    y += directions[dir][1]

    while x >= 0 and x < len(boarddc) and y >= 0 and y < len(boarddc[x]):
        if boarddc[x][y] == '#':
            x -= directions[dir][0]
            y -= directions[dir][1]
            dir = (dir + 1) % 4
            boarddc[x][y] = 'X'
            x += directions[dir][0]
            y += directions[dir][1]
        else:
            boarddc[x][y] = 'X'

            x += directions[dir][0]
            y += directions[dir][1]
    return boarddc


def initial_direction(start_pos):
    global dir
    if board[start_pos[0]][start_pos[1]] == '^':
        dir = 0
    elif board[start_pos[0]][start_pos[1]] == '>':
        dir = 1
    elif board[start_pos[0]][start_pos[1]] == 'v':
        dir = 2
    else:
        dir = 3


def count_steps(board):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'X':
                count += 1
    return count


def main():
    global dir
    read_input()
    start_pos = find_start()
    initial_direction(start_pos)
    print(count_steps(move(start_pos)))
    

if __name__ == '__main__':
    main()