#!/usr/bin/env python3
# by rog

from collections import defaultdict
from tempfile import TemporaryDirectory
import os

if __name__ == "__main__":
    with open("test_input") as file:
        # data = file.read()
        new_list = []
        data = file.read().split("\n")
        # print(data)
        new_list = [item.split(")") for item in data]
        # print(new_list)


my_list = [
    ["B", "C"],
    ["C", "D"],
    ["D", "E"],
    ["E", "F"],
    ["B", "G"],
    ["G", "H"],
    ["D", "I"],
    ["E", "J"],
    ["J", "K"],
    ["K", "L"],
    ["COM", "B"],
]
# create a direcotry
def create_directory(pathname):
    try:
        os.makedirs(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s" % path)

# use a defaultdict to create dict of lists where each key has the values of the
# next orbiting bodies

orbits = defaultdict(list)
for item in my_list:
    # print(item[0], item[1])
    orbits[item[0]].append(item[1])
print(orbits)

# start at com and get next body
current_body = "COM"
next_body = orbits[current_body]
orbit_count = ['COM']
# create temp dir to workin
# dir = TemporaryDirectory()
# define the name of the directory to be created
path = current_body
create_directory(path)

# go from body to body and build the tree
os.chdir(path)
while next_body:
    print(f"{current_body} -> {next_body}")
    if len(next_body) > 1:
        for i in range(len(next_body)):
            path = next_body[i]
            create_directory(path)
    else:
        path = next_body[0]
        create_directory(path)


   orbit_count.append(next_body[0])
   current_body = next_body[0]
   next_body = orbits[current_body]
   os.chdir(path)
print(orbit_count)
