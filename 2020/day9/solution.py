import math

INPUT = open('input.txt', 'r').read().split('\n')
INPUT = filter(lambda l: l != '', INPUT)
INPUT = list(map(lambda l: int(l), INPUT))


def part1():
  preamble_size = 25

  s = set(INPUT[:preamble_size])

  for i in range(preamble_size, len(INPUT)):
    el = INPUT[i]

    sum_found = False
    for s_el in s:
      if abs(el - s_el) in s:
        sum_found = True
        break
    
    if not sum_found:
      return el

    s.remove(INPUT[i-preamble_size])
    s.add(el)

  return -1


def part2():
  target = 14360655

  nums = [INPUT[0]]
  s = nums[0]

  for el in INPUT[1:]:
    s += el
    nums.append(el)

    while s >= target:
      if s == target:
        nums = sorted(nums)
        return nums[0] + nums[-1]
      s -= nums.pop(0)
 
  return -1


if __name__ == '__main__':
  print('Part 1: {}'.format(part1()))
  print('Part 2: {}'.format(part2()))
