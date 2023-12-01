import os
import re
import sys

FILE = "input.txt"


def read_inputs() -> list:
    if not os.path.isfile(FILE):
        print(f'Input file "{FILE}" does not exist!')
        sys.exit()
    with open(FILE) as lines:
        return lines.readlines()


def return_value(str_val):
    if str_val == "one":
        return "1"
    elif str_val == "two":
        return "2"
    elif str_val == "three":
        return "3"
    elif str_val == "four":
        return "4"
    elif str_val == "five":
        return "5"
    elif str_val == "six":
        return "6"
    elif str_val == "seven":
        return "7"
    elif str_val == "eight":
        return "8"
    elif str_val == "nine":
        return "9"
    return str_val


def main():
    res1, res2 = 0, 0

    ##### PART 1 #####
    digits = re.compile(r"([1-9])")
    for line in read_inputs():
        all = digits.findall(line)
        if len(all) == 1:
            val = all[0] * 2
        else:
            val = all[0] + all[-1]
        res1 += int(val)
    print(f"Result1:{res1}")

    ##### PART 2 #####
    # Return all matches that are non-overlap
    all = re.compile(r"(one|two|three|four|five|six|seven|eight|nine|[1-9])")
    # Return only the last match
    last = re.compile(r"(?s:.*)(one|two|three|four|five|six|seven|eight|nine|[1-9])")

    for line in read_inputs():
        val1 = all.findall(line)[0]  # First match that is found
        val2 = last.findall(line)[0]  # There is only 1 match, the last one
        res2 += int(return_value(val1) + return_value(val2))
    print(f"Result2:{res2}")


if __name__ == "__main__":
    main()
