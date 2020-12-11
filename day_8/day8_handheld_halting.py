
with open("day8_handheld_halting.txt", 'r') as f:
    instructions = [i.replace('\n', '') for i in f.readlines()]

print(instructions)


def do_instruction(i, n, instructions):
    inst = instructions[i]
    if inst[0:3] == 'acc':
        return i+1, n+int(inst[5:]) if inst[4] == '+' else n-int(inst[5:])
    elif inst[0:3] == 'nop':
        return i+1, n
    elif inst[0:3] == 'jmp':
        return i+int(inst[5:])if inst[4] == '+' else i-int(inst[5:]), n
    else: return i,n


def find_end_loop(instructions):
    acc = 0
    list_i = [0]
    i = 0
    for _ in range(len(instructions)):
        i, acc = do_instruction(i, acc, instructions)
        if i in list_i:
            return acc, True
        else:
            list_i.append(i)
        if i == len(instructions):
            return acc, False
    return acc, False

print(find_end_loop(instructions))
for_end = len(instructions)
for l in range(for_end):
    # print(l)
    if instructions[l][0:3] == 'jmp':
        current_instructions = instructions.copy()
        current_instructions[l] = 'nop' + instructions[l][3:]
        print(instructions[l], current_instructions[l])
        acc, is_loop = find_end_loop(current_instructions)
        if not is_loop:
            print(acc)
            break
    elif instructions[l][0:3] == 'nop':
        current_instructions = instructions.copy()
        current_instructions[l] = 'jmp' + instructions[l][3:]
        print(instructions[l], current_instructions[l])
        acc, is_loop = find_end_loop(current_instructions)
        if not is_loop:
            print(acc)
            break
