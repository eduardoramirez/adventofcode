import copy

INPUT = open('input.txt', 'r').read().split(',')
initial_memory = list(map(lambda l: int(l), INPUT))

HALT = 99
STEP = 4
ADD  = 1
MULT = 2


def run(memory, noun, verb):
    memory[1] = noun
    memory[2] = verb

    ptr = 0
    while memory[ptr] != HALT:
        opcode = memory[ptr]
        param1_ptr = memory[ptr + 1]
        param2_ptr = memory[ptr + 2]
        store_ptr = memory[ptr + 3]

        if opcode == ADD:
            memory[store_ptr] = memory[param1_ptr] + memory[param2_ptr]
        elif opcode == MULT:
            memory[store_ptr] = memory[param1_ptr] * memory[param2_ptr]
        else:
            raise Exception('UNKOWN OPCODE: {}'.format(opcode))

        # advance the program
        ptr += STEP

    return memory[0]


def part1():
    memory = copy.deepcopy(initial_memory)
    return run(memory, noun=12, verb=2)


def part2():
    desired = 19690720

    for noun in range(0, 100):
        for verb in range(0, 100):
            memory = copy.deepcopy(initial_memory)
            res = run(memory, noun, verb)

            if res == desired:
                return 100 * noun + verb


if __name__ == '__main__':
    print('Part 1: {}'.format(part1()))
    print('Part 2: {}'.format(part2()))
