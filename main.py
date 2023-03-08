import os
from pprint import pprint

def form_cook_book(file, path = os.getcwd()):
    with open('cook_book.txt', 'rt', encoding='utf-8') as f:
        cook_book = {}
            # ingrs = []
        for string in f:
            dish = string.strip()
            ingrs_count = int(f.readline().strip())
            ingredients = []
            for i in range(ingrs_count):
                ingredient_name, quantity, measure = f.readline().strip().split(' | ')
                ingredients.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
            f.readline()
            cook_book[dish] = ingredients
        # pprint(cook_book, sort_dicts=False)
        return cook_book


def count_ingredients(cook_book, dishes, person_count):
    purchase = {}
    for dish in dishes:
        if dish in cook_book:
            pass
        else:
            dishes.remove(dish)
            print(f'Блюда "{dish}" нет в кулинарной книге. Список будет рассчитан без него.')
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in purchase.keys():
                purchase[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                           'quantity': ingredient['quantity'] * person_count}
            else:
                purchase[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return purchase


book = form_cook_book('cook_book.txt')
pprint(count_ingredients(book, ['Омлет', 'Фахитос', 'Карбонара'], 3))
