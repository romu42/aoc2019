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
                memory, position
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
    opcode 3 stores input to address in parameter
    """
    memory[memory[position + 1]] = 1
    return memory, position + 2


def opcode_4(
    memory: list, position: int
) -> (list, int):
    """
    opcode 4 outputs value of parameter
    """
    print(memory[memory[position + 1]])
    return memory, position + 2

def parse_instructions(instructions: int) -> tuple:
    _instructions = list(str(instructions))
    if len(_instructions) == 2:
        opcode = int("".join(_instructions[-2:]))
        if opcode == 99:
            return 99, 0, 0, 0
    if len(_instructions) == 1:
        if _instructions[0] == '3':
            return 3, 0, 0, 0
        elif _instructions[0] == '4':
            return 4, 0, 0, 0
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
        data = file.read().split(',')
        print(computer(data))
    # memory = [1002, 4, 3, 4, 33]
    # position1 = 0
    # opcode, param_mode1, param_mode2, param_mode3 = parse_instructions(memory[position1])
    # print(opcode, param_mode1, param_mode2, param_mode3)
    # memory = [3, 0, 4, 0, 99]
    # print(computer(memory))
