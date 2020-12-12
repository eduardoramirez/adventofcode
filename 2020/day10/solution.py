INPUT = open('input.txt', 'r').read().split('\n')
INPUT = filter(lambda l: l != '', INPUT)
INPUT = list(map(lambda l: int(l), INPUT))


def part1():
  jolts = sorted(INPUT)

  diffs = [0, 0, 1]
  last_jolt = 0
  i = 0 
  while i < len(jolts):
    while (jolts[i] - last_jolt) > 3:
      i += 1

    diff = jolts[i] - last_jolt
    diffs[diff - 1] += 1

    last_jolt = jolts[i]
    i += 1

  return diffs[0] * diffs[2]


def part2():
  pass


if __name__ == '__main__':
  print('Part 1: {}'.format(part1()))
  print('Part 2: {}'.format(part2()))
