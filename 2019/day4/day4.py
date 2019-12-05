import math

INPUT = '256310-732736'
ranges = INPUT.split('-')


def is_valid_pass(pw, exact_match=False):
    digits = [int(n) for n in str(pw)]

    for i in range(1, len(digits)):
        if digits[i] < digits[i-1]:
            return False

    for d in digits:
        if exact_match:
            if digits.count(d) == 2:
                return True
        else:
            if digits.count(d) > 1:
                return True

    return False


def get_valid_passwords(exact_match=False):
    lo = int(ranges[0])
    hi = int(ranges[1])

    passwords = 0
    while lo <= hi:
        if is_valid_pass(lo, exact_match):
            passwords += 1
        lo += 1

    return passwords


def part1():
    return get_valid_passwords()


def part2():
    return get_valid_passwords(exact_match=True)


if __name__ == '__main__':
    print('Part 1: {}'.format(part1()))
    print('Part 2: {}'.format(part2()))
