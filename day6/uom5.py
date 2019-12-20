#!/usr/bin/env python3
# by rog

from collections import defaultdict


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

# use a defaultdict to create dict of lists where each key has the values of the
# next orbiting bodies

orbits = defaultdict(list)
for item in my_list:
    orbits[item[0]].append(item[1])
print(orbits)

current = 'COM'
distance = 1

def set_distance(current, distance):
    orbits[currentdd

if __name__ == "__main__":
    with open("test_input") as file:
        # data = file.read()
        new_list = []
        data = file.read().split("\n")
        # print(data)
        new_list = [item.split(")") for item in data]
        # print(new_list)
