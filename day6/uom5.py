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
distance = 0
orbit_lst = [['COM']]


def set_distance(current, distance):
    orbit_lst.append([orbits[current], distance])
    print(orbit_lst)


def add_orbit_lst(current):
    tmp_lst = []
    for parent in current:
        for orbit in orbits[current]:
            tmp_lst.append(orbit)
        orbit_lst.append(tmp_lst)

# set_distance(current, distance)
add_orbit_lst('COM')
add_orbit_lst('B')
for orb in orbit_lst[-1]:
    print(orb)

print(orbit_lst)
print(len(orbit_lst[2]))


if __name__ == "__main__":
    with open("test_input") as file:
        # data = file.read()
        new_list = []
        data = file.read().split("\n")
        # print(data)
        new_list = [item.split(")") for item in data]
        # print(new_list)
