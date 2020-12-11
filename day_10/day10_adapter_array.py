with open('day10_adapter_array.txt', 'r') as f:
    adapters = [int(i.replace('\n', '')) for i in f.readlines()]


def find_suit(adapter):
    n1, n2, n3 = 0, 0, 0
    for i in range(len(adapter)-1):
        if adapter[i+1] - adapter[i] == 1:
            n1 += 1
        elif adapter[i+1] - adapter[i] == 3:
            n3 += 1
        elif adapter[i+1] - adapter[i] == 2:
            n2 += 1
        else:
            raise Exception(f"i is {i}, could not compute {adapter[i+1]} - {adapter[i]}, difference is {adapter[i+1] - adapter[i]}")

    return n1, n2, n3+1


def find_multiplier(n):
    begin_multipliers = [1, 1, 2]
    for i in range(n+1):
        if i<len(begin_multipliers):
            pass
        else:
            begin_multipliers.append(sum(begin_multipliers[i-3:i]))
    return begin_multipliers[i]


def find_arrangements(adapters):
    n_arrangement = 1
    previous_diff, current_n = 0, 0
    for i in range(len(adapters)-1):
        diff = adapters[i+1] - adapters[i]
        if diff == previous_diff:
            current_n += 1
        else:
            if previous_diff == 1:
                n_arrangement *= find_multiplier(current_n)
            previous_diff, current_n = diff, 1

    return n_arrangement


adapters.append(0)
adapters.sort()
adapters.append(adapters[-1]+3)
print(adapters)
# print(adapters)
# n1, n2, n3 = find_suit(adapters)
# print(f"n1 = {n1}, n2 = {n2}, n3 = {n3}\n{n1*n3}")
print(find_arrangements(adapters))

