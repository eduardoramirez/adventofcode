INPUT = open('input.txt', 'r').read().split('\n')
INPUT = list(filter(lambda l: l != '', INPUT))
INPUT = list(map(lambda l: [l[0], int(l[1:])], INPUT))

#         (north: 0)
#             |
# (west: 3) --|-- (east: 1)
#             |
#         (south: 2)

def part1():
  direction = 1
  directions = ['N', 'E', 'S', 'W']
  # x, y
  ship = (0, 0)

  def move(p, action, val):
    (x, y) = p
    if action == 'N':
      return (x, y+val)
    elif action == 'S':
      return (x, y-val)
    elif action == 'E':
      return (x+val, y)
    elif action == 'W':
      return (x-val, y)

  for [action, val] in INPUT:
    if action == 'L':
      direction = int(((direction % 4) - (val / 90)) % 4)
    elif action == 'R':
      direction = int((direction + (val / 90)) % 4)
    elif action == 'F':
      ship = move(ship, directions[direction], val)
    else:
      ship = move(ship, action, val)
  
  return abs(ship[0]) + abs(ship[1])


def part2():
  # x, y
  ship = (0, 0)
  wp = (10, 1)

  def move(p, action, val):
    (x, y) = p
    if action == 'N':
      return (x, y+val)
    elif action == 'S':
      return (x, y-val)
    elif action == 'E':
      return (x+val, y)
    elif action == 'W':
      return (x-val, y)
  
  def rotate(p, angle, direction):
    (x, y) = p
    if (angle, direction) in [(90, 1), (270, -1)]:
      return (y, -x)
    elif (angle, direction) in [(180, 1), (180, -1)]:
      return (-x, -y)
    elif (angle, direction) in [(270, 1), (90, -1)]:
      return (-y, x)
    elif angle == 360:
      return (x, y)

  for [action, val] in INPUT:
    if action == 'L':
      wp = rotate(wp, val, -1)
    elif action == 'R':
      wp = rotate(wp, val, 1)
    elif action == 'F':
      ship = (ship[0]+(wp[0]*val), ship[1]+(wp[1]*val))
    else:
      wp = move(wp, action, val)
  
  return abs(ship[0]) + abs(ship[1])


if __name__ == '__main__':
  print('Part 1: {}'.format(part1()))
  print('Part 2: {}'.format(part2()))
