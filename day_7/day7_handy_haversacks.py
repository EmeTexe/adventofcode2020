import time

gloabl_parent_children = {}

with open("day7_handy_haversacks.txt", 'r') as f:
    for line in f:
        if 'other' not in line:
            gloabl_parent_children[line.split(' contain ')[0].split(' bag')[0]] = [
                (int(color.split(' bag')[0].split(' ')[0]), ' '.join(color.split(' bag')[0].split(' ')[1:])) for color
                in line.split(' contain ')[1].split(', ')]

list_of_children = [(1, 'shiny gold')]
total = 0
while len(list_of_children) != 0:
    print(list_of_children)
    current_list_of_children = []
    for elem in list_of_children:
        for parent, children in gloabl_parent_children.items():
            if elem[1] == parent:
                for child in children:
                    n = elem[0] * child[0]
                    current_list_of_children.append((n, child[1]))
                    total += n
    list_of_children = current_list_of_children
print(total)

# global_list_of_parents = []
# list_of_parents = ['shiny gold']
# while len(list_of_parents) != 0:
#     current_list_of_parents = []
#     print(list_of_parents)
#     time.sleep(1)
#     for elem in list_of_parents:
#         # for parent, children in gloabl_parent_children.items():
#         #     if elem in children:
#         #         current_list_of_parents.append(parent)
#         current_list_of_parents += [parent for parent, children in gloabl_parent_children.items() if elem in children]
#     list_of_parents = current_list_of_parents
#     global_list_of_parents += [parent for parent in list_of_parents if parent not in global_list_of_parents]
#
# print(len(set(global_list_of_parents)))
