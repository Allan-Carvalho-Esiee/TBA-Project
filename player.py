# Définition de la classe Player
'''
Author : Carvalho Allan & Brault Oscar
'''

from item import Item

class Player:
    '''
    Classe Player
    '''
    def __init__(self, name):
        """
        Initialise un nouveau joueur.

        Args:
            name (str): Le nom du joueur.
        """
        self.name = name
        self.current_room = None  # La pièce actuelle du joueur
        self.history = []  # Historique des pièces visitées
        self.inventory_player ={} #{"diamond_sword" : Item("épée en diamant", "une épée au fil tranchant comme un rasoir", 2)}
        self.max_poids = 15
        self.equipped_weapon = None  # Arme équipée par défaut
        self.health = 20  # Points de vie du joueur

    def move(self, direction):
        """
        Déplace le joueur dans la direction spécifiée et met à jour l'historique.

        Args:
            direction (str): La direction vers laquelle le joueur veut se déplacer.

        Returns:
            bool: True si le déplacement a réussi, False sinon.
        """
        # Vérifie s'il existe une sortie pour cette direction
        next_room = self.current_room.exits.get(direction)
        if next_room is None:
            print("\nAucune possibilitée dans cette direction !\n")
            return False

        # Ajoute la pièce actuelle à l'historique avant de se déplacer
        self.history.append(self.current_room)

        # Change la pièce actuelle
        self.current_room = next_room
        print(self.current_room.get_long_description())

        # Affiche l'historique après le déplacement
        print(self.get_history())
        return True

    def get_history(self):
        """
        Retourne une chaîne de caractères représentant les pièces déjà visitées.

        Returns:
            str: Une chaîne formatée listant les noms des pièces visitées.
        """
        if not self.history:  # Si l'historique est vide
            return "Vous n'avez encore visité aucune pièce."

        visited_rooms = list(room.name for room in self.history)

        # Construit la chaîne formatée
        history_text = "Vous avez déjà visité les pièces suivantes:\n"
        for name in visited_rooms:
            history_text += f"    - {name}\n"

        return history_text


    def get_inventory(self): #Joueur
        """
        Retourne une chaîne de caractères représentant l'inventaire du joueur.

        Returns:
            str: Une chaîne formatée listant l'inventaire'
        """
        if not self.inventory_player : # Si l'inventaire est vide
            return "Votre inventaire est vide."

        inventory_list = ["Vous disposez des items suivants :"]
        for item in self.inventory_player.values():
            inventory_list.append(f"    - {item}")
        return "\n".join(inventory_list)  # Retourne la chaîne formatée

    def equip_weapon(self, weapon_name):
        """
        Équipe une arme de l'inventaire du joueur.

        Args:
            weapon_name (str): Le nom de l'arme à équiper.

        Returns:
            str: Message confirmant ou non l'équipement.
        """
        # Utilisation de inventory_player au lieu de inventory
        if weapon_name in self.inventory_player:
            self.equipped_weapon = self.inventory_player[weapon_name]
            return f"Vous avez équipé {self.equipped_weapon.name}."
        return "Cette arme n'est pas dans votre inventaire."

    def attack(self, monster):
        """
        Attaque un monstre.

        Args:
            monster (Monster): Le monstre à attaquer.

        Returns:
            str: Résultat de l'attaque.
        """
        if self.equipped_weapon:
            damage = self.equipped_weapon.weight
        else:
            damage = 1  # Dégâts par défaut si aucune arme n'est équipée

        monster.health -= damage

        if monster.health <= 0:
            if monster.name == "Ender Dragon":
                print(f"\nVous avez tué le {monster.name} ! Vous avez gagné !")
            else :
                return f"Vous avez vaincu le {monster.name} !"
        return f"Vous avez infligé {damage} de dégâts au {monster.name}. Il lui reste {monster.health} PV."