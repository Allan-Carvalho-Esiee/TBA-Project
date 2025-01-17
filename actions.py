# Description: The actions module.
'''
Author : Carvalho Allan & Brault Oscar
'''
# Import modules
import random
from item import Item

DEBUG = True
# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1
# variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"





class Actions:
    '''
    La classe Actions permet d'établir la manière dont
    le joueur pourra interargir dans le monde 
    '''
    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction
        ( N, E, S, O ) or vertical direction ( Up and Down ).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """

        Direction_Map = {"N": "N", "NORD": "N", "E": "E", "EST": "E", "S":
                        "S", "SUD": "S", "O": "O", "OUEST": "O", "UP": "UP",
                        "HAUT": "UP", "DOWN": "DOWN", "BAS": "DOWN"}


        player = game.player

        # Nettoyage de l'entrée pour supprimer les espaces inutiles
        list_of_words = [word.strip() for word in list_of_words if word.strip()]

        list = len(list_of_words)

        # If the number of parameters is incorrect, print an error message and return False.
        if list != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Récupération de la direction saisie et normalisation et
        # Conversion en majuscules pour correspondre aux clés du dictionnaire
        input_direction = list_of_words[1].upper()


        # Vérifier si l'entrée correspond à une direction valide via le mappage
        direction = Direction_Map.get(input_direction)
        if not direction:
            print(f"\nLa direction '{list_of_words[1]}' n'est pas valide. Commandes possibles : go ' N, S, E, O, Up, Down '\n")
            return False

        # Vérification si une sortie existe pour cette direction
        if direction not in player.current_room.exits or player.current_room.exits[direction] is None:
            print(f"\nImpossible d'aller dans la direction '{direction}' depuis ici. Mettez des lunettes...\n")
            return False

        # Déplacement réussi
        player.move(direction)
        return True

    def back(game, list_of_words, number_of_parameters):
        """
        Return the player to the previous action.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        list = len(list_of_words)
        if list != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Vérifier si le joueur a un historique d'actions
        if len(game.player.history) > 0: 
            previous_location = game.player.history.pop()  # Obtenir la dernière location
            game.player.current_room = previous_location  # Revenir à la location précédente
            print(f"\nVous êtes retourné à : {previous_location}")  # Afficher la représentation de la salle
            print(game.player.get_history())
            return True
        print("Euh ?? Vous êtes déjà au début... vous ne pouvez pas mieux faire.. AH SI ! fermer le jeu ;)")
        return False

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    def history(game, list_of_words, number_of_parameters):
        """
        Affiche l'historique des actions du joueur.

        Print the list of available commands.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Afficher l'historique
        print(game.player.get_history())
        print()
        return True

    def check(game, list_of_words, number_of_parameters):
        """
        Affiche l'inventaire du joueur.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Afficher l'inventaire
        print(game.player.get_inventory())
        print()
        return True

    def look(game, list_of_words, number_of_parameters):
        """
        Affiche les items dans la pièce.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Afficher l'inventaire
        print(game.player.current_room.get_inventory())
        print()
        return True

    def take(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de prendre un item dans la pièce où il se trouve.
        Ajoute l'item dans l'inventaire du joueur et le retire de la pièce.

        Args:
            game (Game): Le jeu en cours.
            list_of_words (list): Les mots de la commande, ex: ['take', 'item_name'].
            number_of_parameters (int): Le nombre de paramètres attendus.
        """
        # Vérifier que le joueur a bien spécifié un item à prendre
        if len(list_of_words) < 2:
            print("Précisez quel objet vous voulez prendre.")
            return

        # Obtenir le nom de l'item
        item_name = list_of_words[1]

        # Vérifier si l'item est présent dans la pièce actuelle
        current_room_inventory = game.player.current_room.inventory_room
        if item_name not in current_room_inventory:
            print(f"L'objet '{item_name}' n'est pas dans la pièce.")
            return

        # Récupérer l'item depuis l'inventaire de la pièce
        item = current_room_inventory.pop(item_name)

        # Ajouter l'item à l'inventaire du joueur
        game.player.inventory_player[item_name] = item
        print(f"Vous avez pris {item_name} : {item}.")


    def drop(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de reposer un item dans la pièce où il se trouve.
        Retire l'item de l'inventaire du joueur et le remet dans la pièce.

        Args:
            game (Game): Le jeu en cours.
            list_of_words (list): Les mots de la commande, ex: ['drop', 'item_name'].
            number_of_parameters (int): Le nombre de paramètres attendus.
        """

        # Vérifier que le joueur a bien spécifié un item à déposer
        if len(list_of_words) < 2:
            print("Précisez quel objet vous voulez reposer.")
            return

        # Obtenir le nom de l'item
        item_name = list_of_words[1]

        # Vérifier si l'item est présent dans l'inventaire du joueur
        player_inventory = game.player.inventory_player
        if item_name not in player_inventory:
            print(f"L'objet '{item_name}' n'est pas dans votre inventaire\n")
            return

        # Récupérer l'item depuis l'inventaire du joueur
        item = player_inventory.pop(item_name)

        # Ajouter l'item à l'inventaire de la pièce
        game.player.current_room.inventory_room[item_name] = item

        print(f"Vous avez reposé {item_name} : {item}.\n")


    def move(self, list_of_words, number_of_parameters):
        """
        Déplace le personnage non joueur vers une pièce adjacente
        avec une probabilité de 50%.

        Returns:
            bool: True si le personnage s'est déplacé, False sinon.
        """
        if random.choice([True, False]):  # 50% de chance de déplacement
            exits = list(self.player.current_room.exits.values())
            if exits:  # Vérifie s'il y a des pièces adjacentes
                new_room = random.choice(exits)
                self.player.current_room.characters.pop(self.character.name)  # Retire le personnage de l'ancienne salle
                self.player.current_room = new_room
                self.player.current_room.characters[self.character.name] = self  # Ajoute le personnage dans la nouvelle salle

                if DEBUG:
                    print(f"DEBUG: {self.character.name} s'est déplacé vers {self.player.current_room.name}.")
                return True
        if DEBUG:
            print(f"DEBUG: {self.character.name} est resté dans {self.player.current_room.name}.")
        return False
        
    def talk(game, list_of_words, number_of_parameters):
        """
        Interagit avec un PNJ mentionné dans la commande.

        Args:
            game (Game): L'objet du jeu.
            list_of_words (list): Les mots de la commande.
            number_of_parameters (int): Le nombre de paramètres attendus.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Vérifier si un PNJ est mentionné
        pnj_name = list_of_words[1]
        current_room = game.player.current_room

        # Rechercher le PNJ dans la pièce
        pnj = current_room.characters.get(pnj_name)
        if not pnj:
            print(f"Il n'y a pas de personnage nommé '{pnj_name}' ici.")
            return False

        # Appeler la méthode get_msg() du PNJ
        print(pnj.get_msg())
        player_inventory = game.player.inventory_player

        if current_room.characters.get("villageois"):
            action = input("\nQue voulez-vous faire ? (trade/partir) : ").strip().lower()
            if action == "trade":
                print("\nVoici la liste de mes échanges : ")
                exchanges = {
                    "diamant": ("épée_en_diamant", "une épée au fil tranchant comme un rasoir", 3),
                    "fer": ("épée_en_fer", "une épée tranchante", 2),
                    "stick": ("arc", "un bâton relié avec un fil permettant de tirer des flèches", 4),
                    "blazerod": ("œil_maudit", "un objet bien mystérieux...", 1)
                }

                for key, (name, desc, _) in exchanges.items():
                    print(f"- {key.capitalize()} contre {name}")

                item_choice = input("\nQue voulez-vous échanger ? (diamant/fer/stick/blazerod/rien) : ").strip().lower()

                if item_choice in exchanges:
                    if item_choice in player_inventory:
                        item_name, item_desc, item_value = exchanges[item_choice]
                        player_inventory.pop(item_choice)
                        player_inventory[item_name] = Item(item_name, item_desc, item_value)
                        print(f"Vous avez reçu {item_name}.")
                        return True
                    else:
                        print(f"Vous n'avez pas de {item_choice} pour échanger.")
                        return False
                elif item_choice == "rien":
                    print("Vous avez choisi de ne rien échanger.")
                    return True
                else:
                    print("Action invalide. Essayez 'diamant', 'fer', 'stick', 'blazerod' ou 'rien'.")
                    return False

            elif action == "partir":
                print("Vous partez !\n")
                return True
            else:
                print("Action invalide. Essayez 'trade' ou 'partir'.")
                return False

        return True
    
    def equip(game, list_of_words, number_of_parameters):
        """
        Équipe une arme du joueur.

        Args:
            game (Game): L'objet du jeu.
            list_of_words (list): Liste des mots de la commande.
            number_of_parameters (int): Nombre de paramètres attendus par la commande.

        Returns:
            bool: True si la commande a été exécutée avec succès, False sinon.
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        weapon_name = list_of_words[1]
        # Appel de equip_weapon
        message = game.player.equip_weapon(weapon_name)
        print(message)
        return True
    
    def combat(game, list_of_words, number_of_parameters):
        """
        Lance un combat tour par tour entre le joueur et un monstre.

        Args:
            game (Game): L'objet du jeu.
            list_of_words (list): Les mots de la commande, ex: ['combat', 'monster_name'].
            number_of_parameters (int): Le nombre de paramètres attendus.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        # Vérification du nombre de paramètres
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Récupérer le nom du monstre
        monster_name = list_of_words[1]
        current_room = game.player.current_room

        # Vérifier si le monstre existe dans la pièce actuelle
        monster = current_room.characters.get(monster_name)
        if not monster:
            print(f"Il n'y a pas de monstre nommé '{monster_name}' ici.")
            return False

        print(f"\nVous entrez en combat avec un {monster.name} !")
        player = game.player

        # Boucle du combat
        while player.health > 0 and monster.health > 0:
            # Tour du joueur
            action = input("\nQue voulez-vous faire ? (attaquer/fuir) : ").strip().lower()
            if action == "attaquer":
                damage = player.attack(monster)  # les dégâts infligés
                print(f"\n{damage}")  # Affiche le résultat ici
            elif action == "fuir":
                print("Vous fuyez le combat !\n")
                return True
            else:
                print("Action invalide. Essayez 'attaquer' ou 'fuir'.")
                continue

            # Vérifier si le monstre est mort
            if monster.health <= 0:
                if monster.name == "Dragon":
                    print(f"Vous avez gagné les habitants sont enfin sauvés !")
                    print(f"Merci d'avoir joué ! ^^\n")
                    print(f"##########################################################")
                    game.finished = True
                else : 
                    print(f"")
                current_room.characters.pop(monster.name)  # Retirer le monstre de la pièce
                return True

            # Tour du monstre
            damage = monster.attack(player)  # Passer le joueur à la méthode attack
            print(f"{damage}")

        # Résultat du combat
        if player.health <= 0:
            print("\nLe jeu est terminé.\n")
            print("##########################################################")
            game.finished = True
        return True
