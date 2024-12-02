import sys

a = []

def read_data():
    with open('input.txt', 'r') as f:
        for line in f:
            aux = []
            for i in line.split():
                aux.append(int(i))
            a.append(aux)


def is_descending(a):
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            return False
    return True


def is_ascending(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True


def diff_checker(a):
    for i in range(len(a) - 1):
        if abs(a[i] - a[i + 1]) < 1:
            return False
        if abs(a[i] - a[i + 1]) > 3:
            return False
    return True


def task1():
    count = 0
    for i in range(len(a)):
        if is_descending(a[i]) or is_ascending(a[i]):
            if diff_checker(a[i]):
                count += 1 
    
    return count


def task2():
    count = 0
    
    for i in range(len(a)):
        safe = False
        if is_descending(a[i]) or is_ascending(a[i]):
            if diff_checker(a[i]):
                count += 1 
                safe = True
        
        if not safe:
            for j in range(len(a[i])):
                aux = a[i].copy()
                aux.pop(j)
                if is_descending(aux) or is_ascending(aux):
                    if diff_checker(aux):
                        count += 1 
                        break   
    
    return count


def main():
    read_data()
    print(task1())
    print(task2())

if __name__ == '__main__':
    main()