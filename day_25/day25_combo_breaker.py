# part 1
divider = 20201227
sub_n = 7

with open('day25_combo_breaker.txt', 'r') as f:
    lines = f.readlines()
    card_pkey, door_pkey = int(lines[0].rstrip()), int(lines[1].rstrip())


def find_key(n, div, l):
    key = 1
    for _ in range(l):
        key = (key * n) % div
    return key


pkey = 1
i = 0
while pkey != card_pkey:
    i += 1
    pkey = (pkey * sub_n) % divider

ekey = find_key(door_pkey, divider, i)
print(ekey)
