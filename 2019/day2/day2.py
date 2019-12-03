import copy

INPUT = open('input.txt', 'r').read().split(',')
initial_program = list(map(lambda l: int(l), INPUT))

HALT = 99
STEP = 4
ADD  = 1
MULT = 2

def run(program, current_pos=0):
    retrieve_var = lambda pos: program[program[pos]]

    while program[current_pos] != HALT:
        result = None

        opcode = program[current_pos]
        var1 = retrieve_var(current_pos + 1)
        var2 = retrieve_var(current_pos + 2)
        store_pos = program[current_pos + 3]

        if opcode == ADD:
            result = var1 + var2
        elif opcode == MULT:
            result = var1 * var2
        else:
            raise Exception('UNKOWN OPCODE: {}'.format(opcode))

        # store result
        program[store_pos] = result

        # advance the program
        current_pos += STEP


def part1():
    program = copy.deepcopy(initial_program)
    program[1] = 12
    program[2] = 2
    run(program)
    return program[0]


def part2():
    desired = 19690720

    for noun in range(0, 100):
        for verb in range(0, 100):
            program = copy.deepcopy(initial_program)

            program[1] = noun
            program[2] = verb

            run(program)

            if program[0] == desired:
                return 100 * noun + verb

if __name__ == '__main__':
    print('Part 1: {}'.format(part1()))
    print('Part 2: {}'.format(part2()))
