class Item:
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight} kg)"
    
    # Création des items
diamond_sword = Item("épée en diamant", "une épée au fil tranchant comme un rasoir", 2)
stone_sword = Item("épée en pierre", "une épée robuste mais basique", 3)
wooden_sword = Item("épée en bois", "une épée fragile mais légère", 1)
iron_sword = Item("épée en fer", "une épée solide et bien équilibrée", 2.5)

diamond_pickaxe = Item("pioche en diamant", "une pioche ultra résistante pour miner rapidement", 3)
stone_pickaxe = Item("pioche en pierre", "une pioche basique mais utile pour débuter", 4)
wooden_pickaxe = Item("pioche en bois", "une pioche simple mais fragile", 2)
iron_pickaxe = Item("pioche en fer", "une pioche efficace et robuste", 3.5)

diamond_armor = Item("armure en diamant", "une armure d'une solidité exceptionnelle", 10)
iron_armor = Item("armure en fer", "une armure fiable et résistante", 8)

diamond_ore = Item("minerai de diamant", "un minerai avec une solidité exceptionnelle", 1)
iron_ore = Item("minerai de fer", "un minerai fiable et résistante", 0.5)

blaze_rod = Item("Blaze rod", "un bâton particulier qui nous servira plus tard", 0.3)