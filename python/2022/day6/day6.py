import os
import sys

FILE = "input.txt"


def check_duplicates(st, size):
    if len(set(st)) == size:
        return False
    else:
        return True


def load_n_process():
    if not os.path.isfile(FILE):
        print(f'Input file "{FILE}" does not exist!')
        sys.exit()

    with open(FILE) as f:
        lines = f.readlines()

    stream = lines[0]
    found1, found2 = False, False
    for i in range(len(stream) - 4):
        substr1, substr2 = stream[i : i + 4], stream[i : i + 14]
        if not (check_duplicates(substr1, 4)) and not found1:
            found1 = True
            print(f"Result1 >> {i + 4}")
        if not (check_duplicates(substr2, 14)) and not found2:
            found2 = True
            print(f"Result2 >> {i + 14}")


def main():
    load_n_process()


if __name__ == "__main__":
    main()
