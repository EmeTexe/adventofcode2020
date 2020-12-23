import time

start = time.time()
puzzle_input = '789465123'

"""
# My first function, that was waaayyyyy too slow for part 2 (almost 5000 time slower than part 2 function)
def play_part1(cups, n):
    print(cups)
    l = len(cups)
    current_i = 0
    current_cup = cups[0]
    for i in range(n):
        selection = [cups[j % l] for j in range(current_i+1, current_i+4)]
        for c in selection:
            cups.remove(c)
        dest = l if current_cup == 1 else current_cup - 1
        while dest in selection:
            dest = l if dest == 1 else dest - 1
        dest_index = cups.index(dest) + 1
        for j, c in enumerate(selection):
            cups.insert(dest_index + j, c)
        current_i = (cups.index(current_cup) + 1) % l
        current_cup = cups[current_i]
    return cups
"""


def play_part2(cups, n):
    l = len(cups)
    d_cups = {}
    for i in range(l - 1):
        d_cups[cups[i]] = cups[i + 1]
    d_cups[cups[-1]] = cups[0]

    current_cup = d_cups[cups[-1]]
    for i in range(n):

        next_ = d_cups[current_cup]
        selection = []
        for _ in range(3):
            selection.append(next_)
            next_ = d_cups[next_]

        dest = l if current_cup == 1 else current_cup - 1
        while dest in selection:
            dest = l if dest == 1 else dest - 1

        d_cups[current_cup] = d_cups[selection[-1]]
        d_cups[selection[-1]] = d_cups[dest]
        d_cups[dest] = selection[0]
        current_cup = d_cups[current_cup]

    return d_cups


cups = [int(i) for i in puzzle_input]
d_cups = play_part2(cups, 100)
next_ = 1
result_str2 = ''
for _ in range(len(d_cups) - 1):
    result_str2 += str(d_cups[next_])
    next_ = d_cups[next_]

print(result_str2)

cups = [int(i) for i in puzzle_input]
part2_cups = cups + list(range(10, 1_000_001))
part2_d_cups = play_part2(part2_cups, 10_000_000)
a = part2_d_cups[1]
b = part2_d_cups[a]
print(a * b)
# 15 seconds on computation time
print(time.time() - start)
