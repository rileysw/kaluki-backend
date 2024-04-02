from table import Table

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

    def get_ready_players(self):
        return self._table.get_players()

    def start_game(self):
        pass
