class Item:
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight} kg)"
    
    blaze_rod = ("blaze rod", "Petit batôn provenant d'un blaze", 1)
    stick = ("stick", "Petit batôn provenant d'un arbre", 1)
    diamond = ("diamond", "Pierre précieuse de couleurs bleu", 1)
    iron = ("iron", "Lingot de fer provenant de la roche", 1)
    ender_pearles = ("ender pearles", "Oeil hanté ayant des caractéristique mystique...", 1)
    ender_eyes = ("ender eyes", "La fusion d'un batôn de blaze et d'une ender eyes", 1)
    iron_pickaxe = ("iron pickaxe", "Pioche permettant d'extraire le diamand", 1)
    diamond_sword = ("diamond sword", "Epée solide permettant de se défendre", 1)
    iron_sword = ("iron sword", "Epée permettant de se défendre", 1)
    wood_pickaxe = ("wood pickaxe", "Pioche en bois permettant d'extraire l'iron de la roche", 1)
    iron_armor = ("iron armor", "Armure forgée à l'aide d'iron", 1)
    diamond_armor = ("diamond armor", "Armure forgée à l'aide de diamond", 1)