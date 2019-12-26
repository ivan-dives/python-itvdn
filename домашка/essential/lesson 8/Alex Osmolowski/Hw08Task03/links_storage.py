"""Модуль основной логики приложения.
Предоставляет класс LinksSt -- хранилище ссылок.
"""

from urllib.parse import urlparse
import os.path
import shelve

class LinksSt():
    """Хранилище ссылок"""

    def __init__(self):
        """Конструктор класса"""

        self._st_name = os.path.join('database', 'links_st')

    def get_url(self, name):
        """Метод получения ссылки по имени.
        Выбрасывает KeyError, если имя не найдено."""

        with shelve.open(self._st_name) as st:
            return st[name]

    def set_url(self, name, url):
        """Метод добавления новой ссылки.
        Выбрасывает KeyError, если имя уже существует или пустое.
        Выбрасывает ValueError, если URL пустой или некорректный."""

        url = self.normalize_url(url)

        if not name:
            raise KeyError('Имя ссылки не может быть пустым', name)
        if not url:
            raise ValueError('Некорректный URL', url)

        with shelve.open(self._st_name) as st:
            if name in st:
                raise KeyError('Ссылка с таким именем уже существует', name)
            st[name] = url

    def normalize_url(self, url):
        """Метод, который добавляет протокол, если он отсутствует,
        и возвращает исправленный или исходный URL, если он корректный,
        или None в ином случае."""

        if not urlparse(url).scheme:
            url = 'http://' + url
        if urlparse(url).netloc:
            return url
        else:
            return None
