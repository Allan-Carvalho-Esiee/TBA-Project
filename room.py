# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory_room = {}  # Dictionnaire pour l'inventaire

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<Room(name={self.name})>"
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
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
    
    def get_inventory(self): #Room
        """
        Retourne une chaîne de caractères représentant l'inventaire de la pièce.

        Returns:
            str: Une chaîne formatée listant l'inventaire'
        """
        if not self.inventory_room : # Si l'inventaire est vide
            return "il n'y a rien ici"

        else:
            inventory_list = ["Vous disposez des items suivants :"]
            for item in self.inventory_room.values():
                inventory_list.append(f"    - {item}")
            return "\n".join(inventory_list)  # Retourne la chaîne formatée

