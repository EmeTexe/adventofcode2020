n_empty_line = 0
field_valid = {}
all_tickets = []
all_valid = []
with open('day16_ticket_translation.txt', 'r') as f:
    for line in f:
        if line == '\n':
            n_empty_line += 1
        elif n_empty_line == 0:
            ranges = line.replace('\n', '').split(': ')[1].split(' or ')
            valids = []
            for r in ranges:
                for i in range(int(r.split('-')[0]), int(r.split('-')[1]) + 1, 1):
                    valids.append(i)
                    all_valid.append(i)
            field_valid[line.split(': ')[0]] = valids
        elif n_empty_line == 1 and 'your' not in line:
            my_ticket = [int(i) for i in line.replace('\n', '').split(',')]
        elif n_empty_line == 2 and 'nearby' not in line:
            all_tickets.append([int(i) for i in line.replace('\n', '').split(',')])
del n_empty_line
# part 1
minima = min(all_valid)
maxima = max(all_valid)
all_invalid = [i for i in range(minima, maxima + 1) if i not in all_valid]
del all_valid

error_rate = 0
for ticket in all_tickets:
    for n in ticket:
        if n in all_invalid or n < minima or n > maxima:
            error_rate += n
            break

print(error_rate)


# part 2
def find_possibles(t, field_valid, all_possible):
    current_possible = []
    for field, valid in field_valid.items():
        if t in valid:
            current_possible.append(field)

    return [i for i in current_possible if i in all_possible]


n_invalid = 0
for i in range(len(all_tickets)):
    for n in all_tickets[i - n_invalid]:
        if n in all_invalid or n < minima or n > maxima:
            del all_tickets[i - n_invalid]
            n_invalid += 1
            break

possibilities = []
for i in range(len(my_ticket)):
    all_possible = list(field_valid.keys())
    for t in all_tickets:
        all_possible = find_possibles(t[i], field_valid, all_possible)
    possibilities.append(all_possible)
del all_tickets

discovered = []
for _ in range(len(field_valid)):
    new_discovered = []
    for poss in possibilities:
        if len(poss) == 1 and poss[0] not in discovered:
            new_discovered.append(poss[0])
    for i, poss in enumerate(possibilities):
        for p in new_discovered:
            if p in poss and len(poss) > 1:
                possibilities[i].remove(p)
    if len(new_discovered) == 0:
        break
    else:
        for i in new_discovered:
            discovered.append(i)
del new_discovered
del discovered
del field_valid

print(possibilities)
multiplied_values = 1
for i, p in enumerate(possibilities):
    if 'departure' in p[0]:
        multiplied_values *= my_ticket[i]
        print(my_ticket[i])
print(multiplied_values)
