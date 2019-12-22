URLS = {}


def found_by_short(short):
    global URLS
    tmp = URLS.get(int(short[14:]), 'Short url is not created')
    return tmp


def add_n_get(url):
    global URLS
    short = abs(hash(url))
    URLS.setdefault(short, url)
    return 'short_url.biz/' + str(short)
