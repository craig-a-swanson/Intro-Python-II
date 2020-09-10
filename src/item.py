

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f'{self.name}: {self.description}\n'


class Light(Item):
    def __init__(self, name, description, luminosity, longevity):
        super().__init__(name, description)
        self.luminosity = luminosity
        self.longevity = longevity
    
    def __str__(self):
        base_string = super().__str__()
        return f'{base_string}\tLuminosity: {self.luminosity}\n\tLongevity: {self.longevity}\n'

class Reference(Item):
    def __init__(self, name, description, size):
        super().__init__(name, description)
        self.size = size
    
    def __str__(self):
        base_string = super().__str__()
        return f'{base_string}\tSize: {self.size}'





# Possible Items to find
torch = Light("Torch", "Oil soaked rags on a stick", 3, 2)
lantern = Light("Handheld Lantern", "A moderately sized plastic and metal, battery powered lantern", 5, 7)
flashlight = Light("Flashlight", "Handheld metal cylinder with an LED bulb", 7, 8)
spellbook = Reference("Book of Spells", "A large reference manual containing all sorts of chants and stuff", 10)
level_map = Reference("Area Map", "A detailed paper map of current surronding area", 2)
large_map = Reference("Large Map", "A detailed, multi-page map of a large swath of areas", 5)
