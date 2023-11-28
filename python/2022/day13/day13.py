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


# Ugly !! -> Add "[[2]]" and "[[6]]" to the input file
def process2():
    status = True
    inputs = read_inputs()
    old = list()
    new = list()

    for i in range(len(inputs)):
        if inputs[i] != "\n":
            old.append(inputs[i].strip())

    while old:
        # print(f"OLD:{old}")
        for i in range(len(old)):
            line = list(old[i])
            for j in range(len(old)):
                if j != i:
                    line2 = list(old[j])

                    if compare_lists(line[:], line2[:]):
                        status = True
                    else:
                        status = False
                        break

            if status:
                new.append(old[i])
                old.pop(i)
                break

    for i, item in enumerate(new):
        if item == "[[2]]":
            result2 = i + 1
        if item == "[[6]]":
            result2 *= i + 1
    print(f"Result part 2: {result2}")


def process():
    pair = 0
    result1 = 0
    p1, p2 = str(), str()
    inputs = read_inputs()
    for i in range(len(inputs)):
        if inputs[i] == "\n":
            p1, p2 = str(), str()
        elif p1 == "":
            p1 = inputs[i].strip()
        else:
            p2 = inputs[i].strip()

        if p1 and p2:
            pair += 1

            l = list(p1)
            r = list(p2)

            if compare_lists(l, r):
                result1 += pair
    print(f"Result part 1: {result1}")


def compare_lists(l, r):
    l.pop(), l.pop(0), r.pop(), r.pop(0)

    while True:
        cl = None
        cr = None

        if l:
            if l[0] == ",":
                cl = l.pop(0)
            elif l[0].isalnum():
                cl = l.pop(0)
                if l and l[0].isalnum():
                    cl = cl + l.pop(0)
                cl = int(cl)
            elif l[0] == "[":
                cl = "["
            elif l[0] == "]":
                cl = "]"

        if r:
            if r[0] == ",":
                cr = r.pop(0)
            elif r[0].isalnum():
                cr = r.pop(0)
                if r and r[0].isalnum():
                    cr = cr + r.pop(0)
                cr = int(cr)
            elif r[0] == "[":
                cr = "["
            elif r[0] == "]":
                cr = "]"

        if cl is not None and cr is not None:
            if cl == "]" and type(cr) is int:
                return True
            if cl == "]" and cr == "[":
                return True
            if cr == "]" and type(cl) is int:
                return False
            if cr == "]" and cl == "[":
                return False

            if cl == "[":
                l.pop(0)
            if cr == "[":
                r.pop(0)

            if cl == "]" and cr == "]":
                r.pop(0), l.pop(0)

            if type(cl) is int and type(cr) is int:
                if cl < cr:
                    return True
                elif cl > cr:
                    return False

            if type(cl) is int and cr == "]":
                return False
            elif type(cr) is int and cl == "]":
                return True

            if type(cl) is int and cr == "[":
                l.insert(0, "]")
                l.insert(0, str(cl))
                l.insert(0, "[")
                r.insert(0, "[")
            elif type(cr) is int and cl == "[":
                r.insert(0, "]")
                r.insert(0, str(cr))
                r.insert(0, "[")
                l.insert(0, "[")

        if len(l) == 0:
            return True
        if len(r) == 0:
            return False
    return True


if __name__ == "__main__":
    process()
    process2()
