from operator import itemgetter

INPUT = open('day6.txt','r').read().split('\n')
INPUT = filter(lambda xs: len(xs) > 0, INPUT)


def get_correct_message(descending=True):
    message_length = len(INPUT[0])
    messages = [[line[i] for line in INPUT] for i in range(message_length)]

    corrected_message = ''

    for message in messages:
        letters = [(letter, message.count(letter)) for letter in set(message)]
        letters = sorted(letters, key=itemgetter(1), reverse=descending)
        corrected_message += letters[0][0]

    return corrected_message

def part1():
    return get_correct_message()


def part2():
    return get_correct_message(False)


if __name__ == '__main__':
    print 'Part 1: ' + str(part1())
    print 'Part 2: ' + str(part2())
