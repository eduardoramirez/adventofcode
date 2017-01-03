INPUT = open('day2.txt','r').read().split('\n')
INPUT = filter(lambda xs: len(xs) > 0, INPUT)

KEYPAD = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

KEYPAD_2 = [
    ['-', '-', '1', '-', '-'],
    ['-', '2', '3', '4', '-'],
    ['5', '6', '7', '8', '9'],
    ['-', 'A', 'B', 'C', '-'],
    ['-', '-', 'D', '-', '-'],
]


def move(current_loc, move):
    (r, c) = current_loc

    if move == 'U' and (r - 1) >= 0:
        r = r - 1
    elif move == 'R' and (c + 1) <= 2:
        c = c + 1
    elif move == 'D' and (r + 1) <= 2:
        r = r + 1
    elif move == 'L' and (c - 1) >= 0:
        c = c - 1

    return (r, c)


def move2(current_loc, move):
    (r, c) = current_loc

    if move == 'U' and (r - 1) >= 0:
        r = r - 1 if KEYPAD_2[r - 1][c] != '-' else r
    elif move == 'R' and (c + 1) <= 4:
        c = c + 1 if KEYPAD_2[r][c + 1] != '-' else c
    elif move == 'D' and (r + 1) <= 4:
        r = r + 1 if KEYPAD_2[r + 1][c] != '-' else r
    elif move == 'L' and (c - 1) >= 0:
        c = c - 1 if KEYPAD_2[r][c - 1] != '-' else c

    return (r, c)


def convert_to_code_number(pad, location):
    (r, c) = location
    return pad[r][c]


def get_bathroom_code(location, move_fn, pad):
    bathroom_code = ''

    for instructions in INPUT:
        for instruction in instructions:
            location = move_fn(location, instruction)
        code_number = convert_to_code_number(pad, location)
        bathroom_code += str(code_number)

    return bathroom_code


def part1():
    return get_bathroom_code((1, 1), move, KEYPAD)


def part2():
    return get_bathroom_code((2, 0), move2, KEYPAD_2)


if __name__ == '__main__':
    print 'Part 1: ' + str(part1())
    print 'Part 2: ' + str(part2())
