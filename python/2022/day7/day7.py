import os
import re
import sys

FILE = "input.txt"

# https://adventofcode.com/2022/day/7
Total_part1 = 0  # Result for the first exercise


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


def display(dir):
    print(f"Content of Directory {dir.name}, size={dir.size}")
    for f in dir.files:
        print(f"File:{f.name}")
    for d in dir.directories:
        print(f"Dir:{d}")
    for d in dir.directories:
        display(dir.directories[d])


# Part 1, sum of all directories with size at most 100'000.
# At this stage, each dir contains already it's own size.
# We need to add the sub directories
# We naviage to tree Bottom -> Up
def calculate_size(dir):
    for d in dir.directories:
        calculate_size(dir.directories[d])
        dir.directories[d].previous_directory.size += dir.directories[d].size


# Sum of all directories of size < 100'000
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
                print(f" <PARSING PARSING> {line.strip()}")
    return root_dir


def main():
    root = load()
    calculate_size(root)
    calculate_sum(root)
    # display(root)
    print(f"Total Part1: {Total_part1}")


if __name__ == "__main__":
    main()
