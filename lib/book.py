#!/usr/bin/env python3

class Book:
    def __init__(self, title: str, page_count: int, author: str = None):
        self.title = title
        self.author = author
        self.current_page = 0
        # Use the setter property to apply validation on creation
        self.page_count = page_count

    @property
    def page_count(self) -> int:
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            return
        self._page_count = value

    def turn_page(self):
        if self.current_page < self.page_count:
            self.current_page += 1
        print("Flipping the page...wow, you read fast!")

    def read(self, pages: int = 1):
        for _ in range(pages):
            self.turn_page()
