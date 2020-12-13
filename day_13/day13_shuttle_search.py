with open('day13_shuttle_search.txt', 'r') as f:
    depart_time = int(f.readline().replace('\n', ''))
    all_bus, all_diff_t, n = [], [], 0
    for i in f.readline().replace('\n', '').split(','):
        if 'x' not in i:
            all_bus.append(int(i))
            all_diff_t.append(n)
        n += 1

t = all_bus[0]
up = all_bus[0]
for i in range(1, len(all_bus)):
    while (t + all_diff_t[i]) % all_bus[i] != 0:
        t += up
    up *= all_bus[i]

print(t)

# for i in range(depart_time, depart_time + min(all_bus)):
#     for bus in all_bus:
#         if i%bus == 0:
#             break
#     else: continue
#     break
#
# print((i - depart_time)*bus)
