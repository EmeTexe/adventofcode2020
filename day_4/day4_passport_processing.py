"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""


def is_valid(item: []):
    key = item[0]
    value = item[1]
    if key == 'byr':
        return 1920 <= int(value) <= 2002
    elif key == 'iyr':
        return 2010 <= int(value) <= 2020
    elif key == 'eyr':
        return 2020 <= int(value) <= 2030
    elif key == 'hgt':
        if value[-2:] == 'cm':
            return 150 <= int(value[:-2]) <= 193
        elif value[-2:] == 'in':
            return 59 <= int(value[:-2]) <= 76
    elif key == 'hcl':
        return value[0] == '#' and all(elem in '0123456789abcdef' for elem in value[1:]) and len(value[1:]) == 6
    elif key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == 'pid':
        try:
            return type(int(value)) == int and len(value) == 9
        except:
            return False
    else:
        return False


valid_fields = sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
current_fields = []
nb_valid = 0
n = 0
with open('day4_passport_processing.txt') as f:
    for line in f:
        n += 1
        if line == '\n':
            print('on y passe')
            print(sorted(current_fields))
            print(n)

            # if sorted(current_fields) == valid_fields:
            if all(elem in current_fields for elem in valid_fields):
                nb_valid += 1
            current_fields = []
        else:
            parsed_line = line.replace('\n', '').split(' ')
            for i in parsed_line:
                parsed_i = i.split(':')
                if is_valid(parsed_i):
                    current_fields.append(parsed_i[0])

print(nb_valid)
