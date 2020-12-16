import time

number_turns = {}
with open('day15_rambunctious_recitation.txt', 'r') as f:
    for i, num in enumerate(f.readline().replace('\n', '').split(',')):
        number_turns[int(num)] = [i]
    last_turn = int(num)
number_turns.pop(last_turn)
number_turns[0] = number_turns.get(0, [])

start = len(number_turns) + 1
for i in range(start, 30_000_000, +1):
    if i % 100000 == 0:
        print(i)
    if last_turn in number_turns:
        current_turn = i - 1 - number_turns[last_turn][-1]
        number_turns[last_turn].append(i - 1)
    else:
        current_turn = 0
        number_turns[last_turn] = [i - 1]
    last_turn = current_turn

print(f"{last_turn}")
