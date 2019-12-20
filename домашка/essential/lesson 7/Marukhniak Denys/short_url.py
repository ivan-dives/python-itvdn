URLS = {}


def add_new_url(url_add):
    global URLS
    short_name = abs(hash(url_add))
    tmp = {short_name: url_add}
    URLS.update(tmp)


def found_by_short(short):
    global URLS
    tmp = URLS.get(int(short[14:]), 'Short url is not created')
    return tmp


def get_short(url):
    global URLS
    short = abs(hash(url))
    tmp = URLS.get(short, 'Short url is not created')
    short_url = 'short_url.biz/' + str(short)
    return short_url
