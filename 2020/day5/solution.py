import math

INPUT = open('input.txt', 'r').read().split('\n')
entries = list(filter(lambda l: l != '', INPUT))


def get_seat_ids(): 
  ids = []

  for entry in entries:
    entry = entry.replace('F', '0')
    entry = entry.replace('B', '1')
    entry = entry.replace('L', '0')
    entry = entry.replace('R', '1')
    
    ids.append(int(entry, 2))

  return ids


def part1():
  return max(get_seat_ids())


def part2():
  ids = sorted(get_seat_ids())

  for i in range(1, len(ids)-1, 1):
    c = ids[i]
    if ids[i-1]+1 != c:
      return c - 1
    elif ids[i+1]-1 != c:
      return c + 1
  
  return -1


if __name__ == '__main__':
  print('Part 1: {}'.format(part1()))
  print('Part 2: {}'.format(part2()))
