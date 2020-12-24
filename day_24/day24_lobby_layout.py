"""
rules : x   y
nw : -0.5 +0.5
ne : +0.5 +0.5
sw : -0.5 -0.5
se : +0.5 -0.5
w : -1 0
e : +1 0
"""
from tqdm import tqdm


def find_x_y(directions):
    nw = directions.count('nw')
    ne = directions.count('ne')
    sw = directions.count('sw')
    se = directions.count('se')
    w = directions.count('w') - nw - sw
    e = directions.count('e') - ne - se
    return e - w + 0.5 * (ne + se) - 0.5 * (nw + sw), 0.5 * (nw + ne) - 0.5 * (sw + se)


def fill_dict(n_day):
    global all_tiles
    # this is largely sufficient for a map, don't need to go further
    xint, yint = range(int(-x_max - n_day / 2), int(x_max + n_day / 2) + 2, 1), range(int(-x_max - n_day / 2),
                                                                                      int(y_max + n_day / 2) + 2, 1)
    xfloat, yfloat = [i - 0.5 for i in xint], [i - 0.5 for i in yint]
    for x in xint:
        for y in yint:
            all_tiles[(x, y)] = all_tiles.get((x, y), 0) + 0
    for x in xfloat:
        for y in yfloat:
            all_tiles[(x, y)] = all_tiles.get((x, y), 0) + 0


def get_neighbor(x, y):
    v1 = all_tiles[(x + 1, y)] % 2 if (x + 1, y) in all_tiles else 0
    v2 = all_tiles[(x - 1, y)] % 2 if (x - 1, y) in all_tiles else 0
    v3 = all_tiles[(x + 0.5, y + 0.5)] % 2 if (x + 0.5, y + 0.5) in all_tiles else 0
    v4 = all_tiles[(x + 0.5, y - 0.5)] % 2 if (x + 0.5, y - 0.5) in all_tiles else 0
    v5 = all_tiles[(x - 0.5, y + 0.5)] % 2 if (x - 0.5, y + 0.5) in all_tiles else 0
    v6 = all_tiles[(x - 0.5, y - 0.5)] % 2 if (x - 0.5, y - 0.5) in all_tiles else 0
    return sum((v1, v2, v3, v4, v5, v6))


def one_turn():
    current_tiles = {}
    global all_tiles
    for key, value in all_tiles.items():
        n_black = get_neighbor(key[0], key[1])
        if value % 2 == 1:
            current_tiles[key] = 0 if n_black == 0 or n_black > 2 else 1
        else:
            current_tiles[key] = 1 if n_black == 2 else 0
    return current_tiles


n_day = 100
all_tiles = {}
x_max, y_max = 0, 0
with open('day24_lobby_layout.txt') as f:
    for line in f:
        x, y = find_x_y(line)
        x_max = x if x > x_max else x_max
        y_max = y if y > y_max else y_max
        all_tiles[(x, y)] = all_tiles.get((x, y), 0) + 1

print(f"Day 0 : {sum([1 for i in all_tiles.values() if i % 2 != 0])}")

fill_dict(n_day)

for i in tqdm(range(1, n_day + 1)):
    all_tiles = one_turn()
print(f"Day {i} : {sum([1 for i in all_tiles.values() if i % 2 != 0])}")
