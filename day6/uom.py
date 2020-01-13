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
    """ gets the node object based on the node name
    """
    for n in node_list:
        if n.name == obj:
            return n
    raise Exception('no node name found pound panic button')

def get_or_create_node(node_list: list, obj: str):
    """ return node if it exits or creates and returns it if it doesn't
    """
    for n in node_list:
        if n.name == obj:
            return n
    n = Node(obj)
    node_list.append(n)
    return n

def get_transfer_node(path_1: list, path_2: list):
    """ get the transfer node and the distance from YOU or SAN
    """
    path_count = 0
    for item in path_1:
        if item in path_2:
            return (item, path_count)
        else:
            path_count += 1




if __name__ == '__main__':
    #with open("test_input") as file:
    with open("puzzle_input") as file:
        obj_list = []
        data = file.read().split("\n")
        """ 
        Create all the nodes, create connections to parent and child as necessary
        """
        for item in data:
            if not item:
                continue
            parent, child = item.split(")")
            child = get_or_create_node(obj_list, child)
            parent = get_or_create_node(obj_list, parent)
            assert child.parent == None
            child.parent = parent
        """
        using a list of all the objects get the total of all orbits
        """
        dist = 0
        for obj in obj_list:
            dist = dist + obj.get_distance()
        #print(dist)

        """
        Part2, get the paths to COM and then find the nearest intersection, then
        find the distance for an orbital transfer
        """
        YOU = get_me(obj_list, 'YOU')
        SAN = get_me(obj_list, 'SAN')
        you_path = YOU.get_path()
        san_path = SAN.get_path()
        trans1, trans1_distance = (get_transfer_node(you_path, san_path))
        trans2, trans2_distance = (get_transfer_node(san_path, you_path))
        print(trans1_distance + trans2_distance)

