INPUT = open('input.txt', 'r').read().split()
entries = list(map(lambda l: int(l), INPUT))
entries_set = set(entries)


def part1():
  want = 2020

  for entry in entries:
    need = want - entry
    if need > 0 and need in entries_set:
      return entry * need


def part2():
  want = 2020

  sorted_entries = sorted(entries)

  for i in range(len(sorted_entries)):
    lo = i + 1
    hi = len(sorted_entries) - 1

    while lo < hi:
      summ = sorted_entries[i] + sorted_entries[lo] + sorted_entries[hi]

      if summ == want:
        return sorted_entries[i] * sorted_entries[lo] * sorted_entries[hi]
      elif summ > want:
        hi -= 1
      else:
        lo += 1


if __name__ == '__main__':
  print('Part 1: {}'.format(part1()))
  print('Part 2: {}'.format(part2()))
