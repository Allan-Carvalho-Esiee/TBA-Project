# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction ( N, E, S, O ) or vertical direction ( Up and Down ).

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

        l = len(list_of_words)
        
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        # Récupération de la direction saisie et normalisation
        input_direction = list_of_words[1].upper()  # Convertir en majuscules pour correspondre aux clés du dictionnaire

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
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Vérifier si le joueur a un historique d'actions
        if len(game.player.history) > 0:  # Assurez-vous d'accéder à l'historique du joueur via l'objet game
            previous_location = game.player.history.pop()  # Obtenir la dernière location
            game.player.current_room = previous_location  # Revenir à la location précédente
            print(f"\nVous êtes retourné à : {previous_location}")  # Afficher la représentation de la salle
            print(game.player.get_history())
            return True
        else:
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
    
    # Fonction 'take' pour prendre un item de la pièce et l'ajouter à l'inventaire du joueur
    def take(game, list_of_words, number_of_parameters):
        """
        Prend un item dans la pièce où le joueur se trouve et l'ajoute à son inventaire.

        Args:
            game (Game): L'objet du jeu.
            list_of_words (list): La liste des mots dans la commande (doit contenir l'item à prendre).
            number_of_parameters (int): Le nombre de paramètres attendus (1 paramètre - l'item à prendre).

        Returns:
            bool: True si la commande a été exécutée avec succès, False sinon.
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))  # Affichage de l'erreur si le nombre de paramètres est incorrect
            return False

        # Vérifier que l'item existe dans l'inventaire de la pièce
        item_name = list_of_words[1]
        player = game.player
        item = next((item for item in player.current_room.inventory if item.name == item_name), None)

        if not item:
            print(f"\nL'objet '{item_name}' n'est pas dans cette pièce.\n")
            return False

        # Ajouter l'item à l'inventaire du joueur
        player.inventory.append(item)
        # Retirer l'item de l'inventaire de la pièce
        player.current_room.inventory.remove(item)

        print(f"\nVous avez pris l'objet '{item_name}' et l'avez ajouté à votre inventaire.\n")
        return True

    # Fonction 'drop' pour reposer un item dans la pièce
    def drop(game, list_of_words, number_of_parameters):
        """
        Repose un item dans la pièce où le joueur se trouve et l'enlève de son inventaire.

        Args:
            game (Game): L'objet du jeu.
            list_of_words (list): La liste des mots dans la commande (doit contenir l'item à poser).
            number_of_parameters (int): Le nombre de paramètres attendus (1 paramètre - l'item à poser).

        Returns:
            bool: True si la commande a été exécutée avec succès, False sinon.
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))  # Affichage de l'erreur si le nombre de paramètres est incorrect
            return False

        # Vérifier que l'item est dans l'inventaire du joueur
        item_name = list_of_words[1]
        player = game.player
        item = next((item for item in player.inventory if item.name == item_name), None)

        if not item:
            print(f"\nVous n'avez pas l'objet '{item_name}' dans votre inventaire.\n")
            return False

        # Retirer l'item de l'inventaire du joueur
        player.inventory.remove(item)
        # Ajouter l'item à l'inventaire de la pièce
        player.current_room.inventory.append(item)

        print(f"\nVous avez reposé l'objet '{item_name}' dans cette pièce.\n")
        return True
