from table import Table
from card import Card

class Kaluki:
    def __init__(self):
        self._table = None

    def has_table(self):
        return self._table != None

    def add_player(self, name: str):
        if self._table == None:
            self._table = Table(name)
        else:
            self._table.add_player(name)

    def remove_player(self, name: str):
        self._table.remove_player(name)

    def get_player_names(self):
        return [player.get_name() for player in self._table.get_players()]

    def start_game(self):
        self._table.create_deck()
        self._table.shuffle_deck()
        self._table.deal_cards()

        # test
        for player in self._table.get_players():
            print("player: ", player.get_name())
            print("size: ", len(player.get_hand()))
            print("hand: ", player.get_hand())

    def get_player_hand(self, name: str):
        for player in self._table.get_players():
            if player.get_name() == name:
                return [(card.get_name(), card.get_value(), card.get_id()) for card in player.get_hand()]

    def update_player_hand(self, name: str, hand: list):
        for player in self._table.get_players():
            if player.get_name() == name:
                player.set_hand([Card(card[0], card[1], card[2]) for card in hand])
                break

    def draw_card(self, name: str):
        for player in self._table.get_players():
            if player.get_name() == name:
                if len(player.get_hand()) == 15:
                    raise ValueError("Hand already has 15 cards.")
                else:
                    player.add_to_hand(len(player.get_hand()), self._table.remove_from_deck())
                    break

    def trash_card(self, name: str, index: int):
        for player in self._table.get_players():
            if player.get_name() == name:
                trash_card = player.remove_from_hand(index)
                self._table.add_to_trash(trash_card)
                return [trash_card.get_name(), trash_card.get_value(), trash_card.get_id()]
