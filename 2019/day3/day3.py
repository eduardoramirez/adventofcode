import math

INPUT = open('input.txt', 'r').read().split()
wire_directions = list(map(lambda l: l.split(','), INPUT))

def create_points(directions):
    all_points = [(0, 0)]

    for d in directions:
        steps = int(d[1:])
        (x, y) = all_points[-1]
        if d.startswith('R'):
            points = [(step_x, y) for step_x in range(x+1, x+steps+1)]
            all_points += points
        elif d.startswith('U'):
            points = [(x, step_y) for step_y in range(y+1, y+steps+1)]
            all_points += points
        elif d.startswith('L'):
            points = [(step_x, y) for step_x in range(x-1, x-(steps+1), -1)]
            all_points += points
        elif d.startswith('D'):
            points = [(x, step_y) for step_y in range(y-1, y-(steps+1), -1)]
            all_points += points
        else:
            raise Exception('Unknown direction {}'.format(d))

    return all_points[1:]


def manhattan_dist(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def part1():
    root = (0, 0)

    wire_1 = set(create_points(wire_directions[0]))
    wire_2 = set(create_points(wire_directions[1]))

    intersections = list(wire_1.intersection(wire_2))

    return min([manhattan_dist(root, p) for p in intersections])


def part2():
    wire_1_points = create_points(wire_directions[0])
    wire_2_points = create_points(wire_directions[1])

    # Create the mapping in reverse so we keep the shortest path
    wire_1_idx = {wire_1_points[i]:i for i in range(len(wire_1_points)-1, -1, -1)}
    wire_2_idx = {wire_2_points[i]:i for i in range(len(wire_2_points)-1, -1, -1)}

    intersections = list(set(wire_1_points).intersection(set(wire_2_points)))

    # 2 is to account for omitted roots
    return min([2 + wire_1_idx[itx] + wire_2_idx[itx] for itx in intersections])


if __name__ == '__main__':
    print('Part 1: {}'.format(part1()))
    print('Part 2: {}'.format(part2()))
