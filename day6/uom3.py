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

COM = MyClass('COM')
orbits = defaultdict(list)
for item in my_list:
    print('bob')
    MyClass(item[0])
    item[1] = MyClass(item[1], parent=item[0])
    orbits[item[0]].append(item[1])
print(orbits)

for pre, fill, node in RenderTree(COM):
    print("%s%s" % (pre, node.name))
