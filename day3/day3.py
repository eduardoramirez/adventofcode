INPUT = open('day3.txt','r').read().split('\n')
INPUT = filter(lambda xs: len(xs) > 0, INPUT)
INPUT = [[int(n) for n in line.split()] for line in INPUT]

def get_valid_triangles(triangles):
    valid_triangles = 0
    for triangle_sides in triangles:
        triangle_sides = sorted(triangle_sides)
        valid_triangles += 1 if (triangle_sides[0] + triangle_sides[1]) > triangle_sides[2] else 0

    return valid_triangles


def part1():
    return get_valid_triangles(INPUT)


def part2():
    triangles = []
    for i in range(0, len(INPUT) - 2, 3):
        row_1 = INPUT[i]
        row_2 = INPUT[i+1]
        row_3 = INPUT[i+2]

        triangles.append([row_1[0], row_2[0], row_3[0]])
        triangles.append([row_1[1], row_2[1], row_3[1]])
        triangles.append([row_1[2], row_2[2], row_3[2]])

    return get_valid_triangles(triangles)


if __name__ == '__main__':
    print 'Part 1: ' + str(part1())
    print 'Part 2: ' + str(part2())
