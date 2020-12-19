import time

t1 = time.time()
rules = {}
messages = []
message = False
max_len_message = 0
with open('day19_monster_messages.txt', 'r') as f:
    for line in f:
        if line == '\n':
            message = True
        elif message:
            messages.append(line.rstrip())
            max_len_message = len(line.rstrip()) if len(line.rstrip()) > max_len_message else max_len_message
        else:
            if '"' not in line:
                n = line.split(': ')[0]
                rule = line.rstrip().split(': ')[1]
                rules[n] = [i for i in rule.split(' ')]
            else:
                n = line.split(': ')[0]
                rule = line.rstrip().split(': ')[1].split('"')[1]
                rules[n] = rule

valid_rules = {}
for key, value in rules.items():
    if type(value) == str:
        valid_rules[key] = [value]


def make_rule_valid(rule: [str], valid_rules: {int: [str]}) -> [str]:
    rules = [x.split(' ') for x in " ".join(rule).split(" | ")]
    valid_rule = []
    for r in rules:
        current_rule = []
        if len(r) == 1:
            current_rule = valid_rules[r[0]]
        else:
            for value1 in valid_rules[r[0]]:
                for value2 in valid_rules[r[1]]:
                    if len(r) == 3:
                        for value3 in valid_rules[r[2]]:
                            current_rule.append(value1 + value2 + value3)
                    else:
                        current_rule.append(value1 + value2)
        valid_rule += current_rule
    return valid_rule


while len(rules) > (len(valid_rules) + 3):
    for n, rule in rules.items():
        if n in ['8', '11', '0']:
            continue
        else:
            parsed_rule = rule[:]
            if '|' in parsed_rule:
                parsed_rule.remove('|')
            can_become_valid = True
            for i in parsed_rule:
                if i not in valid_rules.keys():
                    can_become_valid = False
            # print(can_become_valid)

            if can_become_valid:
                valid_rules[n] = make_rule_valid(rule, valid_rules)

n = 0
rules0 = [42, 42, 31]
for m in messages:
    if len(m) / 8 != 3:
        continue
    m_split = [m[i:i + 8] for i in range(0, len(m), 8)]
    is_correct = False
    for i, word in enumerate(m_split):
        if word not in valid_rules[str(rules0[i])]:
            break
    else:
        is_correct = True
    if is_correct:
        n += 1
print(n)

"""
8: 42 | 42 8
11: 42 31 | 42 11 31

len of each elements in rule 42 anr rule 31 are 8, so a maximum of 12 elements (96 being the length of message with most char)
all possible combinations of rules for 0 : """

all_rules_str = '42 42 31 | 42 42 42 31 | 42 42 42 42 31 | 42 42 42 42 42 31 | 42 42 42 42 42 42 31 | 42 42 42 42 42 ' \
                '42 42 31 | 42 42 42 42 42 42 42 42 31 | 42 42 42 42 42 42 42 42 42 31 | 42 42 42 42 42 42 42 42 42 ' \
                '42 31 | 42 42 42 42 42 42 42 42 42 42 42 31 | 42 42 42 31 31 | 42 42 42 42 31 31 | 42 42 42 42 42 31 ' \
                '31 | 42 42 42 42 42 42 31 31 | 42 42 42 42 42 42 42 31 31 | 42 42 42 42 42 42 42 42 31 31 | 42 42 42 ' \
                '42 42 42 42 42 42 31 31 | 42 42 42 42 42 42 42 42 42 42 31 31 | 42 42 42 42 31 31 31 | 42 42 42 42 ' \
                '42 31 31 31 | 42 42 42 42 42 42 31 31 31 | 42 42 42 42 42 42 42 31 31 31 | 42 42 42 42 42 42 42 42 ' \
                '31 31 31 | 42 42 42 42 42 42 42 42 42 31 31 31 | 42 42 42 42 42 31 31 31 31 | 42 42 42 42 42 42 31 ' \
                '31 31 31 | 42 42 42 42 42 42 42 31 31 31 31 | 42 42 42 42 42 42 42 42 31 31 31 31 | 42 42 42 42 42 ' \
                '42 31 31 31 31 31 | 42 42 42 42 42 42 42 31 31 31 31 31'
rules0 = {}
for r in all_rules_str.split(' | '):
    key = len(r.split(' '))
    if key not in rules0:
        rules0[key] = [r.split(' ')]
    else:
        rules0[key].append(r.split(' '))

n = 0
for x, message in enumerate(messages):
    # print(x)
    if len(message) % 8 != 0 or len(message) < 24:
        print(message)
        continue
    n_combi = int(len(message) / 8)
    m_split = [message[i:i + 8] for i in range(0, len(message), 8)]
    # print(m_split)
    is_correct = False
    for rule in rules0[n_combi]:
        for i, word in enumerate(m_split):
            if word not in valid_rules[rule[i]]:
                break
        else:
            is_correct = True
            break
    if is_correct:
        n += 1

print(n)
print(time.time() - t1)

"""had so much trouble, took me hours to figure out how to do it, would surely have been easier and quicker to learn 
regex (that i don't know how to use yet) and write the code... But like bethesda said : 'it just works'
And it works fast, my solution take only 0.012s, or 12ms"""
