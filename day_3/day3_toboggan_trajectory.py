# nb_tree = 0
# j = 0
# with open('day3_toboggan_trajectory.txt') as f:
#     for line in f:
#         toboggan_line = line.replace('\n', '')
#         if toboggan_line[j] == '#':
#             nb_tree += 1
#         j = (j + 3) % len(toboggan_line)
#
# print(nb_tree)

all_slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def count_trees(r, d):
    nb_tree = 0
    i = 0
    j = 0
    with open('day3_toboggan_trajectory.txt') as f:
        for line in f:
            toboggan_line = line.replace('\n', '')
            print(i%d)
            if i % d == 0:
                if toboggan_line[j] == '#':
                    nb_tree += 1
                j = (j + r) % len(toboggan_line)
            i+=1

    return nb_tree


result = 1
for slope in all_slopes:
    result *= count_trees(slope[0], slope[1])

print(result)
