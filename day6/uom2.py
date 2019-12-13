#!/usr/bin/env python3
# by rog

from collections import defaultdict
from tempfile import TemporaryDirectory
import os
from anytree import Node, RenderTree, NodeMixin




class MyBaseClass(object):
    foo = 4

class Orbit(MyBaseClass, NodeMixin):
    def __init__(self, name, parent=None, children=None):
        super(Orbit, self).__init__()
        self.name = name
        self.parent = parent
        if children:
            self.children = children

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
    # print(item[0], item[1])
    orbits[item[0]].append(item[1])
print(orbits)

# start at com and get next body
current_body = "COM"
next_body = orbits[current_body]
orbit_count = ['COM']
COM = Orbit("COM")

for pre, fill, node in RenderTree(COM):
    print("%s%s" % (pre, node.name))
# B = Node("B", parent=COM)
# for key in orbits.keys():
#     COM.children = [orbits[key]]
for key in orbits.keys():
    if len(orbits[key]) > 1:
        parent = str(key)
        for i in range(len(orbits[key])):
            print(orbits[parent][i])
            child = str(orbits[parent][i])
            # child = Orbit(child, parent=parent)
            child = Orbit(child)
    else:
        print(key)
        child = orbits[parent][0]
        # child = Orbit(child, parent=parent)
        child = Orbit(child)

    # B = Node("B", parent=COM)
# C = Node("C", parent=B)
# D = Node("D", parent=C)
# E = Node("E", parent=D)
# F = Node("F", parent=E)
# G = Node("G", parent=B)
# H = Node("H", parent=G)
# I = Node("I", parent=D)
# J = Node("J", parent=E)
# K = Node("K", parent=J)
# L = Node("L", parent=K)

for pre, fill, node in RenderTree(COM):
    print("%s%s" % (pre, node.name))

