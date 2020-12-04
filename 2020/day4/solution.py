import re

INPUT = open('input.txt', 'r').read().split('\n')

passports = []
current_passport = None
for line in INPUT:
  if line == '':
    current_passport = None
  else:
    if current_passport is None:
      current_passport = {}
      passports.append(current_passport)
    for field in line.split(' '):
      [key, val] = field.split(':')
      current_passport[key] = val


def part1():
  required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

  valid = 0
  for passport in passports:
    fields = set(passport.keys())
    if 'cid' in fields:
      fields.remove('cid')

    valid += fields == required if 1 else 0

  return valid


def part2():
  required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

  valid = 0
  for passport in passports:
    fields = set(passport.keys())
    if 'cid' in fields:
      fields.remove('cid')

    def is_field_valid(f, v):
      if f == 'byr':
        return v.isnumeric() and 1920 <= int(v) <= 2002
      elif f == 'iyr':
        return v.isnumeric() and 2010 <= int(v) <= 2020
      elif f == 'eyr':
        return v.isnumeric() and 2020 <= int(v) <= 2030
      elif f == 'hgt':
        if v[-2:] == 'cm':
          return 150 <= int(v[0:-2]) <= 193
        elif v[-2:] == 'in':
          return 59 <= int(v[0:-2]) <= 76
      elif f == 'hcl':
        return re.match('^\#[0-9a-f]{6}$', v) if True else False
      elif f == 'ecl':
        return v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
      elif f == 'pid':
        return re.match('^\d{9}$', v) if True else False
      return False

    is_valid = fields == required and all(is_field_valid(f, passport[f]) for f in required) 
    
    valid += int(is_valid)

  return valid


if __name__ == '__main__':
  print('Part 1: {}'.format(part1()))
  print('Part 2: {}'.format(part2()))
