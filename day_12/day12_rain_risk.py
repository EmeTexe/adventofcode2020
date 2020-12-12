import time

with open('day12_rain_risk.txt', 'r') as f:
    directions = [i.replace('\n', '') for i in f.readlines()]


def next_place(d):
    direc, dist = d[0], int(d[1:])
    if direc == 'F':
        positions_boat['x'] += positions_way['x'] * dist
        positions_boat['y'] += positions_way['y'] * dist
    elif direc == 'R':
        if dist == 90:
            new_x, new_y = positions_way['y'], -positions_way['x']
            positions_way['x'], positions_way['y'] = new_x, new_y
        elif dist == 180:
            positions_way['x'], positions_way['y'] = -positions_way['x'], -positions_way['y']
        elif dist == 270:
            new_x, new_y = -positions_way['y'], positions_way['x']
            positions_way['x'], positions_way['y'] = new_x, new_y
    elif direc == 'L':
        if dist == 90:
            new_x, new_y = -positions_way['y'], positions_way['x']
            positions_way['x'], positions_way['y'] = new_x, new_y
        elif dist == 180:
            positions_way['x'], positions_way['y'] = -positions_way['x'], -positions_way['y']
        elif dist == 270:
            new_x, new_y = positions_way['y'], -positions_way['x']
            positions_way['x'], positions_way['y'] = new_x, new_y
    else:
        if direc == 'N':
            positions_way['y'] += dist
        elif direc == 'S':
            positions_way['y'] -= dist
        elif direc == 'E':
            positions_way['x'] += dist
        elif direc == 'W':
            positions_way['x'] -= dist


positions_boat = {'x': 0, 'y': 0}
positions_way = {'x': 10, 'y': 1}

for d in directions:
    next_place(d)
    # print(f"{d}, boat = {positions_boat}, waypoint = {positions_way}")
    # time.sleep(1)

print(abs(positions_boat['x']) + abs(positions_boat['y']))
