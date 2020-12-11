import copy

with open('day11_seating_system.txt', 'r') as f:
    seat_map = [[j for j in i.replace('\n', '')] for i in f.readlines()]
    print(seat_map)


def new_state(x, y, seats):
    neighbours = find_neighbour(x - 1, -1, y - 1, -1, seats) + find_neighbour(x - 1, -1, y, 0, seats) + find_neighbour(
        x - 1, -1, y + 1, +1, seats) + \
                 find_neighbour(x, 0, y - 1, -1, seats) + find_neighbour(x, 0, y + 1, +1, seats) + \
                 find_neighbour(x + 1, +1, y - 1, -1, seats) + find_neighbour(x + 1, +1, y, 0, seats) + find_neighbour(
        x + 1, +1, y + 1, +1, seats)
    n_occupied = neighbours.count('#')
    current_state = seats[x][y]
    if current_state == '#':
        return '#' if n_occupied < 5 else 'L'
    if current_state == 'L':
        return '#' if n_occupied == 0 else 'L'
    else:
        return '.'


def valid(xi, yj, seats):
    # print(type(xi), type(yj))
    if xi < 0 or xi >= len(seats) or yj < 0 or yj >= len(seats[0]):
        return '.'
    else:
        return seats[xi][yj]


def is_valid(xi, yj, seats):
    if xi < 0 or xi >= len(seats) or yj < 0 or yj >= len(seats[0]):
        return False
    else:
        return True


def find_neighbour(xi, xi_change, yj, yj_change, seats):
    result = valid(xi, yj, seats)
    while is_valid(xi, yj, seats):
        result = seats[xi][yj]
        if result == '#' or result == 'L':
            break
        xi += xi_change
        yj += yj_change
    return result


def print_2d_list(seat_map):
    for i in seat_map:
        print(i)


current_map = copy.deepcopy(seat_map)
n = 0
while True:
    print(n)
    for i in range(len(seat_map)):
        for j in range(len(seat_map[i])):
            current_map[i][j] = new_state(i, j, seat_map)
    if current_map == seat_map:
        break
    n += 1
    seat_map = copy.deepcopy(current_map)

n_diese = 0
for i in seat_map:
    n_diese += i.count('#')
print(n_diese)
