import os
import sys

FILE = "input.txt"
data_temp = [[] for i in range(8)]
data = [[] for i in range(9)]
data_moves = []


def check_item(item):
    if item == " ":
        return False
    return item


def load_data():
    with open(FILE) as f:
        lines = f.readlines()

    if not os.path.isfile(FILE):
        print(f'Input file "{FILE}" does not exist!')
        sys.exit()

    i = 0
    for line in lines:
        if line[0] == "[":
            for x in range(9):
                c = line[x * 4 + 1]
                if check_item(c):
                    data_temp[i].append(c)
                else:
                    data_temp[i].append(c)
        elif line[0] == "m":
            data_moves.append([int(s) for s in line.split() if s.isdigit()])

        i = i + 1

    # We prepare the array with the data for later processing
    for i in range(len(data_temp)):
        temp_d = data_temp[len(data_temp) - 1 - i]
        for d in range(len(temp_d)):
            if temp_d[d] != " ":
                data[d].append(temp_d[d])


def execute_moves():
    for m in data_moves:
        for nb in range(m[0]):
            data[m[2] - 1].append(data[m[1] - 1].pop())


def execute_moves_v2():
    for m in data_moves:
        pop_index = len(data[m[1] - 1]) - m[0]
        for mo in range(m[0]):
            data[m[2] - 1].append(data[m[1] - 1].pop(pop_index))


def main():
    load_data()
    # execute_moves()
    execute_moves_v2()

    for line in data:
        print(f"Line:{line}")


if __name__ == "__main__":
    main()
