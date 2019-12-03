# https://adventofcode.com/2019/day/3

""" R, Right is +x
    L, Left is -x
    U, Up is +y
    D, Down is -y
    manhattan distance is |x1 - x2| + |y1 - y2|

    """

def closest_intersect(moves):
    wire1 = [(0,0)]
    wire2 = [[0,0]]
    for move in moves:
        print(move)


def move_right(move: str) -> list:
    move_list = []
    return moves_list


def move_left(move: str) -> list:
    moves_list = []
    return moves_list


def move_up(move: str) -> list:
    moves_list = []
    return moves_list


def move_down(move: str) -> list:
    moves_list = []
    return moves_list


if __name__ == '__main__':
    with open("puzzle_input") as file:
        moves = [line.rstrip() for line in file]
        wire1_path = get_wire_path(moves[0])
        wire2_path = get_wire_path(moves[1])

