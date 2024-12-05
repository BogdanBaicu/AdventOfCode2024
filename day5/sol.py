import sys

rules = []
updates = []


def read_input():
    global rules, updates

    with open("input.txt", "r") as f:
        data = f.read()

    for line in data.split("\n"):
        if "|" in line:
            rules.append(line)
        else:
            updates.append(line)

    updates = list(filter(None, updates))

    for i in range(len(updates)):
        updates[i] = list(map(int, updates[i].split(",")))


def valid_updates_finder():
    valid_updates = []
    for update in updates:
        right_order = True
        for i in range(len(update) - 1):
            for j in range(i + 1, len(update)):
                # check if the string update[i]|update[i+1] is in the rules
                if f"{update[i]}|{update[j]}" not in rules:
                    right_order = False
                    break
        if right_order:
            valid_updates.append(update)
    
    return valid_updates
            

def invalid_updates_finder():
    invalid_updates = []
    valid_updates = valid_updates_finder()
    for update in updates:
        if update not in valid_updates:
            invalid_updates.append(update)

    return invalid_updates


def updates_fixer():
    invalid_updates = invalid_updates_finder()
    fixed_updates = []
    while invalid_updates:
        update = invalid_updates.pop()
        dict = {}
        for page in update:
            dict[page] = 0
        for page1 in update:
            for page2 in update:
                if f"{page1}|{page2}" in rules:
                    dict[page2] += 1
        fixed_update = []
        # sort the pages by the number of times they appear in the rules
        for page in sorted(dict, key=dict.get, reverse=True):
            fixed_update.append(page)
        fixed_updates.append(fixed_update)
    
    return fixed_updates


def middle_page_adder(updates):
    sum = 0
    for update in updates:
        sum += update[len(update) // 2]

    return sum


def main():
    read_input()
    print(middle_page_adder(valid_updates_finder()))
    print(middle_page_adder(updates_fixer()))

if __name__ == "__main__":
    main()