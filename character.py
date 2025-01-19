# Définition de la classe Character
'''
Author Carvalho Allan & Brault Oscar
'''
class Character:
    '''
    La classe Character permet d'établir la manière dont
    un PNJ pourra interargir dans le monde ( ses actions ... )
    '''
    def __init__(self, name, description, current_room=None, msgs=None):
        """
        Initialise un nouveau personnage non joueur.

        Args:
            name (str): Le nom du personnage.
            description (str): Une description du personnage.
            current_room (Room, optional): La pièce actuelle du personnage. Par défaut, None.
            msgs (list, optional): Liste des messages que le personnage peut dire. Par défaut, None.
        """
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs if msgs is not None else []

    def __str__(self):
        """
        Retourne une représentation textuelle du personnage.

        Returns:
            str: Une chaîne sous la forme "Nom : description".
        """
        return f"{self.name} : {self.description}"


    def get_msg(self):
        """
        Retourne un message cyclique associé au personnage.

        Returns:
            str: Un message du personnage.
        """
        if not self.msgs:
            return f"{self.name} n'a rien à dire pour le moment."

        # Retourne et réinsère le message à la fin de la liste
        message = self.msgs.pop(0)
        self.msgs.append(message)
        return message
