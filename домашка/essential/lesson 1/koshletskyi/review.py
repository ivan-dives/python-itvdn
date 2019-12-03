#!/usr/bin/python3
# -*- coding: utf-8 -*_

class Review:

    def __init__(self, review=None):
        self.review = review

    def __str__(self):
        return self.review or "No review on this book"