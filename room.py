# Define the Room class.
'''
Author : Carvalho Allan & Brault Oscar
'''

class Room:
    '''
    La classe Room permet de définir le comportement
    d'une pièce
    '''
    # Define the constructor.
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {} # Dictionnaire des sorties disponibles
        self.inventory_room = {}  # Dictionnaire pour l'inventaire
        self.characters = {}  # Dictionnaire des personnages non joueurs

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<Room(name={self.name})>"

    # Define the get_exit method.
    def get_exit_string(self):
        exit_string = "Direction possibles : "
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string
        
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Direction possibles : "
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"


    def get_inventory(self):
        """
        Retourne une chaîne de caractères représentant l'inventaire de la pièce.

        Returns:
            str: Une chaîne formatée listant l'inventaire'
        """
        inventory_list = ["On peut voir ici :"]

        # Ajout des items présents dans la pièce
        if self.inventory_room:
            for item in self.inventory_room.values():
                inventory_list.append(f"    - {item.name} : {item.description} ({item.weight} kg)")
        else:
            inventory_list.append("    - Aucun item ici.")

        # Ajout des personnages présents dans la pièce
        if self.characters:
            for character in self.characters.values():
                inventory_list.append(f"    - {character.name} : {character.description}")
        else:
            inventory_list.append("    - Aucun personnage ici.")

        return "\n".join(inventory_list) 
