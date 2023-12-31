import os
import re
import sys

FILE = "input.txt"


def read_inputs():
    if not os.path.isfile(FILE):
        print(f'Input file "{FILE}" does not exist!')
        sys.exit()
    with open(FILE) as lines:
        return lines.readlines()


def return_value(value):
    values = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    return str(values.index(value)) if value in values else value


def main():
    res1, res2 = 0, 0

    # PART 1 #
    digits = re.compile(r"[1-9]")
    for line in read_inputs():
        all = digits.findall(line)
        val = all[0] * 2 if len(all) == 1 else all[0] + all[-1]
        res1 += int(val)
    print(f"Result1:{res1}")

    # PART 2 #
    values = "one|two|three|four|five|six|seven|eight|nine|[1-9]"
    all = re.compile(values)  # Return all matches that are non-overlap
    last = re.compile(r"(?:.*)(" + values + ")")  # Return only the last match

    for line in read_inputs():
        val1 = all.findall(line)[0]
        val2 = last.findall(line)[0]
        res2 += int(return_value(val1) + return_value(val2))
    print(f"Result2:{res2}")


if __name__ == "__main__":
    main()
