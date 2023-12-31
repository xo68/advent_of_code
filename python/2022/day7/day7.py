import os
import re
import sys

FILE = "input.txt"

# https://adventofcode.com/2022/day/7

# Part 1
Total_part1 = 0  # Result for the first exercise

# Part 2
DISK_SPACE = 70000000  # 70M
REQUIRED_SPACE = 30000000  # 30M
Potential_candidate = []  # List all dir sizes that can be deleted


class Directory:
    def __init__(self, name, p_dir):
        self.name = name
        self.files = []  # List of files within the directory
        self.directories = {}  # Dictionnary of Dir Name <-> Dir Object
        self.current_directory = False  # is it the current directory ?
        self.previous_directory = p_dir  # Pointer to the previous Dir (cd ..)
        self.size = 0  # Sum of all the files size, incl. subdirectories


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


# Part 1, sum of all directories with size at most 100'000.
# At this stage, each dir contains already it's own size.
# We need to add the sub directories
# We naviage to tree Bottom -> Up
def calculate_size(dir):
    for d in dir.directories:
        calculate_size(dir.directories[d])
        dir.directories[d].previous_directory.size += dir.directories[d].size


# Part 1, Sum of all directories of size < 100'000
# We navigate the Tree and check the size of each directory
def calculate_sum(dir):
    for d in dir.directories:
        calculate_sum(dir.directories[d])
        dir_size = dir.directories[d].size
        if dir_size < 100000:
            global Total_part1
            Total_part1 += dir_size


def load():
    if not os.path.isfile(FILE):
        print(f'Input file "{FILE}" does not exist!')
        sys.exit()

    with open(FILE) as f:
        lines = f.readlines()

    # RegEx definitions
    ls = re.compile(r"^\$ ls")  # List directory content
    is_dir = re.compile(r"(^dir)\s(\w+)")  # Display dir name
    is_file = re.compile(r"(^\d+)\s([\w\.]+$)")  # Display File
    dir_cd_back = re.compile(r"^\$ cd \.\.")  # One step back "cd .."
    dir_cd_move = re.compile(r"(^\$ cd)\s(\w+)")  # Move to a directory

    current_dir = None  # Living pointer for the current position in the Tree
    root_dir = None  # Static pointer to the current durectory

    for line in lines:
        if is_file.match(line):
            match = is_file.match(line)
            current_dir.files.append(File(match.group(2), match.group(1)))
            current_dir.size += int(match.group(1))
        elif is_dir.match(line):
            match = is_dir.match(line)
            current_dir.directories[match.group(2)] = Directory(
                match.group(2), current_dir
            )
        elif dir_cd_back.match(line):
            current_dir = current_dir.previous_directory
        elif dir_cd_move.match(line):
            match = dir_cd_move.match(line)
            current_dir = current_dir.directories[match.group(2)]
        elif ls.match(line):
            pass
        else:
            # Entry point / Directory
            if re.match(r"^\$ cd /", line.strip()):
                current_dir = Directory("Root", None)
                current_dir.current_directory = True
                root_dir = current_dir
            else:
                print(f" <PARSING ERROR> {line.strip()}")
                sys.exit()
    return root_dir


# Part 2 of the exercice
# Put all directories's size in a list of candidate
def get_candidate(dir):
    for d in dir.directories:
        get_candidate(dir.directories[d])
        Potential_candidate.append(dir.directories[d].size)


# Part 2 of the exercice
# Return smallest directory size that will free up enough space
def calculate_part2(dir):
    unused_space = DISK_SPACE - dir.size
    get_candidate(dir)
    Potential_candidate.sort()
    for i in Potential_candidate:
        if i + unused_space > REQUIRED_SPACE:
            return i


def main():
    root = load()
    calculate_size(root)
    calculate_sum(root)
    print(f"Total Part1: {Total_part1}")
    print(f"Total Part2: {calculate_part2(root)}")


if __name__ == "__main__":
    main()
