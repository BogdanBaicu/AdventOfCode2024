import sys

disk_map = []
disk = []


def read_input():
    with open('input.txt', 'r') as f:
        data = f.read()
    data = [int(x) for x in data if x != '\n']
    return data


def disk_map_to_disk(disk_map):
    file_type = True
    index = 0
    for i in range(len(disk_map)):
        if file_type:
            for j in range(disk_map[i]):
                disk.append(index)
            index += 1
            file_type = False    

        else:
            for j in range(disk_map[i]):
                disk.append('.')
            file_type = True
    return disk


def file_compact(disk):
    for i in range(len(disk)):
        if disk[i] == '.':
            for j in range(len(disk)-1, i, -1):
                if disk[j] != '.':
                    disk[i], disk[j] = disk[j], disk[i]
                    break
    return disk


def file_compact_enhaced(disk, disk_map):
    disk_list = []
    pos = 0
    index = 0
    new_disk_list = []
    new_disk = []
    while pos < len(disk):
        disk_list.append((disk_map[index], disk[pos]))
        pos += disk_map[index]
        index += 1
    for i in range(len(disk_list)):
        if disk_list[i][1] != '.':
            new_disk_list.append(disk_list[i])
        else:
            size = disk_list[i][0]
            added = False
            for j in range(len(disk_list)-1, i, -1):
                if disk_list[j][1] != '.':
                    if disk_list[j][0] <= size:
                        new_disk_list.append(disk_list[j])
                        size -= disk_list[j][0]
                        added = True
                        disk_list[j] = (disk_list[j][0], '.')
            if added and size > 0:
                new_disk_list.append((size, '.'))
            if not added:
                new_disk_list.append((disk_list[i][0], '.'))
    for i in range(len(new_disk_list)):
        for j in range(new_disk_list[i][0]):
            new_disk.append(new_disk_list[i][1])
    return new_disk
            


def file_checksum(disk):
    sum = 0
    for i in range(len(disk)):
        if disk[i] != '.':
            sum += disk[i] * i
        
    return sum


def main():
    disk_map = read_input()
    print(file_checksum(file_compact(disk_map_to_disk(disk_map))))
    print(file_checksum(file_compact_enhaced(disk_map_to_disk(disk_map), disk_map)))


if __name__ == '__main__':
    main()