'''
Author : Carvalho Allan & Brault Oscar
'''

class Item:
    '''
    Classe Item pour définir les items
    '''
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight} kg)"

    # Création des items
diamond_sword = Item("épée en diamant", "une épée au fil tranchant comme un rasoir", 2)
iron_sword = Item("épée en fer", "une épée solide et bien équilibrée", 2.5)
diamond_ore = Item("minerai de diamant", "un minerai avec une solidité exceptionnelle", 1)
iron_ore = Item("minerai de fer", "un minerai fiable et résistante", 0.5)
blaze_rod = Item("Blaze rod", "un bâton particulier qui nous servira plus tard", 0.3)
