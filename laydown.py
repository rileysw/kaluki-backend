from collections import deque
from card import Card


class Laydown:
    def __init__(self, cards: list):
        self._laydown = deque(cards)

    def get(self):
        return self._laydown

    def add(self, index: int, card: Card):
        self._laydown.insert(index, card)

    def replace(self, index: int, card: int):
        temp = self._laydown[index]
        self._laydown[index] = card
        return temp
