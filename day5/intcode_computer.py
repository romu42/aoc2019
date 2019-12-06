from itertools import product
from collections import deque


def computer(memory: list) -> (list, int):
    position = 0
    end = len(memory)

    while position < end:
        opcode, param_mode1, param_mode2, param_mode3 = parse_instructions(
            memory[position]
        )
        if opcode == 99:
            return memory
        elif opcode == 1:
            memory, position = opcode_1(
                memory, position, param_mode1, param_mode2, param_mode3
            )
        elif opcode == 2:
            memory, position = opcode_2(
                memory, position, param_mode1, param_mode2, param_mode3
            )
        elif opcode == 3:
            memory, position = opcode_3(
                memory, position
            )
        elif opcode == 4:
            memory, position = opcode_4(
                memory, position, param_mode1
            )
        elif opcode == 5:
            memory, position = opcode_5(
                memory, position, param_mode1, param_mode2, param_mode3
            )
        elif opcode == 6:
            memory, position = opcode_6(
                memory, position, param_mode1, param_mode2, param_mode3
            )
        elif opcode == 7:
            memory, position = opcode_7(
                memory, position, param_mode1, param_mode2, param_mode3
            )
        elif opcode == 8:
            memory, position = opcode_8(
                memory, position, param_mode1, param_mode2, param_mode3
            )

    return memory


def opcode_1(
    memory: list, position: int, param_mode1: int, param_mode2: int, param_mode3: int
) -> (list, int):
    """
    opcode 1 adds together numbers read from two positions and stores the result in a third position.
    returns updated memory and current position in memory
    """
    if param_mode1 == 0:
        param1 = memory[memory[position + 1]]
    else:
        param1 = memory[position + 1]
    if param_mode2 == 0:
        param2 = memory[memory[position + 2]]
    else:
        param2 = memory[position + 2]

    memory[memory[position + 3]] = param1 + param2

    return memory, position + 4


def opcode_2(
    memory: list, position: int, param_mode1: int, param_mode2: int, param_mode3: int
) -> (list, int):
    """
    opcode 2 multiplies together numbers and stores the result in a third position.
    returns updated memory and current position in memory
    """
    if param_mode1 == 0:
        param1 = memory[memory[position + 1]]
    else:
        param1 = memory[position + 1]
    if param_mode2 == 0:
        param2 = memory[memory[position + 2]]
    else:
        param2 = memory[position + 2]

    memory[memory[position + 3]] = param1 * param2

    return memory, position + 4


def opcode_3(
    memory: list,
    position: int,
) -> (list, int):
    """
    opcode 3 stores input to address in parameter ( next memory position ) and moves position forward 2
    """
    memory[memory[position + 1]] = 5
    # memory[memory[position + 1]] = 9
    return memory, position + 2


def opcode_4(
    memory: list, position: int, param_mode1: int,
) -> (list, int):
    """
    opcode 4 outputs value of parameter ( next memory position ) and moves memory pointer forward 2
    """
    if param_mode1 == 0:
        print(memory[memory[position + 1]])
    elif param_mode1 == 1:
        print(memory[position + 1])
    return memory, position + 2

def opcode_5(
    memory: list, position: int, param_mode1: int, param_mode2: int, param_mode3: int
) -> (list, int):
    """
    opcode 5 jump-if-true if the fist parameter is non-zero set memory pointer to value from the second parameter or do nothing
    returns updated memory and current position in memory
    """
    if param_mode1 == 0:
        param1 = memory[memory[position + 1]]
    else:
        param1 = memory[position + 1]
    if param_mode2 == 0:
        param2 = memory[memory[position + 2]]
    else:
        param2 = memory[position + 2]
    if param1 != 0:
        position = param2
    else:
        position = position + 3

    return memory, position

def opcode_6(
    memory: list, position: int, param_mode1: int, param_mode2: int, param_mode3: int
) -> (list, int):
    """
    opcode 6 jump-if-false if the fist parameter is zero set memory pointer to value from the second parameter or do nothing
    returns updated memory and current position in memory
    """
    if param_mode1 == 0:
        param1 = memory[memory[position + 1]]
    else:
        param1 = memory[position + 1]
    if param_mode2 == 0:
        param2 = memory[memory[position + 2]]
    else:
        param2 = memory[position + 2]
    if param1 == 0:
        position = param2
    else:
        position = position + 3

    return memory, position

def opcode_7(
    memory: list, position: int, param_mode1: int, param_mode2: int, param_mode3: int
) -> (list, int):
    """
    opcode 7 less than: if the first param is less than the second param store 1 in position of third param otherwise it stores 0
    returns updated memory and current position in memory
    """
    if param_mode1 == 0:
        param1 = memory[memory[position + 1]]
    else:
        param1 = memory[position + 1]
    if param_mode2 == 0:
        param2 = memory[memory[position + 2]]
    else:
        param2 = memory[position + 2]

    if param_mode3 == 0:
        if param1 < param2:
            memory[memory[position + 3]] = 1
        else:
            memory[memory[position + 3]] = 0

    else:
        if param1 < param2:
            memory[position + 3] = 1
        else:
            memory[position + 3] = 0

    return memory, position + 4


def opcode_8(
        memory: list, position: int, param_mode1: int, param_mode2: int, param_mode3: int
) -> (list, int):
    """
    opcode 8 equals: if the first param equals the second param store 1 in position of third param otherwise it stores 0
    returns updated memory and current position in memory
    """
    if param_mode1 == 0:
        param1 = memory[memory[position + 1]]
    else:
        param1 = memory[position + 1]
    if param_mode2 == 0:
        param2 = memory[memory[position + 2]]
    else:
        param2 = memory[position + 2]

    if param_mode3 == 0:
        if param1 == param2:
            memory[memory[position + 3]] = 1
        else:
            memory[memory[position + 3]] = 0

    else:
        if param1 == param2:
            memory[position + 3] = 1
        else:
            memory[position + 3] = 0

    return memory, position + 4


def parse_instructions(instructions: int) -> tuple:
    _instructions = list(str(instructions))

    if len(_instructions) == 2:
        opcode = int("".join(_instructions[-2:]))
        if opcode == 99:
            return 99, 0, 0, 0

    if len(_instructions) == 1:
        if _instructions[0] == '1':
            return 1, 0, 0, 0
        elif _instructions[0] == '2':
            return 2, 0, 0, 0
        elif _instructions[0] == '3':
            return 3, 0, 0, 0
        elif _instructions[0] == '4':
            return 4, 0, 0, 0
        elif _instructions[0] == '5':
            return 5, 0, 0, 0
        elif _instructions[0] == '6':
            return 6, 0, 0, 0
        elif _instructions[0] == '7':
            return 7, 0, 0, 0
        elif _instructions[0] == '8':
            return 8, 0, 0, 0

    if len(_instructions) == 3:
        opcode = int("".join(_instructions[-2:]))
        param_mode1 = int(_instructions[-3])
        param_mode2 = 0
        param_mode3 = 0
        return opcode, param_mode1, param_mode2, param_mode3

    if len(_instructions) == 4:
        opcode = int("".join(_instructions[-2:]))
        param_mode1 = int(_instructions[-3])
        param_mode2 = int(_instructions[-4])
        param_mode3 = 0
        return opcode, param_mode1, param_mode2, param_mode3

    if len(_instructions) == 5:
        opcode = int("".join(_instructions[-2:]))
        param_mode1 = int(_instructions[-3])
        param_mode2 = int(_instructions[-4])
        param_mode3 = int(_instructions[-5])
        return opcode, param_mode1, param_mode2, param_mode3

if __name__ == "__main__":
    with open("puzzle_input") as file:
        data = [int(v) for v in file.read().split(',')]
        computer(data)
