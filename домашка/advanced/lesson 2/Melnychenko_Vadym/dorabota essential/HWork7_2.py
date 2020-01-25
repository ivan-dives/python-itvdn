
from urllib.parse import urlparse

class LinksDB(object):


    def __init__(self):

        self._links = {}  # словарь ссылок

    def get_url(self, name):


        return self._links[name]

    def set_url(self, name, url):

        url = self.normalize_url(url)

        if not name:
            raise KeyError('Link name cannot be empty', name)
        if not url:
            raise ValueError('Invalid link URL', url)
        if name in self._links:
            raise KeyError('Link already exists', name)

        self._links[name] = url

    def normalize_url(self, url):
        if not urlparse(url).scheme:
            url = 'http://' + url
        if urlparse(url).netloc:
            return url
        else:
            return None
