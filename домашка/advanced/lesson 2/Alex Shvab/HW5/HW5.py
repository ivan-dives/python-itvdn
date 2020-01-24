import sqlite3


class RowSet:
    def __init__(self):
        # инициализируем контейнер
        self.rows = set()

    def step(self, value):
        # добавляем элемент в контейнер
        self.rows.add(value)

    def finalize(self):
        # завершение агрегации
        return ';'.join(self.rows)
# def conc(row):
#     return row + ";"

conn = sqlite3.connect("mydb.sqlite3")
conn.create_aggregate("concat", 1, RowSet)
cur = conn.cursor()

cur.execute('CREATE TABLE "material"(id, mat_name VARCHAR , weight REAL, height REAL, add_character)')
cur.execute(
    """INSERT INTO material(id, mat_name, weight, height, add_character)
       VALUES (1,"Brus", 5.2, 1, "[('width', 3), ('netto', 0.8)]"),
              (2, "Metal", 3, 5.2, "[('width', 2), ('netto', 0.2)]"),
              (3, "Car", 1000, 1.5, "[('wheels', 4), ('passengers', 5)]")
    """
)

cur.execute('SELECT concat(mat_name) FROM material')
row = cur.fetchall()
print(row)

conn.close()