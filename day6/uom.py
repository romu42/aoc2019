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

# start at com and get next body
current_body = "COM"
total_orbit_count = 0
distance_from_com = ["COM"]


def get_child(current_body, orbit_count):
    global total_orbit_count
    global distance_from_com
    for bodies in orbits[current_body]:
        orbit_count += 1
        if bodies:
            for body in bodies:
                distance_from_com.append(body)
                print(
                    f"body={body}, orbit count={orbit_count}, total={total_orbit_count}"
                )
                get_child(body, orbit_count)
            total_orbit_count = total_orbit_count + orbit_count
    return orbit_count, total_orbit_count, distance_from_com

print(get_child("COM", 0))

if __name__ == "__main__":
    with open("test_input") as file:
        # data = file.read()
        new_list = []
        data = file.read().split("\n")
        # print(data)
        new_list = [item.split(")") for item in data]
        # print(new_list)
