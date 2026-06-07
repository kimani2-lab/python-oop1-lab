#!/usr/bin/env python3

class Coffee:
    def __init__(self, size: str, price: float):
        # Use setters to validate input structures
        self.size = size
        self.price = price

    @property
    def size(self) -> str:
        return self._size

    @size.setter
    def size(self, value: str):
        valid_sizes = ["Small", "Medium", "Large"]
        formatted_value = str(value).capitalize()

        if formatted_value not in valid_sizes:
            print("size must be Small, Medium, or Large")
            return
        self._size = formatted_value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            print("price must be a number")
            return
        self._price = float(value)

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1.0
