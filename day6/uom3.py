from anytree import NodeMixin, RenderTree, Node
from collections import defaultdict


class MyBaseClass(object):  # Just an example of a base class
    foo = 4


class MyClass(MyBaseClass, NodeMixin):  # Add Node feature
    def __init__(self, name, parent=None, children=None):
        super(MyClass, self).__init__()
        self.name = name
        self.parent = parent
        if children:
            self.children = children


my0 = MyClass('my0')
my1 = MyClass('m1', parent=my0)
my2 = MyClass('m2', parent=my0)


for pre, fill, node in RenderTree(my0):
    print("%s%s" % (pre, node.name))

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
