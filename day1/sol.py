import sys

a = []
b = []

def read_data():
    with open('input.txt') as f:
        for line in f:
            a.append(int(line.split()[0]))
            b.append(int(line.split()[1]))

            
def task1():
    a.sort()
    b.sort()

    return sum(abs(a[i] - b[i]) for i in range(len(a)))


def task2():
    dict = {}
    for i in range(len(a)):
        dict[a[i]] = 0

    for aux in a:
        if dict[aux] == 0:
            count = 0
            for i in range(len(b)):
                if b[i] == aux:
                    count += 1
            dict[aux] = count
    
    return sum(a[i] * dict[a[i]] for i in range(len(a)))


def main():
    read_data()
    print(task1())
    print(task2())

if __name__ == '__main__':
    main()

