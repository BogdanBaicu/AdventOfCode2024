import sys
import re


def read_data():
    with open('input.txt', 'r') as f:
        data = f.read()
    return data


def compute_sum(matches):
    sum = 0
    for match in matches:
        nums = re.findall(r'\d{1,3}', match)
        sum += int(nums[0]) * int(nums[1])
    return sum


def find_mul(data_str):
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    matches = re.findall(pattern, data_str)
    return matches


def extended_mul(data_str):
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    is_enabled = True
    sum = 0

    for match in re.finditer(f"{mul_pattern}|{do_pattern}|{dont_pattern}", data_str):
        instruction = match.group(0)
        
        if instruction == "do()":
            is_enabled = True
        elif instruction == "don't()":
            is_enabled = False
        else:
            mul_match = re.match(mul_pattern, instruction)
            if mul_match and is_enabled:
                x, y = map(int, mul_match.groups())
                sum += x * y 
    return sum


def main():
    data_str = read_data()
    print(compute_sum(find_mul(data_str)))
    print(extended_mul(data_str))
    


if __name__ == '__main__':
    main()