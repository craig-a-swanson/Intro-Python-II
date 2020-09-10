# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    
    # def _set_n_to(self, room):
    #     self._n_to = room
    # def _get_n_to(self):
    #     return self._n_to
    # n_to = property(_get_n_to, _set_n_to)
    
    def __str__(self):
        output = f"Your current location is: {self.name}.\n{self.description}\n"

        for item in self.items:
            output += f"{item}\n"
        
        return output