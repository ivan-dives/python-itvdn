import random
import string

full_url = {}
short_url = {}

def cut_link(long_link):
    short = (random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in
        range(random.randrange(5, 8)))
    short_link = "http://sashka/" + "".join(short)

    full_url[long_link] = short_link
    short_url[short_link] = long_link
    return short_link

def full_link(short_link):
    return short_url.get(short_link, "Incorrect link")