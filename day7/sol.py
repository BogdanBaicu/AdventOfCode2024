import sys

equations = []


def parse_input():
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.replace(':', '')
            equations.append(list(map(int, line.split())))


def decimal_to_padded_bin(decimal_number: int, total_bits: int) -> str:
    binary_number = bin(decimal_number)[2:]
    padded_binary = binary_number.zfill(total_bits)
    
    if len(padded_binary) > total_bits:
        raise ValueError(f"Cannot pad: Binary representation exceeds {total_bits} bits.")
    
    return list(map(int, padded_binary))


def decimal_to_padded_base3(decimal_number: int, total_digits: int) -> str:
    
    base3_number = ""
    while decimal_number > 0:
        base3_number = str(decimal_number % 3) + base3_number
        decimal_number //= 3
    
    base3_number = base3_number or "0"
    
    padded_base3 = base3_number.zfill(total_digits)
    
    if len(padded_base3) > total_digits:
        raise ValueError(f"Cannot pad: Base 3 representation exceeds {total_digits} digits.")
    
    return list(map(int, padded_base3))


def validate_equation(equation):
    for i in range(2**(len(equation) - 2)):
        op = decimal_to_padded_bin(i, len(equation) - 2)
        sum = equation[1]
        for j in range(len(op)):
            if op[j] == 0:
                sum += equation[j + 2]
            else:
                sum *= equation[j + 2]
        if sum == equation[0]:
            return True
    return False


def validate_equation2(equation):
    for i in range(3**(len(equation) - 2)):
        op = decimal_to_padded_base3(i, len(equation) - 2)
        sum = equation[1]
        for j in range(len(op)):
            if op[j] == 0:
                sum += equation[j + 2]
            elif op[j] == 1:
                sum *= equation[j + 2]
            else:
                sum = int(str(sum) + str(equation[j + 2]))
        if sum == equation[0]:
            return True
    return False

def task1():
    sum = 0
    for i in range(len(equations)):
        if validate_equation(equations[i]):
            sum += equations[i][0]
    print(sum)


def task2():
    sum = 0
    for i in range(len(equations)):
        if validate_equation2(equations[i]):
            sum += equations[i][0]
    print(sum)


def main():
    parse_input()
    task1()
    task2()

if __name__ == "__main__":
    main()