# https://adventofcode.com/2019/day/3

""" R, Right is +x
    L, Left is -x
    U, Up is +y
    D, Down is -y
    manhattan distance is |x1 - x2| + |y1 - y2|

    """


def closest_intersect(path1: list, path2: list) -> int:
    positions = [element for element in path1 if element in path2]
    positions = [element for element in positions if element != (0,0)]
    distances = []

    for x, y in positions:
        distances.append(abs(0 - x) + abs(0 - y))
        distances.sort()
    return distances[0]



def get_wire_path(moves: list) -> list:
    wire = [(0, 0)]
    for move in moves:
        if move[0] == 'R':
            wire = move_right(move[1:], wire)
        elif move[0] == 'L':
            wire = (move_left(move[1:], wire))
        elif move[0] == 'U':
            wire = move_up(move[1:], wire)
        elif move[0] == 'D':
            wire = move_down(move[1:], wire)
    return wire


def move_right(move: str, wire: list) -> list:
    x, y = wire[-1]
    for delta in range(1, int(move) + 1):
        wire.append((x + delta, y))
    return wire


def move_left(move: int, wire: list) -> list:
    x, y = wire[-1]
    for delta in range(1, int(move) + 1):
        wire.append((x - delta, y))
    return wire


def move_up(move: int, wire: list) -> list:
    x, y = wire[-1]
    for delta in range(1, int(move) + 1):
        wire.append((x, y + delta))
    return wire


def move_down(move: int, wire: list) -> list:
    x, y = wire[-1]
    for delta in range(1, int(move) + 1):
        wire.append((x, y - delta))
    return wire


if __name__ == '__main__':
    with open("puzzle_input") as file:
        moves = [line.rstrip() for line in file]
        wire1_path = get_wire_path(moves[0].split(','))
        wire2_path = get_wire_path(moves[1].split(','))
        # print(wire1_path)
        # print(wire2_path)
        common = [element for element in wire1_path if element in wire2_path]
        print(common)
        print(sorted([wire1_path.index(item) + wire2_path.index(item) for item in common])[1])
        print(closest_intersect(wire1_path, wire2_path))


