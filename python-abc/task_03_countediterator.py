#!/usr/bin/env python3


"""module that contains class"""


class CountedIterator:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.count = 0

    def __next__(self):
        try:
            next_item = next(self.iterable)
            self.count += 1
            return next_item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        return self.count