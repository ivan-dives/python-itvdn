# Створіть функцію category_stat(data_file) яка на вхід отримує один аргумент, що є шляхом до .csv файлу з даними.
# Файл включає в себе три колонки:
# код товару (текст),
# назва категорії товару (текст),
# доступність товару для продажу (текст (0 або 1)).
#
# На вихід функція повинна повернути список кортежів, кожен з яких складається з трьох елементів:
# назва категорії,
# кількість товарів даної категорії загалом,
# кількість товраів даної категорії доступних для продажу.
#
# Результуючий список повинен бути відсортований за зростанням по назві категорії
#
# Заголовок у файлі може бути присутнім, а може і не бути.
#
# Приклад вхідного файлу:
#
# product_code,categ_id.complete_name,Is Sellable
# T-00012165,Товары / МБТ / Пылесосы,0
# T-00011859,Товары / МБТ / Мультиварки,0
# T-00009681,Товары / МБТ / Кухонные комбайны,0
# T-00000129,Товары / КТ,1
# T-00011684,Товары / МБТ / Электрочайники,1
# T-00009682,Товары / МБТ / Кухонные комбайны,0
# T-00009630,Товары / МБТ / Блендеры,0
# T-00011207,Товары / МБТ / Электрочайники,1


import csv
from collections import defaultdict


def category_stat(data_file):
    res = defaultdict(lambda *a, **k: defaultdict(int))

    def process_row(cat, sellable):
        res[cat]['total_products'] += 1
        if sellable == '1':
            res[cat]['sellable_products'] += 1

    with open(data_file, 'r', 1, 'utf-8') as f:
        reader = csv.reader(f)
        row = next(reader)

        # if row is header
        if row[-1] in ('0', '1'):
            _, cat, sellable = row
            process_row (cat, sellable)

        for _, cat, sellable in reader:
            process_row(cat, sellable)

    return [
        (cat, res[cat]['total_products'], res[cat]['sellable_products'])
        for cat in sorted(list(res))
    ]


stat = category_stat('category_stat_1.csv')
print('\n'.join(str(i) for i in stat))