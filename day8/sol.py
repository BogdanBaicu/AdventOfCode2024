import sys

board = []


def read_input():
    global board
    with open('input.txt', 'r') as f:
        board = f.readlines()
        board = [x.strip() for x in board]
        board = [list(x) for x in board]
        

def task1():
    global board
    overlap = []
    counter = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] not in ['.', '#']:
                for ii in range(i, len(board)):
                    for jj in range(len(board[ii])):
                        if board[ii][jj] == board[i][j] and i != ii and j != jj:
                            difx = i - ii
                            dify = j - jj
                            if 0 <= ii - difx < len(board) and 0 <= jj - dify < len(board[i]):
                                if board[ii - difx][jj - dify] == '.':
                                    board[ii - difx][jj - dify] = '#'
                                    counter += 1
                                else:
                                    if board[ii - difx][jj - dify] != '#':
                                        overlap.append((ii - difx, jj - dify))
                                
                            if 0 <= i + difx < len(board) and 0 <= j + dify < len(board[i]):
                                if board[i + difx][j + dify] == '.':
                                    board[i + difx][j + dify] = '#'
                                    counter += 1
                                else:
                                    if board[i + difx][j + dify] != '#':
                                        overlap.append((i + difx, j + dify))
    overlap = list(set(overlap))
    return counter + len(overlap)
    


def main():
    read_input()
    print(task1())


if __name__ == '__main__':
    main()