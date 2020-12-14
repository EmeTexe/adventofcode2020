# part 1
def apply_mask(value, mask):
    binary = list(bin(value))[2:]
    length = len(binary)

    for _ in range(36 - length):
        binary.insert(0, '0')

    for i, c in enumerate(mask):
        if c == 'X':
            pass
        else:
            binary[i] = c

    return sum([int(j) * 2 ** i for i, j in enumerate(binary[::-1])])


memory = {}

with open('day14_docking_data.txt', 'r') as f:
    for line in f:
        if 'mask' in line:
            mask = line.split(' = ')[1].replace('\n', '')
        elif 'mem' in line:
            mem_adress = int(line.split('[')[1].split(']')[0])
            value = int(line.replace('\n', '').split(' = ')[1])
            memory[mem_adress] = apply_mask(value, mask)

print(sum(list(memory.values())))


# part 2
def apply_mask_memory(value, mask):
    binary = list(bin(value))[2:]
    length = len(binary)

    for _ in range(36 - length):
        binary.insert(0, '0')

    all_values = []
    position_x, int_position_x = bin(0)[2:].zfill(36), 0
    for i in range(2 ** mask.count('X')):
        current_binary = binary[:]
        count_x = 0

        for j in range(len(mask)):
            if mask[j] == 'X':
                count_x += 1
                current_binary[j] = position_x[-count_x]
            elif mask[j] == '1':
                current_binary[j] = '1'

        all_values.append(current_binary)
        int_position_x += 1
        position_x = bin(int_position_x)[2:].zfill(36)

    return [sum([int(j) * 2 ** i for i, j in enumerate(n[::-1])]) for n in all_values]


memory = {}
with open('day14_docking_data.txt', 'r') as f:
    for line in f:
        if 'mask' in line:
            mask = line.split(' = ')[1].replace('\n', '')
        elif 'mem' in line:
            mem_adress = int(line.split('[')[1].split(']')[0])
            value = int(line.replace('\n', '').split(' = ')[1])
            mem_adresses = apply_mask_memory(mem_adress, mask)

            for i in mem_adresses:
                memory[i] = value

print(sum(list(memory.values())))
