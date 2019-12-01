'''
Orientations
    0 = West
    1 = North
    2 = East
    3 = South

Directions
    L = -1
    R = 1
'''

INPUT = open('day1.txt','r').read().split(', ')

def get_instructions():
    instructions = [-1 if instruction[0] == 'L' else 1 for instruction in INPUT]

    instructions_tuples = []
    for i in range(len(instructions)):
        orientation = sum(instructions[0:i+1]) % 4

        length = int(INPUT[i][1:])
        adjusted_length = -length if orientation in [0, 3] else length

        instructions_tuples.append((orientation, adjusted_length))

    return instructions_tuples


def part1():
    x = 0
    y = 0

    for (orientation, length) in get_instructions():
        if orientation in [0, 2]:
            x += length
        else:
            y += length

    return abs(x) + abs(y)


def part2():
    previously_visited = (0, 0)
    visited_map = {}
    double_whammy = None

    visited_map[(0, 0)] = True

    for (orientation, length) in get_instructions():
        steps = range(length, 0)[::-1] if orientation in [0, 3] else range(1, length + 1)
        (previous_x, previous_y) = previously_visited

        for s in steps:
            visited_point = (previous_x + s, previous_y) if orientation in [0, 2] else (previous_x, previous_y + s)
            previously_visited = visited_point

            if visited_point in visited_map:
                double_whammy = visited_point
                break
            visited_map[visited_point] = True

        if double_whammy:
            break

    (x, y) = double_whammy
    return abs(x) + abs(y)


if __name__ == '__main__':
    print 'Part 1: ' + str(part1())
    print 'Part 2: ' + str(part2())
