from src.index import store

class Customer:
    def __init__(self, first_name = str, last_name = str):
        self._first_name = first_name.upper()
        self._last_name = last_name.upper()
        self.id = len(store['customers']) + 1
        store['customers'][self.id] = self

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name.upper()

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name.upper()