INPUT = open('input.txt', 'r').read().split(',')
initial_memory = list(map(lambda l: int(l), INPUT))

HALT = 99
ADD  = 1
MULT = 2
SAVE = 3
PRINT = 4
JUMP_TRUE = 5
JUMP_FALSE = 6
LT = 7
EQ = 8

def reverse(ls):
    return ls[::-1]


def run(memory, part2=False):
    ptr = 0
    while memory[ptr] != HALT:
        instr = str(memory[ptr])
        for i in range(0, 5-len(instr)):
            instr = '0' + instr

        opcode = int(instr[-2:])
        param_modes = reverse([int(n) for n in instr[:3]])

        param = lambda p, i: memory[memory[p+i]] if param_modes[i-1] == 0 else memory[p+i]

        if opcode == ADD:
            memory[memory[ptr+3]] = param(ptr, 1) + param(ptr, 2)
            ptr += 4
        elif opcode == MULT:
            memory[memory[ptr+3]] = param(ptr, 1) * param(ptr, 2)
            ptr += 4
        elif opcode == SAVE:
            memory[memory[ptr+1]] = int(input('Input: '))
            ptr += 2
        elif opcode == PRINT:
            print('Output: {}'.format(param(ptr, 1)))
            ptr += 2
        elif part2 and opcode == JUMP_TRUE:
            if param(ptr, 1) != 0:
                ptr = param(ptr, 2)
            else:
                ptr += 3
        elif part2 and opcode == JUMP_FALSE:
            if param(ptr, 1) == 0:
                ptr = param(ptr, 2)
            else:
                ptr += 3
        elif part2 and opcode == LT:
            if param(ptr, 1) < param(ptr, 2):
                memory[memory[ptr+3]] = 1
            else:
                memory[memory[ptr+3]] = 0
            ptr += 4
        elif part2 and opcode == EQ:
            if param(ptr, 1) == param(ptr, 2):
                memory[memory[ptr+3]] = 1
            else:
                memory[memory[ptr+3]] = 0
            ptr += 4
        else:
            raise Exception('UNKOWN OPCODE: {}'.format(opcode))


def part1():
    run(initial_memory[:])


def part2():
    run(initial_memory[:], part2=True)


if __name__ == '__main__':
    print('Part 1:')
    part1()
    print('Part 2:')
    part2()
