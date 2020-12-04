INPUT = open('input.txt', 'r').read().split('\n')
lines = list(filter(lambda l: l != '', INPUT))


def find_trees(step_x, step_y):
  x = 0
  trees = 0
  
  for i in range(0, len(lines)-step_y, step_y):
    pattern = lines[i+step_y]
    x = (x+step_x) % len(pattern)

    trees += int(pattern[x] == '#')

  return trees


def part1():
  return find_trees(3, 1)


def part2():
  slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
  ]
  
  res = 1
  for [step_x, step_y] in slopes:
    res *= find_trees(step_x, step_y)

  return res


if __name__ == '__main__':
  print('Part 1: {}'.format(part1()))
  print('Part 2: {}'.format(part2()))
