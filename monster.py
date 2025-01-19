class Monster:
    """
    Classe représentant un monstre.
    """

    def __init__(self, name, description, health, damage, current_room=None):
        """
        Initialise un nouveau monstre.

        Args:
            name (str): Le nom du monstre.
            health (int): Points de vie du monstre.
            damage (int): Dégâts infligés par le monstre.
            current_room (Room, optional): La pièce actuelle du monstre. Par défaut, None.
        """
        self.name = name
        self.description = description
        self.health = health
        self.damage = damage
        self.current_room = current_room

    def attack(self, player):
        """
        Attaque le joueur.

        Args:
            player (Player): Le joueur à attaquer.

        Returns:
            str: Résultat de l'attaque.
        """
        player.health -= self.damage

        if player.health <= 0:
            return f"{self.name} vous a tué ! Vous avez perdu..."
        return f"{self.name} vous a infligé {self.damage} dégâts. Il vous reste {player.health} PV."

    def take_damage(self, amount):
        """
        Réduit la santé du monstre en fonction des dégâts reçus.

        Args:
            amount (int): Dégâts reçus.
        """
        amount = int(amount)
        self.health -= amount
        if self.health < 0:
            self.health = 0  # Empêche la santé d'être négative