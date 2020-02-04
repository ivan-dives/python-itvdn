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


def category_stat(data_file):
    cat_dict = {}
    with open(data_file, 'rt', 1, 'utf-8') as file:
        for curr_ln in file:
            lst_curr = curr_ln.split(sep=",")
            if len(lst_curr) < 3:
                continue
            try:
                enable_curr = int(lst_curr[2])
            except ValueError:
                continue
            cat_curr = lst_curr[1]
            inf_curr = cat_dict.setdefault(cat_curr, (0,0))
            cat_dict[cat_curr] = (inf_curr[0]+1, inf_curr[1]+enable_curr)

    res_lst = []
    keys_lst = list(cat_dict.keys())
    keys_lst.sort()
    for k in keys_lst:
        c_val = cat_dict.get(k)
        res_lst.append((k, c_val[0], c_val[1]))
    return res_lst


stat = category_stat('category_stat_1.csv')
print('\n'.join(str(i) for i in stat))