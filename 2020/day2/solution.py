INPUT = open('input.txt', 'r').read().split('\n')

entries = filter(lambda l: l != '', INPUT)
entries = list(map(lambda l: l.split(':'), entries))


def get_policy_and_password(entry):
  [policy, password] = entry

  [count, letter] = policy.split(' ')
  [min, max] = count.split('-')

  return ((int(min), int(max), letter), password.strip())

def part1():
  valid = 0
  for entry in entries:
    ((min, max, letter), password) = get_policy_and_password(entry)

    letter_cnt = 0
    for l in password:
      if l == letter:
        letter_cnt += 1

    if letter_cnt >= min and letter_cnt <= max:
      valid += 1

  return valid


def part2():
  valid = 0
  for entry in entries:
    ((pos_one, pos_two, letter), password) = get_policy_and_password(entry)

    letters = set([password[pos_one-1], password[pos_two-1]])
    if letter in letters and len(letters) == 2:
      valid += 1

  return valid


if __name__ == '__main__':
  print('Part 1: {}'.format(part1()))
  print('Part 2: {}'.format(part2()))
