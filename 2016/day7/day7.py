import re

INPUT = open('day7.txt','r').read().split('\n')
INPUT = filter(lambda xs: len(xs) > 0, INPUT)


def get_by_pattern(strings, pattern):
    length = 4 if pattern == 'abba' else 3
    matched = []
    for s in strings:
        for i in range(0, len(s) - (length - 1)):
            if s[i:i + length] == s[i:i + length][::-1] and s[i] != s[i + 1]:
                matched.append(s[i:i + length])

    return matched


def part1():
    is_abba = lambda x: len(get_by_pattern(x, 'abba')) > 0

    tls_count = 0

    for ip in INPUT:
        supernets = re.sub(r'\[.+?\]', ' ', ip).split()
        hypernets = [match[1:-1] for match in re.findall(r'\[.+?\]', ip)]

        if is_abba(supernets) and not is_abba(hypernets):
            tls_count += 1

    return tls_count


def part2():
    sls_count = 0

    for ip in INPUT:
        supernets = re.sub(r'\[.+?\]', ' ', ip).split()
        hypernets = [match[1:-1] for match in re.findall(r'\[.+?\]', ip)]

        abas = set(get_by_pattern(supernets, 'aba'))
        babs = set(get_by_pattern(hypernets, 'aba'))

        for aba in abas:
            bab = aba[1] + aba[0] + aba[1]
            if bab in babs:
                sls_count += 1
                break

    return sls_count


if __name__ == '__main__':
    print 'Part 1: ' + str(part1())
    print 'Part 2: ' + str(part2())
