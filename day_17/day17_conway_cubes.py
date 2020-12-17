def print_all_voisins_4d():
    """
    print all of the neighbors in 4d (the 80 neighbors) so that we just have to copy/paste it and not write it from scratch
    :return: nothing
    """
    all_voisins = []
    for x in ('x-1', 'x', 'x+1'):
        for y in ('y-1', 'y', 'y+1'):
            for z in ('z-1', 'z', 'z+1'):
                for w in ('w-1', 'w', 'w+1'):
                    all_voisins.append((x, y, z, w))
    to_print = '[('
    for i in all_voisins:
        if i == ('x', 'y', 'z', 'w'):
            continue
        elif i == ('x+1', 'y+1', 'z+1', 'w+1'):
            for j in i:
                to_print += j + ', ' if 'w' not in j else j + ')]'
            break
        for j in i:
            to_print += j + ', ' if 'w' not in j else j + '), ('

    print(to_print)


print_all_voisins_4d()

# part 1
coord_state = {}
with open('day17_conway_cubes.txt', 'r') as f:
    for xi, line in enumerate(f):
        for yi, state in enumerate(line):
            coord_state[(xi, yi, 0)] = 1 if state == '#' else 0


def next_state(x, y, z, state):
    """
    find the next state of the current cube, knowing its position and calculating the number of active neighbors
    :param x: x coordinate of the cube (1st dimension)
    :param y: y coordinate of the cube (2nd dimension)
    :param z: z coordinate of the cube (3rd dimension)
    :param state: current state of the cube
    :return: next state of the cube (1 or 0, respectively active or inactive)
    """
    n_active = 0
    all_voisins = [(x - 1, y - 1, z - 1), (x - 1, y - 1, z), (x - 1, y - 1, z + 1), (x - 1, y, z - 1), (x - 1, y, z),
                   (x - 1, y, z + 1), (x - 1, y + 1, z - 1), (x - 1, y + 1, z), (x - 1, y + 1, z + 1),
                   (x, y - 1, z - 1), (x, y - 1, z), (x, y - 1, z + 1), (x, y, z - 1), (x, y, z + 1), (x, y + 1, z - 1),
                   (x, y + 1, z), (x, y + 1, z + 1), (x + 1, y - 1, z - 1), (x + 1, y - 1, z), (x + 1, y - 1, z + 1),
                   (x + 1, y, z - 1), (x + 1, y, z), (x + 1, y, z + 1), (x + 1, y + 1, z - 1), (x + 1, y + 1, z),
                   (x + 1, y + 1, z + 1)]
    for coord in all_voisins:
        n_active += coord_state[coord] if coord in coord_state else 0

    if state == 1:
        return 1 if 2 <= n_active <= 3 else 0
    else:
        return 1 if n_active == 3 else 0


minx, miny, minz, maxx, maxy, maxz = 0, 0, 0, xi, yi, 0
for i in range(6):
    current_map = {}
    for xi in range(minx - 1, maxx + 2, +1):
        for yi in range(miny - 1, maxy + 2, +1):
            for zi in range(minz - 1, maxz + 2, +1):
                current_state = coord_state[(xi, yi, zi)] if (xi, yi, zi) in coord_state else 0
                current_map[(xi, yi, zi)] = next_state(xi, yi, zi, current_state)
    coord_state = dict(current_map)
    minx, miny, minz, maxx, maxy, maxz = minx - 1, miny - 1, minz - 1, maxx + 1, maxy + 1, maxz + 1
print(sum(coord_state.values()))

# part 2
coord_state = {}
with open('day17_conway_cubes.txt', 'r') as f:
    for xi, line in enumerate(f):
        for yi, state in enumerate(line):
            coord_state[(xi, yi, 0, 0)] = 1 if state == '#' else 0


def next_state_4d(x, y, z, w, state):
    """
    find the next state of the current cube, knowing its position and calculating the number of active neighbors
    :param x: x coordinate of the cube (1st dimension)
    :param y: y coordinate of the cube (2nd dimension)
    :param z: z coordinate of the cube (3rd dimension)
    :param w: w coordinate of the cube (4th dimension)
    :param state: current state of the cube
    :return: next state of the cube (1 or 0, respectively active or inactive)
    """
    n_active = 0
    all_voisins = [(x - 1, y - 1, z - 1, w - 1), (x - 1, y - 1, z - 1, w), (x - 1, y - 1, z - 1, w + 1),
                   (x - 1, y - 1, z, w - 1), (x - 1, y - 1, z, w), (x - 1, y - 1, z, w + 1),
                   (x - 1, y - 1, z + 1, w - 1), (x - 1, y - 1, z + 1, w), (x - 1, y - 1, z + 1, w + 1),
                   (x - 1, y, z - 1, w - 1), (x - 1, y, z - 1, w), (x - 1, y, z - 1, w + 1), (x - 1, y, z, w - 1),
                   (x - 1, y, z, w), (x - 1, y, z, w + 1), (x - 1, y, z + 1, w - 1), (x - 1, y, z + 1, w),
                   (x - 1, y, z + 1, w + 1), (x - 1, y + 1, z - 1, w - 1), (x - 1, y + 1, z - 1, w),
                   (x - 1, y + 1, z - 1, w + 1), (x - 1, y + 1, z, w - 1), (x - 1, y + 1, z, w),
                   (x - 1, y + 1, z, w + 1), (x - 1, y + 1, z + 1, w - 1), (x - 1, y + 1, z + 1, w),
                   (x - 1, y + 1, z + 1, w + 1), (x, y - 1, z - 1, w - 1), (x, y - 1, z - 1, w),
                   (x, y - 1, z - 1, w + 1), (x, y - 1, z, w - 1), (x, y - 1, z, w), (x, y - 1, z, w + 1),
                   (x, y - 1, z + 1, w - 1), (x, y - 1, z + 1, w), (x, y - 1, z + 1, w + 1), (x, y, z - 1, w - 1),
                   (x, y, z - 1, w), (x, y, z - 1, w + 1), (x, y, z, w - 1), (x, y, z, w + 1), (x, y, z + 1, w - 1),
                   (x, y, z + 1, w), (x, y, z + 1, w + 1), (x, y + 1, z - 1, w - 1), (x, y + 1, z - 1, w),
                   (x, y + 1, z - 1, w + 1), (x, y + 1, z, w - 1), (x, y + 1, z, w), (x, y + 1, z, w + 1),
                   (x, y + 1, z + 1, w - 1), (x, y + 1, z + 1, w), (x, y + 1, z + 1, w + 1),
                   (x + 1, y - 1, z - 1, w - 1), (x + 1, y - 1, z - 1, w), (x + 1, y - 1, z - 1, w + 1),
                   (x + 1, y - 1, z, w - 1), (x + 1, y - 1, z, w), (x + 1, y - 1, z, w + 1),
                   (x + 1, y - 1, z + 1, w - 1), (x + 1, y - 1, z + 1, w), (x + 1, y - 1, z + 1, w + 1),
                   (x + 1, y, z - 1, w - 1), (x + 1, y, z - 1, w), (x + 1, y, z - 1, w + 1), (x + 1, y, z, w - 1),
                   (x + 1, y, z, w), (x + 1, y, z, w + 1), (x + 1, y, z + 1, w - 1), (x + 1, y, z + 1, w),
                   (x + 1, y, z + 1, w + 1), (x + 1, y + 1, z - 1, w - 1), (x + 1, y + 1, z - 1, w),
                   (x + 1, y + 1, z - 1, w + 1), (x + 1, y + 1, z, w - 1), (x + 1, y + 1, z, w),
                   (x + 1, y + 1, z, w + 1), (x + 1, y + 1, z + 1, w - 1), (x + 1, y + 1, z + 1, w),
                   (x + 1, y + 1, z + 1, w + 1)]

    for coord in all_voisins:
        n_active += coord_state[coord] if coord in coord_state else 0

    if state == 1:
        return 1 if 2 <= n_active <= 3 else 0
    else:
        return 1 if n_active == 3 else 0


minx, miny, minz, minw, maxx, maxy, maxz, maxw = 0, 0, 0, 0, xi, yi, 0, 0
for i in range(6):
    current_map = {}
    for xi in range(minx - 1, maxx + 2, +1):
        for yi in range(miny - 1, maxy + 2, +1):
            for zi in range(minz - 1, maxz + 2, +1):
                for wi in range(minw - 1, maxw + 2, +1):
                    current_state = coord_state[(xi, yi, zi, wi)] if (xi, yi, zi, wi) in coord_state else 0
                    current_map[(xi, yi, zi, wi)] = next_state_4d(xi, yi, zi, wi, current_state)
    coord_state = dict(current_map)
    minx, miny, minz, minw, maxx, maxy, maxz, maxw = minx - 1, miny - 1, minz - 1, minw - 1, maxx + 1, maxy + 1, maxz + 1, maxw + 1
print(sum(coord_state.values()))
