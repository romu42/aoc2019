#!/usr/bin/env python3
# by rog


class Node:
    parent = None


    def __init__(self, name: str):
        self.name = name


    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def hello(self):
        print(f"hey i am {self.name} and my parent is {self.parent}")


    def get_distance(self):
        """ gets the distance to COM """

        distance = 0
        if self.parent is None:
            return distance

        next_node = self
        while True:
            next_node = next_node.parent
            if next_node is None:
                return distance
            distance += 1

    def get_path(self):
        """ returns the path to COM """
        path = []
        if self.parent is None:
            return path
        next_node = self
        while True:
            next_node = next_node.parent
            if next_node is None:
                return path
            path.append(next_node)
        return path


def get_me(node_list: list, obj: str):
    for n in node_list:
        if n.name == obj:
            return n
    raise Exception('no node name found pound panic button')

def get_or_create_node(node_list: list, obj: str):
    for n in node_list:
        if n.name == obj:
            return n
    n = Node(obj)
    node_list.append(n)
    return n


if __name__ == '__main__':
    with open("test_input") as file:
    #with open("puzzle_input") as file:
        obj_list = []
        data = file.read().split("\n")
        for item in data:
            if not item:
                continue
            parent, child = item.split(")")
            child = get_or_create_node(obj_list, child)
            parent = get_or_create_node(obj_list, parent)
            assert child.parent == None
            child.parent = parent
        dist = 0
        for obj in obj_list:
            dist = dist + obj.get_distance()

        print(dist)
        YOU = get_me(obj_list, 'YOU')
        SAN = get_me(obj_list, 'SAN')
        youlist = YOU.get_path()
        sanlist = SAN.get_path()
