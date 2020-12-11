total = 0
current_list = []
i = 0
with open("day6_custom_customs.txt", 'r') as f:
    for line in f:
        if line == '\n':
            total += len(current_list)
            current_list, i = [], 0
        else:
            if i == 0:
                current_list = [c for c in line.replace('\n', '') if c not in current_list]
            else: current_list = list(set(line.replace('\n', '')) & set(current_list))
            i += 1

print(total)
