class Card:
    def __init__(self, name: str, value: int):
        self._name = name
        self._value = value
    
    def get_name(self):
        return self._name
    
    def get_value(self):
        return self._value
    
    def set_value(self, value: int):
        self._value = value
