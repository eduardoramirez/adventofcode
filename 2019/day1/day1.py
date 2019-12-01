import math

INPUT = open('day1.txt', 'r').read().split()
masses = list(map(lambda l: int(l), INPUT))

def fuel(mass):
    return math.floor(mass / 3) - 2


def fuel_accounted(mass):
    total_fuel = 0
    fuel_ = fuel(mass)
    while fuel_ > 0:
        total_fuel += fuel_
        fuel_ = fuel(fuel_)
    return total_fuel


def part1():
    return sum(map(lambda m: fuel(m), masses))


def part2():
    return sum(map(lambda m: fuel_accounted(m), masses))


if __name__ == '__main__':
    print('Part 1: {}'.format(part1()))
    print('Part 2: {}'.format(part2()))
