import os
from pprint import pprint

with open('cook_book.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
        # ingrs = []
    for string in f:
        name = string.strip()
        ingrs_count = int(f.readline().strip())
        ingredients = []
        for i in range(ingrs_count):
            ingredient_name, quantity, measure = f.readline().strip().split(' | ')
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
        f.readline()
        cook_book[name] = ingredients
    pprint(cook_book, sort_dicts=False)