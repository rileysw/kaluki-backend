from card import Card

class Table:
    def __init__(self, player: str):
        self._players = [player]
        self._deck = []
        self._trash = []
    
    def get_players(self):
        return self._players
    
    def add_player(self, player: str):
        if player in self._players:
            raise ValueError("Player already exists.")
        else:
            self._players.append(player)

    def remove_player(self, player: str):
        self._players.remove(player)

    def set_deck(self):
        # initialize deck with cards
        pass

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
