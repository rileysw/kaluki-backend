from card import Card
from laydown import Laydown


class Player:
    def __init__(self, name: str):
        self._name = name
        self._has_drawn = False
        self._hand = []
        self._laydowns = []

    def get_name(self):
        return self._name

    def get_has_drawn(self):
        return self._has_drawn

    def set_has_drawn(self, has_drawn: bool):
        self._has_drawn = has_drawn

    def get_hand(self):
        return self._hand

    def set_hand(self, hand: list):
        self._hand = hand

    def add_to_hand(self, index: int, card: Card):
        self._hand.insert(index, card)

    def swap_cards(self, index1: int, index2: int):
        temp = self._hand[index1]
        self._hand[index1] = self._hand[index2]
        self._hand[index2] = temp

    def remove_from_hand(self, card_id: int):
        for card in self._hand:
            if card.get_id() == card_id:
                self._hand.remove(card)
                return card

    def get_laydowns(self):
        return self._laydowns

    def add_to_laydowns(self, laydown: Laydown):
        return self._laydowns.append(laydown)
