from collections import defaultdict


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

orbits = defaultdict(list)
for item in my_list:
    orbits[item[0]].append(item[1])
print(orbits)

def get_child(parent, orbitals):
    print(parent)
    if len(orbits[parent])
    print(orbits[parent[0]])

# start at com and get next body
orbitals = ['COM']
current_body = "COM"
current_body = orbits[current_body]
orbitals.append(current_body)
orbitals = get_child(current_body, orbitals)


# while next_body:
#     print(f"{current_body} -> {next_body}")
#     if len(next_body) > 1:
#         for i in range(len(next_body)):
#     else:
#     orbit_count.append(next_body[0])
#     current_body = next_body[0]
#     next_body = orbits[current_body]
# print(orbit_count)
