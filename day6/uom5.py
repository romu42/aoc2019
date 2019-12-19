#!/usr/bin/env python3
# by rog


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

def get_child(current_body, orbit_count):
    # print({current_body}, orbits[current_body])
    global total_orbit_count
    for bodies in orbits[current_body]:
        if bodies:
            for body in bodies:
                orbit_count += 1
                total_orbit_count = total_orbit_count + orbit_count
                print(f"{body}")
                print(f"{orbit_count}")
                get_child(body, orbit_count)
    return orbit_count, total_orbit_count


print(get_child('COM', 0))

if __name__ == "__main__":
    with open("test_input") as file:
        # data = file.read()
        new_list = []
        data = file.read().split("\n")
        # print(data)
        new_list = [item.split(")") for item in data]
        # print(new_list)
