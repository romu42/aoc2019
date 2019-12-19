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
    # print(item[0], item[1])
    orbits[item[0]].append(item[1])
print(orbits)

# start at com and get next body
current_body = "COM"
next_body = orbits[current_body]
print(f"{current_body} -> {next_body}")
# current_body = next_body
orbit_count = 0

def get_next_body(current_body, orbit_count):
    for body in orbits[current_body]:
        orbit_count += 1
        if body:
            for bod in body:
                print(body)
                orbit_count = get_next_body(bod, orbit_count)
    return orbit_count

print(get_next_body('COM', orbit_count))




if __name__ == "__main__":
    with open("test_input") as file:
        # data = file.read()
        new_list = []
        data = file.read().split("\n")
        # print(data)
        new_list = [item.split(")") for item in data]
        # print(new_list)

