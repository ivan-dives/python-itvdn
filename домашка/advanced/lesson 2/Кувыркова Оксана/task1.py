import json

pupil_dict = {"Name": "Bob", "Age": 24, "Groupp": 2}
book_dict = {"Name": "It", "Author": "King", "Genre": "Horror"}
grocery_dict = {"Name1": "apple", "Amount1": 2, "Name2": "Banana", "Amount2": 4}

with open('json_dict.txt', 'w') as outfile:
    pupil = json.dumps(pupil_dict)
    book = json.dumps(book_dict)
    grocery = json.dumps(grocery_dict)


with open('json_dict.txt') as json_file:
    loaded_pupil = json.loads(pupil)
    loaded_book = json.loads(book)
    loaded_grocery = json.loads(grocery)
    for data in loaded_pupil:
        print(loaded_pupil.keys(), loaded_pupil.values())
        print(loaded_book.keys(), loaded_book.values())
        print(loaded_grocery.keys(), loaded_grocery.values())
