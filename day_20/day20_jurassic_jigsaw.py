import numpy as np
import time

AllTiles = {}
AllBorders = {}
tiles = {}
with open('day20_jurassic_jigsaw.txt', 'r') as f:
    for line in f:
        if 'Tile' in line:
            current_tile = line.split(' ')[1].rstrip().replace(':', '')
            tiles[current_tile] = []
        elif line == '\n':
            continue
        else:
            tiles[current_tile].append([i for i in line.rstrip()])


def gen_borders(tile):
    return np.array([tile[0, :], tile[:, -1], tile[-1, :], tile[:, 0]])


def gen_all_tiles(num, tile):
    global AllTiles
    if num in AllTiles:
        return AllTiles[num]
    tiles = [tile, np.rot90(tile, 1), np.rot90(tile, 2), np.rot90(tile, 3), np.flipud(tile),
             np.rot90(np.flipud(tile), 1), np.rot90(np.flipud(tile), 2), np.rot90(np.flipud(tile), 3)]
    AllTiles[num] = tiles


def gen_all_borders(num, tiles):
    global AllBorders
    AllBorders[num] = [gen_borders(i) for i in tiles]


for key, value in tiles.items():
    tiles[key] = np.array(value)
    gen_all_tiles(key, tiles[key])
    gen_all_borders(key, AllTiles[key])


def find_match_border(n, b, ignore):
    nb = 0
    for num, all_borders in AllBorders.items():
        for i, border in enumerate(all_borders):
            # print(border[n])
            if np.array_equal(b, border[n]) and num not in ignore:
                return num, i
    return None, None


def find_top_left_corner():
    for num, all_borders in AllBorders.items():
        # print(num)
        for i, borders in enumerate(all_borders):
            n_lone = 0
            match_tile, match_orientation = find_match_border(0, borders[0], [num])
            if match_tile is None:
                n_lone += 1
            match_tile, match_orientation = find_match_border(3, borders[3], [num])
            if match_tile is None:
                n_lone += 1
            if n_lone == 2:
                print(num)
                return num, i


def find_all_corners():
    corners = []
    for num, all_borders in AllBorders.items():
        # print(num)
        for i, borders in enumerate(all_borders):
            n_lone = 0
            for n, b in enumerate(borders):
                match_tile, match_orientation = find_match_border(n, b, [num])
                if match_tile is None:
                    n_lone += 1
            if n_lone == 2:
                if num not in corners:
                    print(num)
                    corners.append(num)
    return corners


# product = 1
# for i in find_all_corners():
#     product *= int(i)
# print(product)

Grid = [[]]


def extend_grid(x, y):
    if x == 0:
        key = Grid[x][y - 1]
        n = 2
        border = AllBorders[key[0]][key[1]][n]
    else:
        key = Grid[x - 1][y]
        n = 1
        border = AllBorders[key[0]][key[1]][n]
    num, i = find_match_border(n, border, already_in)
    if num is None:
        exit(1)
    return num, i


already_in = []
squarelen = 12  # we have 144 tiles, so a square of length sqrt(144)
for x in range(squarelen):
    for y in range(squarelen):
        print(f"{x}, {y}")
        if x == 0 and y == 0:
            Grid[x].append(find_top_left_corner())
            already_in.append(Grid[x][y][0])
            continue
        Grid[x].append(extend_grid(x, y))
        already_in.append(Grid[x][y][0])
    if x != 11:
        Grid.append([])

for i in Grid:
    print(i)

"""I abandon, I have no idea why it doesn't work, spent so much time for nothing :( """
