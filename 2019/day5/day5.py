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


def run(memory):
    ptr = 0
    while memory[ptr] != HALT:
        instr = str(memory[ptr])
        for i in range(0, 5-len(instr)):
            instr = '0' + instr

        opcode = int(instr[-2:])
        param_modes = reverse([int(n) for n in instr[:3]])

        deref = lambda i: memory[ptr+i]
        param = lambda i: memory[deref(i)] if param_modes[i-1] == 0 else deref(i)

        if opcode == ADD:
            memory[deref(3)] = param(1) + param(2)
            ptr += 4
        elif opcode == MULT:
            memory[deref(3)] = param(1) * param(2)
            ptr += 4
        elif opcode == SAVE:
            memory[deref(1)] = int(input('Input: '))
            ptr += 2
        elif opcode == PRINT:
            print('Output: {}'.format(param(1)))
            ptr += 2
        elif opcode == JUMP_TRUE:
            if param(1) != 0:
                ptr = param(2)
            else:
                ptr += 3
        elif opcode == JUMP_FALSE:
            if param(1) == 0:
                ptr = param(2)
            else:
                ptr += 3
        elif opcode == LT:
            if param(1) < param(2):
                memory[deref(3)] = 1
            else:
                memory[deref(3)] = 0
            ptr += 4
        elif opcode == EQ:
            if param(1) == param(2):
                memory[deref(3)] = 1
            else:
                memory[deref(3)] = 0
            ptr += 4
        else:
            raise Exception('UNKOWN OPCODE: {}'.format(opcode))


if __name__ == '__main__':
    print('Part 1:')
    run(initial_memory[:])
    print('Part 2:')
    run(initial_memory[:])
