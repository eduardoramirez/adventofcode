from itertools import permutations
from collections import deque

INPUT = open('input.txt', 'r').read().split(',')
program = list(map(lambda l: int(l), INPUT))

HALT = 99
ADD  = 1
MULT = 2
SAVE = 3
PRINT = 4
JUMP_TRUE = 5
JUMP_FALSE = 6
LT = 7
EQ = 8


def run(memory):
    input_cnt = 0

    ptr = 0
    while memory[ptr] != HALT:
        instr = str(memory[ptr])
        for i in range(0, 5-len(instr)):
            instr = '0' + instr

        opcode = int(instr[-2:])
        param_modes = list(reversed([int(n) for n in instr[:3]]))

        deref = lambda i: memory[ptr+i]
        param = lambda i: memory[deref(i)] if param_modes[i-1] == 0 else deref(i)

        if opcode == ADD:
            memory[deref(3)] = param(1) + param(2)
            ptr += 4
        elif opcode == MULT:
            memory[deref(3)] = param(1) * param(2)
            ptr += 4
        elif opcode == SAVE:
            inputVal = yield
            memory[deref(1)] = inputVal
            input_cnt += 1
            ptr += 2
        elif opcode == PRINT:
            yield param(1)
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


class Pipeline:
    def __init__(self):
        self.amps = deque()

    def add_amp(self, phase):
        amp_gen = run(program[:])
        self.amps.append(amp_gen)

        next(amp_gen)
        amp_gen.send(phase)

    def run(self, start_val):
        next_input = start_val
        while self.amps:
            try:
                active_amp = self.amps[0]
                # the amp should be in a pending state
                next_input = active_amp.send(next_input)
                # advance the amp to its next pending state
                next(active_amp)
                self.amps.rotate(-1)
            except StopIteration:
                self.amps.popleft()
        return next_input


def calc_max_thruster(settings):
    perms = list(permutations(settings))

    signals = []
    for perm in perms:
        pipeline = Pipeline()
        for phase in perm:
            pipeline.add_amp(phase)

        signal = pipeline.run(start_val=0)
        signals.append(signal)

    return max(signals)


if __name__ == '__main__':
    p1_val = calc_max_thruster([0, 1, 2, 3, 4])
    print('Part 1: {}'.format(p1_val))
    p2_val = calc_max_thruster([5, 6, 7, 8, 9])
    print('Part 2: {}'.format(p2_val))
