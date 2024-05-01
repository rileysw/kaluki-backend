class Card:
    id_counter = 0

    def __init__(self, name: str, value: int, id: int = None):
        if id == None:
            self._id = Card.id_counter
            Card.id_counter += 1
        else:
            self._id = id
        self._name = name
        self._value = value

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_value(self):
        return self._value

    def set_value(self, value: int):
        self._value = value
