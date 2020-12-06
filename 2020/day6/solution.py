import re

INPUT = re.split(r'(\n\n|\n$)', open('input.txt', 'r').read())

def part1():
  return sum([len(set(g.replace('\n', ''))) for g in INPUT])


def part2():
  groups = [answers.split('\n') for answers in INPUT]

  res = 0
  for g in groups:
    gs = [set(m) for m in g]
    res += len(set.intersection(*gs))
  return res
  

if __name__ == '__main__':
  print('Part 1: {}'.format(part1()))
  print('Part 2: {}'.format(part2()))
