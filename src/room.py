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
    
    
    def __str__(self):
        output = f"Your current location is: {self.name}.\n{self.description}\n"

        if len(self.items) > 0:
            output += f"\nThere are {len(self.items)} items that you notice\n"
        for item in self.items:
            output += f"{item}\n"
        
        return output