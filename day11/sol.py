from functools import cache


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        stones = list(map(int, file.read().split()))
    return stones


def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            digits = str(stone)
            mid = len(digits) // 2
            new_stones.append(int(digits[:mid]))
            new_stones.append(int(digits[mid:]))
        else:
            new_stones.append(stone * 2024)
    return new_stones


def count_stones(stones, blinks):
    for _ in range(blinks):
        stones = blink(stones)
    return len(stones)


@cache
def count_for_stone(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return count_for_stone(1, steps - 1)
    str_stone = str(stone)
    length = len(str_stone)
    if length % 2 == 0:
        return count_for_stone(int(str_stone[:length // 2]), steps - 1) + count_for_stone(int(str_stone[length // 2:]), steps - 1)
    return count_for_stone(stone * 2024, steps - 1)
    


def task2(stones, steps):
    return sum(count_for_stone(stone, steps) for stone in stones)


def main():
    stones = read_input()
    print(count_stones(stones, 25))
    print(task2(stones, 75))


if __name__ == "__main__":
    main()
