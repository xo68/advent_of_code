import os
import sys

FILE = "input.txt"


def main():
    elf_current, elf_max = 1, 1
    cal_current, cal_max = 0, 0

    if not os.path.isfile(FILE):
        print(f'Input file "{FILE}" does not exist!')
        sys.exit()

    with open(FILE) as f:
        lines = f.readlines()

    for line in lines:
        if line == "\n":
            if cal_max <= cal_current:
                cal_max = cal_current
                elf_max = elf_current

            elf_current = elf_current + 1
            cal_current = 0

        else:
            cal_current = cal_current + int(line)

    print(f"Elf:{elf_max}, Cal:{cal_max}")


if __name__ == "__main__":
    main()
