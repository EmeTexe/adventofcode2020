all_numbers = [0, 0]
with open('day1_report_repair.txt') as f:
    for line in f:
        current_num = int(line.replace('\n', ''))
        for i in all_numbers:
            for j in all_numbers[:i] + all_numbers[i+1:]:
                if current_num + i + j == 2020:
                    multiplied = current_num * i * j
                    break
            else:
                continue
            break
        else:
            all_numbers.append(current_num)
            continue
        break

print(multiplied)


all_numbers = [0]
with open('day1_report_repair.txt') as f:
    for line in f:
        current_num = int(line.replace('\n', ''))
        all_numbers.append(current_num)
        for i in all_numbers[:-1]:
            if current_num + i == 2020:
                multiplied = current_num * i
                break
        else:
            continue
        break
print(multiplied)