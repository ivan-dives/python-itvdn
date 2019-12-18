container = {
    "https://docs.python.org/3/library/index.html": "https://goo-gl.su/python"
}


# def add_base(*kwargs):
#     container.update({kwargs})
#     return container


row1 = "google"
row2 = "goooooogle"
# add_base(row1, row2)
container[row1] = row2

print(container)
