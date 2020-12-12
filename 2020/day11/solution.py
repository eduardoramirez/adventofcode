INPUT = open('input.txt', 'r').read().split('\n')
INPUT = list(filter(lambda l: l != '', INPUT))


def occupied_seats(taken_fn, taken_thres):
  seats = INPUT[:]

  while True:
    changed = False
    new_seats = []
    
    for i in range(len(seats)):
      new_row = ''
      for j in range(len(seats[i])):
        seat = seats[i][j]
        if seat == 'L' and taken_fn(seats, i, j) == 0:
          changed = True
          new_row += '#'
        elif seat == '#' and taken_fn(seats, i, j) >= taken_thres:
          changed = True
          new_row += 'L'
        else:
          new_row += seats[i][j]
      new_seats.append(new_row)
          
    if not changed:
      break
    seats = new_seats
  
  return ''.join(seats).count('#')


def part1():
  def taken_count(seats, r, c):
    cnt = 0
    for i in [1, 0, -1]:
      for j in [1, 0, -1]:
        t_r = r + i
        t_c = c + j
        if (r, c) != (t_r, t_c) and 0 <= t_r < len(seats) and 0 <= t_c < len(seats[t_r]) and seats[t_r][t_c] == '#':
          cnt += 1
    return cnt

  return occupied_seats(taken_count, 4)


def part2():
  def taken_count(seats, r, c):
    cnt = 0
    for r_fac in [1, 0, -1]:
      for c_fac in [1, 0, -1]:
        t_r = r + r_fac
        t_c = c + c_fac

        while (r, c) != (t_r, t_c) and 0 <= (t_r) < len(seats) and 0 <= (t_c) < len(seats[t_r]):
          if seats[t_r][t_c] == '#':
            cnt += 1
            break
          elif seats[t_r][t_c] == 'L':
            break
          t_r += r_fac
          t_c += c_fac

    return cnt

  return occupied_seats(taken_count, 5)


if __name__ == '__main__':
  print('Part 1: {}'.format(part1()))
  print('Part 2: {}'.format(part2()))
