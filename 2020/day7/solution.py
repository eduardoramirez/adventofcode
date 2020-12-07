import re

INPUT = open('input.txt', 'r').read().split('\n')
INPUT = list(filter(lambda l: l != '', INPUT))

# color -> [(color, count)]
bag_map = {}
for line in INPUT:
  bag_color_re = re.match(r'(.+) bags contain (.+)', line)
  bag_color = bag_color_re.group(1)
  bag_map[bag_color] = []

  nested = re.findall(r'(\d+) (.+?) bags?[,.]', bag_color_re.group(2))
  for (count, color) in nested:
    bag_map[bag_color].append((color, int(count)))


def part1():
  in_set = set()
  def color_in(color):
    for bag_color, nested in bag_map.items():
      for (nested_color, _) in nested:
        if color == nested_color:
          in_set.add(bag_color) 
          color_in(bag_color)

  color_in('shiny gold')

  return len(in_set)


def part2():
  def bags_required(color):
    bags_count = 0
    for (color, count) in bag_map[color]:
      bags_count += count + (count * bags_required(color))
    return bags_count

  return bags_required('shiny gold')


if __name__ == '__main__':
  print('Part 1: {}'.format(part1()))
  print('Part 2: {}'.format(part2()))
