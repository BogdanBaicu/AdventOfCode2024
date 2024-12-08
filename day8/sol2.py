import sys

board = []


def read_input():
    global board
    with open('input.txt', 'r') as f:
        board = f.readlines()
        board = [x.strip() for x in board]
        board = [list(x) for x in board]
        

def is_on_line(x1, y1, x2, y2, x, y):
    if x1 == x2:
        return x == x1
    return abs((y - y1) * (x2 - x1) - (y2 - y1) * (x - x1)) < 1e-6


def task2():
    global board
    counter = 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] not in ['.', '#']:
                for ii in range(len(board)):
                    for jj in range(len(board[0])):
                        if board[ii][jj] == board[i][j] and (i != ii or j != jj):
                            for iii in range(len(board)):
                                for jjj in range(len(board[0])):
                                    if board[iii][jjj] == '.':
                                        if is_on_line(i, j, ii, jj, iii, jjj):
                                            board[iii][jjj] = '#'

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != '.':
                counter += 1
    
    return counter

    


def main():
    read_input()
    print(task2())


if __name__ == '__main__':
    main()