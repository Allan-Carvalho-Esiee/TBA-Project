# Définition de la classe Player

class Player:
    def __init__(self, name):
        """
        Initialise un nouveau joueur.

        Args:
            name (str): Le nom du joueur.
        """
        self.name = name
        self.current_room = None  # La pièce actuelle du joueur
        self.history = []  # Historique des pièces visitées
        self.inventory_player = {}  # Dictionnaire pour l'inventaire

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

        else:
            inventory_list = ["Vous disposez des items suivants :"]
            for item in self.inventory_player.values():
                inventory_list.append(f"    - {item}")
            return "\n".join(inventory_list)  # Retourne la chaîne formatée