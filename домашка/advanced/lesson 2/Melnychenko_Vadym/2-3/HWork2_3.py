import csv


def csv_writer(path, fieldnames, data):
    with open(path, "w", newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


if __name__ == "__main__":
    data = [['programming language', 'student name', 'knowledge level'],
            ['Python', 'Ivan', '80'],
            ['Python', 'Vadym', '2'],
            ['Python', 'Petr', '7']]

    my_list = []
    fieldnames = data[0]
    cell = data[1:]
    for values in cell:
        inner_dict = dict(zip(fieldnames, values))
        my_list.append(inner_dict)

    path = "dict_output.csv"
    csv_writer(path, fieldnames, my_list)
