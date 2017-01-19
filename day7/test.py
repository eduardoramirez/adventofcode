import re

INPUT = open('day7.txt','r').read().split('\n')
INPUT = filter(lambda xs: len(xs) > 0, INPUT)


def get_abba(strings):
    matched = []
    for s in strings:
        for i in range(0, len(s) - 3):
            if s[i:i + 4] == s[i:i + 4][::-1] and s[i] != s[i + 1]:
                matched.append(s[i:i + 4])

    return matched


def get_aba(strings):
    matched = []
    for s in strings:
        for i in range(0, len(s) - 2):
            if s[i:i + 3] == s[i:i + 3][::-1] and s[i] != s[i + 1]:
                matched.append(s[i:i + 3])

    return matched


def part1():
    tls_count = 0

    for ip in INPUT:
        supernets = re.sub(r'\[.+?\]', ' ', ip).split()
        hypernets = [match[1:-1] for match in re.findall(r'\[.+?\]', ip)]

        if get_abba(supernets) > 0 and get_abba(hypernets) == 0:
            tls_count += 1

    return tls_count


def part2():
    sls_count = 0

    for ip in INPUT:
        supernets = re.sub(r'\[.+?\]', ' ', ip).split()
        hypernets = [match[1:-1] for match in re.findall(r'\[.+?\]', ip)]

        abas = set(get_aba(supernets))
        babs = set(get_aba(hypernets))

        for aba in abas:
            bab = aba[1] + aba[0] + aba[1]
            if bab in babs:
                sls_count += 1
                break

    return sls_count


if __name__ == '__main__':
    print 'Part 1: ' + str(part1())
    print 'Part 2: ' + str(part2())
