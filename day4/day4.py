import re

INPUT = open('day4.txt','r').read().split('\n')
INPUT = filter(lambda xs: len(xs) > 0, INPUT)


def get_valid_rooms():
    rooms = []
    for room in INPUT:
        m = re.search('((\w+-)+)(\d+)\[(\w+)\]', room)
        name = m.group(1)
        sectorId = int(m.group(3))
        checksum = list(m.group(4))

        letters = [(letter, name.count(letter)) for letter in set(name) if letter != '-']

        compare = lambda (x, count_x),(y, count_y): count_x - count_y if count_x - count_y != 0 else ord(y) - ord(x)
        sorted_letters = sorted(letters, cmp=compare, reverse=True)
        calculated_checksum = [letter for (letter, count) in sorted_letters]

        if calculated_checksum[:len(checksum)] == checksum:
            rooms.append((name, sectorId))

    return rooms


def part1():
    return sum([sectorId for (name, sectorId) in get_valid_rooms()])


def part2():
    offset = 97
    alphabet_size = 26
    needle = 'northpole object storage '

    for (name, sectorId) in get_valid_rooms():
        decrypted_name = ''
        for letter in name:
            if letter == '-':
                decrypted_name += ' '
                continue

            shift = (ord(letter) - offset + sectorId) % alphabet_size
            decrypted_letter = chr(shift + offset)
            decrypted_name += decrypted_letter

        if needle == decrypted_name:
            return sectorId


if __name__ == '__main__':
    print 'Part 1: ' + str(part1())
    print 'Part 2: ' + str(part2())
