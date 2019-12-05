
from itertools import product


def computer(memory: list) -> (list, int):
    position = 0
    end = len(memory)

    while position < end:
        if memory[position] == 99:
            return memory
        elif memory[position] == 1:
            memory, position = opcode_1(memory, position)
        elif memory[position] == 2:
            memory, position = opcode_2(memory, position)
        elif memory[position] == 3:
            memory, position = opcode_3(memory, position)
        elif memory[position] == 4:
            memory, position = opcode_4(memory, position)

    return memory

def opcode_1(memory: list, position: int) -> (list, int):
    """
    opcode 1 adds together numbers read from two positions and stores the result in a third position.
    returns updated memory and current position in memory
    """
    memory[memory[position + 3]] = memory[memory[position + 1]] + memory[memory[position +2]]
    return memory, position + 4


def opcode_2(memory: list, position: int) -> (list, int):
    """
    opcode 2 multiplies together numbers read from two positions and stores the result in a third position.
    returns updated memory and current position in memory
    """
    memory[memory[position + 3]] = memory[memory[position + 1]] * memory[memory[position +2]]
    return memory, position + 4


def opcode_3(memory: list, position: int) -> (list, int):
    """
    opcode 3
    """
    # stoplen = 3
    pass


def opcode_4(memory: list, position: int) -> (list, int):
    """
    opcode 4
    """
    # stoplen = 3
    pass

def find_noun_verb(initial_state: list) -> list:
    for noun, verb in product(range(100), range(100)):
        input = [x for x in initial_state]
        input[1] = noun
        input[2] = verb
        output = fix_computer(input)
        if output[0] == 19690720:
            return output[0], output[1], output[2], 100 * output[1] + output[2]

if __name__ == "__main__":
    with open("puzzle_input") as file:
        data = file.read().split(',')
        print(data)
    #     print(fix_computer(data))

