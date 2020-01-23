import sqlite3

conn = sqlite3.connect("mydb.sqlite3")

conn.execute('CREATE TABLE "material"(id, weight REAL, height REAL, add_character)')
conn.execute(
    """INSERT INTO material(id, weight, height, add_character)
       VALUES (1, 5.2, 1, "[('width', 3), ('netto', 0.8)]"),
              (2, 3, 5.2, "[('width', 2), ('netto', 0.2)]"),
              (3, 1000, 1.5, "[('wheels', 4), ('passengers', 5)]")
    """
)

mat = conn.execute('SELECT * FROM "material"').fetchall()
print(mat)
print()

res = conn.execute('SELECT AVG(weight) FROM "material"').fetchone()
avg = int(res[0])
print(f"AVG={avg}")

conn.close()