# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
    
    # def _set_n_to(self, room):
    #     self._n_to = room
    # def _get_n_to(self):
    #     return self._n_to
    # n_to = property(_get_n_to, _set_n_to)
    
    def __str__(self):
        return f"Your current location is {self.name}.\n{self.description}"