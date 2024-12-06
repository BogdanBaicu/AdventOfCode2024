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


def will_loop(oi, oj, ii, jj, board):
    if board[oi][oj] == "#":
        return False

    board[oi][oj] = "#"
    i, j = ii, jj
    dir = 0 
    seen = set()

    while True:
        if (i, j, dir) in seen:
            board[oi][oj] = "."
            return True
        seen.add((i, j, dir))

        next_i = i + directions[dir][0]
        next_j = j + directions[dir][1]

        if not (0 <= next_i < len(board) and 0 <= next_j < len(board[0])):
            board[oi][oj] = "."
            return False

        if board[next_i][next_j] == "#":
            dir = (dir + 1) % 4
        else:
            i, j = next_i, next_j


def task2():
    global dir
    visited = set()
    start_pos = find_start()
    ii, jj = start_pos 
    i, j = ii, jj 
    while True:
        visited.add((i, j))

        next_i = i + directions[dir][0]
        next_j = j + directions[dir][1]

        if not (0 <= next_i < len(board) and 0 <= next_j < len(board[0])):
            break

        if board[next_i][next_j] == "#":
            dir = (dir + 1) % 4
        else:
            i, j = next_i, next_j

    counter = 0
    for oi, oj in visited:
        loop = will_loop(oi, oj, ii, jj, board) 
        counter += loop

    print(counter)


def main():
    global dir
    read_input()

    task2()
    
    

    

if __name__ == '__main__':
    main()