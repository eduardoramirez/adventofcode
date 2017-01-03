from operator import itemgetter
import md5

INPUT = open('day5.txt','r').read().split('\n')[0]


def get_hash_hex(text):
    md5_hash = md5.new(text)
    return md5_hash.hexdigest()


def part1(prefix, length):
    index = 0
    password = ''

    while True:
        hex_rep = get_hash_hex(INPUT + str(index))

        if hex_rep.startswith(prefix):
            password += hex_rep[len(prefix)]

        if len(password) == length:
            break

        index += 1

    return password


def part2(prefix, length):
    index = 0
    password = []
    positions = []

    while True:
        hex_rep = get_hash_hex(INPUT + str(index))

        if hex_rep.startswith(prefix):
            position = hex_rep[len(prefix)]
            decrypted_char = hex_rep[len(prefix) + 1]

            if position.isdigit():
                position = int(position)
                if position < length and not position in positions:
                    password.append((position, decrypted_char))
                    positions.append(position)

        if len(password) == length:
            break

        index += 1

    password = sorted(password, key=itemgetter(0))
    password_letter_list = [letter for (position, letter) in password]
    return ''.join(password_letter_list)


if __name__ == '__main__':
    prefix = '00000'
    length = 8

    print 'Part 1: ' + str(part1(prefix, length))
    print 'Part 2: ' + str(part2(prefix, length))
