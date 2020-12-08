INPUT = open('input.txt', 'r').read().split('\n')
INPUT = list(filter(lambda l: l != '', INPUT))


def eval(cmds):
    seen = set()

    i = 0
    acc = 0

    while True:
      if i == len(cmds):
        return (acc, True)
        
      if i > len(cmds) or i < 0:
        return (acc, False)
      
      if i in seen:
        return (acc, False)

      seen.add(i)

      [cmd, val] = cmds[i].split(' ')
      if cmd == 'nop':
        i += 1
      elif cmd == 'acc':
        acc += int(val)
        i += 1
      elif cmd == 'jmp':
        i += int(val)
    
    return (acc, True)


def part1():
  (acc, _) = eval(INPUT)
  return acc


def part2():  
  for i in range(len(INPUT)):
    cmds = INPUT[:]

    [cmd, val] = cmds[i].split(' ')
    if cmd == 'nop':
      cmds[i] = 'jmp ' + val
    elif cmd == 'jmp':
      cmds[i] = 'nop ' + val
    
    (t_acc, t_success) = eval(cmds)
    if t_success:
      return t_acc


if __name__ == '__main__':
  print('Part 1: {}'.format(part1()))
  print('Part 2: {}'.format(part2()))
