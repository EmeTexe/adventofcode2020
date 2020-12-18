# part 1
with open('day18_operation_order.txt', 'r') as f:
    all_calculus = [i.rstrip() for i in f.readlines()]


def find_most_nested(calculus):
    most = 0
    maxi = 0
    for calc in calculus:
        for c in calc:
            most = most + 1 if c == '(' else most - 1 if c == ')' else most
            if most > maxi:
                maxi = most
    return maxi


def find_all_nested(calculus, n):
    all_nested = []
    for calc in calculus:
        all_nested.append([])
        level, start = 0, 0
        for i, c in enumerate(calc):
            if c == '(':
                level += 1
                if level == n:
                    start = i
            elif c == ')':
                level -= 1
                if level == n - 1:
                    all_nested[-1].append((start, i))
    return all_nested


def reduce_calculus(calculus, nested):
    for i, nests in enumerate(nested):
        current_calc_ints = []
        for nest in nests:
            begin, end = nest[0], nest[1]
            current, integ, sign = 0, 0, '+'
            for c in calculus[i][begin + 1:end].split():
                if c == '+':
                    sign = '+'
                elif c == '*':
                    sign = '*'
                else:
                    integ = int(c)
                    current = current + integ if sign == '+' else current * integ
            current_calc_ints.append(current)
        modified_calc = ''
        if len(current_calc_ints) == 0:
            continue
        for n, inte in enumerate(current_calc_ints):
            if n == 0:
                start = 0
            else:
                start = nests[n - 1][1] + 1
            modified_calc += calculus[i][start:nests[n][0]] + str(inte)
        if nests[n][1] + 1 == len(calculus[i]):
            calculus[i] = modified_calc[:]
        else:
            calculus[i] = modified_calc[:] + calculus[i][nests[n][1] + 1:]
    return calculus


def final_sum(calculus):
    total = 0
    for calc in calculus:
        current_tot, sign = 0, '+'
        for c in calc.split():
            if c == '+':
                sign = '+'
            elif c == '*':
                sign = '*'
            else:
                integ = int(c)
                current_tot = current_tot + integ if sign == '+' else current_tot * integ
        total += current_tot
    return total


maxi_parenthesis = find_most_nested(all_calculus)
for i in range(maxi_parenthesis, 0, -1):
    all_nested = find_all_nested(all_calculus, i)
    all_calculus = reduce_calculus(all_calculus, all_nested)
    # print(all_calculus)

print(final_sum(all_calculus))

# part 2
total = 0
with open('day18_operation_order.txt', 'r') as f:
    for line in f:
        line = line.rstrip().replace("(", "((")
        line = line.replace(")", "))")
        line = line.replace(" * ", ") * (")
        line = "(" + line + ")"
        # print(line)
        total += eval(line)
print(total)

# discovered the 'eval()' function for the part 2, will redo part 1 knowing that when I have time (and desire) to do so
