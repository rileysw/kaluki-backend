from card import Card
from laydown import Laydown

class Player:
    def __init__(self, name: str):
        self._name = name
        self._hand = []
        self._laydowns = []

    def get_name(self):
        return self._name
    
    def get_hand(self):
        return self._hand
    
    def add_to_hand(self, index: int, card: Card):
        self._hand.insert(index, card)

    def swap_cards(self, index1: int, index2: int):
        temp = self._hand[index1]
        self._hand[index1] = self._hand[index2]
        self._hand[index2] = temp

    def remove_from_hand(self, index: int):
        self._hand.pop(index)

    def get_laydowns(self):
        return self._laydowns
    
    def add_to_laydowns(self, laydown: Laydown):
        return self._laydowns.append(laydown)