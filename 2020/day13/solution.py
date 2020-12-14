import math

INPUT = open('input.txt', 'r').read().split('\n')
INPUT = list(filter(lambda l: l != '', INPUT))


def part1():
  earliest = int(INPUT[0])
  times = INPUT[1].split(',')

  shortest = math.inf
  shortestId = -1
  for t in times:
    if t == 'x':
      continue
    t = int(t)
    if math.ceil(earliest/t)*t < shortest:
      shortest = math.ceil(earliest/t)*t
      shortestId = t
  return (shortest-earliest) * shortestId


def part2():
  times = INPUT[1].split(',')

  earliest = 0
  prev = int(times[0])
  for i, t in enumerate(times[1:], start=1):
    if t == 'x':
      continue
    t = int(t)
    while (earliest + i) % t != 0:
      earliest += prev
    prev *= t
  return earliest


if __name__ == '__main__':
  print('Part 1: {}'.format(part1()))
  print('Part 2: {}'.format(part2()))
