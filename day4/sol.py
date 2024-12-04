import sys

directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 1),
    (1, 1),
    (-1, -1),
    (1, -1)
]
word = 'XMAS'
word_len = len(word)
data = []
rows = 0
cols = 0


def read_data():
    with open('input.txt', 'r') as f:
        data = f.read()
    lines = data.split('\n')
    lines = list(filter(lambda x: x != '', lines))
    global rows, cols
    rows = len(lines)
    cols = len(lines[0])
    return lines


def check_word(posx, posy, dirx, diry):
    for i in range(word_len):
        auxx = posx + i * dirx
        auxy = posy + i * diry
        if auxx < 0 or auxx >= rows or auxy < 0 or auxy >= cols or data[auxx][auxy] != word[i]:
            return False
    return True


def count_words():
    count = 0
    for i in range(rows):
        for j in range(cols):
            for direction in directions:
                if check_word(i, j, direction[0], direction[1]):
                    count += 1
    return count


def count_x_mas():
    count = 0
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if data[i][j] == 'A':
                if (data[i - 1][j - 1] == 'M' and data[i + 1][j + 1] == 'S') or data[i - 1][j - 1] == 'S' and data[i + 1][j + 1] == 'M':
                    if (data[i - 1][j + 1] == 'M' and data[i + 1][j - 1] == 'S') or data[i - 1][j + 1] == 'S' and data[i + 1][j - 1] == 'M':
                        count += 1
    return count
                


def main():
    global data
    data = read_data()
    print(count_words())
    print(count_x_mas())


if __name__ == '__main__':
    main()