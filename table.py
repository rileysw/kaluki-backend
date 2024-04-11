import random
from card import Card
from player import Player

class Table:
    def __init__(self, name: str):
        self._players = [Player(name)]
        self._deck = []
        self._trash = []
    
    def get_players(self):
        return self._players
    
    def add_player(self, name: str):
        self._players.append(Player(name))

    def remove_player(self, name: str):
        self._players = [player for player in self._players if player.get_name() != name]

    def create_deck(self):
        def make_one_deck():
            one_deck = []
            for suit in ["spades", "clubs", "diamonds", "hearts"]:
                for i in range(2, 11):
                    one_deck.append(Card(str(i) + "_of_" + suit, i))
                for c in ["jack", "queen", "king"]:
                    one_deck.append(Card(c + "_of_" + suit, 10))
                one_deck.append(Card("ace_of_" + suit, None))
            one_deck.append(Card("black_joker", None))
            one_deck.append(Card("red_joker", None))
            return one_deck
        self._deck.extend(make_one_deck())
        self._deck.extend(make_one_deck())

    def shuffle_deck(self):
        random.shuffle(self._deck)

    def deal_cards(self):
        for _ in range(14):
            for player in self._players:
                player.add_to_hand(0, self._deck.pop())
        self._players[0].add_to_hand(0, self._deck.pop())

    def remove_from_deck(self):
        return self._deck.pop()
    
    def add_to_trash(self, card: Card):
        self._trash.append(card)

    def peek_trash(self):
        if len(self._trash) == 0:
            return None
        else:
            return self._trash[-1]
    
    def remove_from_trash(self):
        return self._trash.pop()
