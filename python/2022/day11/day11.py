import os
import re
import sys

FILE = "input.txt"

# https://adventofcode.com/2022/day/10


def read_inputs() -> list:
    if not os.path.isfile(FILE):
        print(f'Input file "{FILE}" does not exist!')
        sys.exit()
    with open(FILE) as lines:
        return lines.readlines()


class Monkey:
    def __init__(self):
        self.inspect = 0

    def add_items(self, items):
        self.items = []
        for i in range(len(items)):
            self.items.append(int(items[i]))

    def clean_items(self):
        self.items.clear()

    def add_item(self, item):
        self.items.append(item)

    def set_op(self, op, val):
        self.op_type = op
        self.op_value = val

    def set_div_value(self, val):
        self.div_value = val

    def set_div_true(self, val):
        self.div_true = val

    def set_div_false(self, val):
        self.div_false = val

    def worry_level_item(self, id, div):
        self.inspect += 1
        if self.op_value == "old":
            self.items[id] = self.items[id] * self.items[id]
        elif self.op_type == "*":
            self.items[id] = self.items[id] * int(self.op_value)
        elif self.op_type == "+":
            self.items[id] = self.items[id] + int(self.op_value)
        # for part1 / 3
        # self.items[id] = int(self.items[id] / 3)

        # for part2
        self.items[id] = self.items[id] % div

    def throw(self, id) -> int:
        # Return monkey id to receive item id
        if self.items[id] % self.div_value == 0:
            return self.div_true
        else:
            return self.div_false

    def __str__(self):
        display = f"items:{self.items} "
        display += f"op type[{self.op_type}] "
        display += f"op va:[{self.op_value}] "
        display += f"div:[{self.div_value}] "
        display += f"true:[{self.div_true}] "
        display += f"false:[{self.div_false}] "
        return display


def part1():
    input = read_inputs()
    monkeys = []
    monkey_id = -1
    global_div = 1

    monkey = re.compile(r"(^Monkey )(.*)(:$)")
    items = re.compile(r"(^  Starting items:)(.*)")
    op = re.compile(r"(^.*= old )(.) (.*)")
    test = re.compile(r"(^  Test: divisible by )(.*)")
    test_true = re.compile(r"(^.*true: throw to monkey )(.*)")
    test_false = re.compile(r"(^.*false: throw to monkey )(.*)")

    for line in input:
        if monkey.match(line):
            monkeys.append(Monkey())
            monkey_id += 1
        elif items.match(line):
            li = items.match(line).group(2).replace(" ", "").split(",")
            monkeys[monkey_id].add_items(li)
        elif op.match(line):
            o = op.match(line).group(2)
            v = op.match(line).group(3)
            monkeys[monkey_id].set_op(o, v)
        elif test.match(line):
            t = test.match(line).group(2)
            monkeys[monkey_id].set_div_value(int(t))
            global_div *= int(t)
        elif test_true.match(line):
            t = test_true.match(line).group(2)
            monkeys[monkey_id].set_div_true(int(t))
        elif test_false.match(line):
            t = test_false.match(line).group(2)
            monkeys[monkey_id].set_div_false(int(t))

    for round in range(10000):
        for m in monkeys:
            for i in range(len(m.items)):
                m.worry_level_item(i, global_div)
                monkeys[m.throw(i)].add_item(m.items[i])
            m.clean_items()

    inspect = []
    for m in monkeys:
        inspect.append(m.inspect)
    inspect.sort()
    print(f"Result={inspect[-1]*inspect[-2]}")


if __name__ == "__main__":
    part1()
