every_ingredients = []
allergen_ingredients = {}
true_allergen_ingredients = {}
safe_ingredients = []
all_dish = []
with open('day21_allergen_assessment.txt', 'r') as f:
    for line in f:
        dish, allergen = line.split(' (')
        all_dish.append(dish.split(' '))
        for ingredient in dish.split(' '):
            if ingredient not in every_ingredients:
                every_ingredients.append(ingredient)
        for a in allergen.rstrip().replace(')', '').replace('contains ', '').split(', '):
            if a not in allergen_ingredients:
                allergen_ingredients[a] = [dish.split(' ')]
            else:
                allergen_ingredients[a].append(dish.split(' '))

for i in every_ingredients:
    is_safe = True
    for key, list_dish in allergen_ingredients.items():
        for dish in list_dish:
            if i not in dish:
                break
        else:
            true_allergen_ingredients[key] = [i] if key not in true_allergen_ingredients else true_allergen_ingredients[
                                                                                                  key] + [i]
            is_safe = False
    if is_safe:
        safe_ingredients.append(i)

n = 0
for i in safe_ingredients:
    for dish in all_dish:
        if i in dish:
            n += 1

print(n)
# part 2
parsed_allergen_ingredients = {}
while len(parsed_allergen_ingredients) < len(allergen_ingredients):
    for key, value in true_allergen_ingredients.items():
        if len(value) == 1:
            parsed_allergen_ingredients[key] = value[0]
            for key2 in true_allergen_ingredients:
                if key2 != key:
                    try:
                        true_allergen_ingredients[key2].remove(value[0])
                    except ValueError:
                        pass

keys = list(parsed_allergen_ingredients.keys())
keys.sort()
to_print = ''
for i in keys:
    to_print = to_print + parsed_allergen_ingredients[i] + ','
print(to_print[:-1])
