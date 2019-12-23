import json

URL_SHORT_LINK = "http//srt.lnk."


def get_data(x):
    with open("db.json", "r") as f:
        f = json.load(f)
        data = f.get(x)
        return data


def put_data(x):
    with open("db.json", "r") as f:
        d = dict(json.load(f))
        d.update(x)
        with open("db.json", "w") as file:
            json.dump(d, file)


def put_default_data(x):
    with open("db.json", "r") as f:
        d = dict(json.load(f))
        d.update(x)
        with open("db.json", "w") as file:
            json.dump(d, file)
