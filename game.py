# Description: Game class
'''
Author : Carvalho Allan & Brault Oscar
'''

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import *
from character import Character
from monster import Monster


class Game:
    '''
    La classe Game permet de créer 
    l'environnement et la jouabilité
    '''
    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.directions = set()
        self.history = []  # Historique des pièces visitées
        self.inventory_room = {}

    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O, UP, DOWN)", Actions.go, 1)
        self.commands["go"] = go
        back = Command("back", " : revenir à l'endroit précédent", Actions.back, 0)
        self.commands["back"] = back
        history = Command("history", " : afficher l'historique", Actions.history, 0)
        self.commands["history"] = history
        check = Command("check", " : afficher l'inventaire du personnage", Actions.check, 0)
        self.commands["check"] = check
        look = Command("look", " : afficher l'inventaire du personnage", Actions.look, 0)
        self.commands["look"] = look
        drop= Command("drop", " : déposer l'objet", Actions.drop , 0)
        self.commands["drop"] = drop
        take=Command("take", " : prendre l'objet", Actions.take , 0)
        self.commands["take"] = take
        move=Command("move", " : déplacer le pnj dans une autre pièce avec un certain pourcentage de chance", Actions.move , 0)
        self.commands["move"] = move
        talk=Command("talk"," : parler au pnj", Actions.talk , 1)
        self.commands["talk"] = talk
        combat=Command("combat"," : combat les monstres", Actions.combat , 1)
        self.commands["combat"] = combat
        equip = Command("equip", ": équipe l'objet", Actions.equip, 1)
        self.commands["equip"]= equip

        # Liste des directions possibles
        self.directions = {"N", "E", "S", "O", "UP", "DOWN"}
        Direction_Map = {"N": "N", "NORD": "N", "E": "E", "EST": "E", "S": "S", "SUD": "S", "O": "O", "OUEST": "O", "UP": "UP", "HAUT": "UP", "DOWN": "DOWN", "BAS": "DOWN"}
        
        # Setup rooms

        forest1 = Room("Forest", "dans la forêt paisible. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(forest1)

        forest2 = Room("Forest", "dans une forêt plus calme, une corde à votre gauche vous permettra de vous échapper.")
        self.rooms.append(forest2)

        forest3 = Room("Forest", "dans une forêt extrêmement dangereuse. Les monstres vous attaquent.")
        self.rooms.append(forest1)

        front_village = Room("Front_village", "à l'entrée d'un village, vous avez la possibilité de vous y balader.")
        self.rooms.append(front_village)

        house_ground_floor = Room ("Ground_floor", "vous êtes au rez de chaussée de la maison, à l'étage vous trouverez le PNJ." )
        self.rooms.append(house_ground_floor)
      
        pnj_floor = Room("Pnj", "à cet étage, vous avez face à vous le pnj qui vous permettra de marchander." )
        self.rooms.append(pnj_floor)

        meadow = Room("Meadow", "dans une immense prairie.")
        self.rooms.append(meadow)

        fontain = Room("Fontain", "au niveau d'une fontaine à eau.. cela pourrait être intéréssant.")
        self.rooms.append(fontain)

        front_cave = Room("Cave", "dans une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
        self.rooms.append(front_cave)

        # Setup under ground

        iron_ore = Room("Iron ore", "dans une grotte avec des minerais tout autour de vous. Allons l'explorer.")
        self.rooms.append(iron_ore)

        diamond_ore = Room("Diamond ore", "dans une grotte avec des minerais plus brilliant autour de vous. Allons miner.")
        self.rooms.append(diamond_ore)
        
        mob_cave = Room("Mob Cave", "dans une grotte avec des monstres qui vous attaquent !")
        self.rooms.append(mob_cave)

        stronghold= Room("Stronghold", "dans pièce avec un portail. Ces yeux sur le portail sont flippants...")
        self.rooms.append(stronghold)

        enderdragon = Room("Enderdragon", "sur l'île du dragon, nous n'avons pas le choix que de le battre.")
        self.rooms.append(enderdragon)

        portal_overwolrd = Room("Portal overwolrd", "au portail pour retrouver la maison, on a réussi... bravo.")
        self.rooms.append(portal_overwolrd)

        lava_lake = Room("Lava lake", "au bord du lac de lave.. il fait chaud ici !")
        self.rooms.append(lava_lake)

        portal_nether = Room("Portal Overwolrd -> Nether", "au niveau d'un portail noir étrange, qui semble mener vers une autre dimension")
        self.rooms.append(portal_nether)

        blaze_spawn = Room("Blaze spawn","dans la forteresse. Il serait intéressant de récuperer des blaze rod")
        self.rooms.append(blaze_spawn)

        portal_nether2 = Room("Portal Nether -> Overworld", "au niveau du portail pour rentrer dans la dimension originelle.")
        self.rooms.append(portal_nether2)


        # Create exits for rooms, inventory & character

        forest1.exits = {"N" : front_village, "E" : None, "S" : None, "O" : None, "UP" : None, "DOWN" : None}
        forest1.inventory_room = {"stick" : Item("stick", "un stick utile pour débuter", 1)}
        zombie = Monster("zombie", "Un zombie puant", 3, 1, forest1)
        forest1.characters[zombie.name] = zombie

        forest2.exits = {"N" : None, "E" : forest3, "S" : None, "O" : forest1, "UP" : None, "DOWN" : None}
        forest2.inventory_room = {"stick" : Item("stick", "un stick utile pour débuter", 1)}
        squelette = Monster("squelette", "Un squelette éffrayant portant un arc", 3, 1, forest2)
        forest2.characters[squelette.name] = squelette

        forest3.exits = {"N" : front_cave, "E" : None, "S" : None, "O" : forest2, "UP" : None, "DOWN" : None}
        forest3.inventory_room = {"stick" : Item("stick", "un stick utile pour débuter", 1)}
        zombie = Monster("zombie", "Un zombie puant", 3, 1, forest3)
        forest3.characters[zombie.name] = zombie

        front_village.exits = {"N" : house_ground_floor, "E" : fontain, "S" : forest1, "O" : None, "UP" : None, "DOWN" : None}

        house_ground_floor.exits = {"N" : None, "E" : None, "S" : front_village, "O" : None, "UP" : pnj_floor, "DOWN" : None}
        
        
        pnj_floor.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "UP" : None, "DOWN" : house_ground_floor}
        villageois = Character("villageois", "un villageois au couteau suisse", pnj_floor, ["Bonjour, si vous voulez procéder à des échanges faites-moi signe. !", "Quand il y a un doute, il n'y a pas de doute, venez procéder à un échange ici !"])
        pnj_floor.characters[villageois.name] = villageois

        meadow.exits = {"N" : None, "E" : None, "S" : fontain, "O" : None, "UP" : None, "DOWN" : None}
        meadow.inventory_room = {"beamer" : Item("beamer", "un téléporteur", 1)}

        fontain.exits = {"N" : meadow, "E" : front_cave, "S" : None, "O" : front_village, "UP" : None, "DOWN" : None}

        front_cave.exits = {"N" : None, "E" : None, "S" : forest3, "O" : fontain, "UP" : None, "DOWN" : iron_ore}

        iron_ore.exits = {"N" : diamond_ore, "E" : lava_lake, "S" : None, "O" : mob_cave, "UP" : front_cave, "DOWN" : None}
        iron_ore.inventory_room  = {"fer" : Item("fer", "un minerai fiable et résistant", 0.5)}

        diamond_ore.exits = {"N" : None, "E" : None, "S" : iron_ore, "O" : None, "UP" : None, "DOWN" : None}
        diamond_ore.inventory_room  = { "diamant" :Item("diamant", "un minerai avec une solidité exceptionnelle", 1)}

        mob_cave.exits = {"N" : stronghold, "E" : iron_ore, "S" : None, "O" : None, "UP" : None, "DOWN" : None}
        zombie = Monster("zombie", 3, 1, mob_cave)
        mob_cave.characters[zombie.name] = zombie


        stronghold.exits = {"N" : None, "E" : None, "S" : mob_cave, "O" : enderdragon, "UP" : None, "DOWN" : None}

        enderdragon.exits = {"N" : None, "E" : None, "S" : None, "O" : portal_overwolrd, "UP" : None, "DOWN" : None,}
        dragon = Monster("dragon", "Un dragon noir volant à toute vitesse", 15, 4, enderdragon)
        enderdragon.characters[dragon.name] = dragon

        portal_overwolrd.exits = {"N" : front_village, "E" : front_village, "S" : front_village, "O" : front_village, "UP" : None, "DOWN" : None}

        lava_lake.exits = {"N" : portal_nether, "E" : None, "S" : None, "O" : iron_ore, "UP" : None, "DOWN" : None}

        portal_nether.exits = {"N" : None, "E" : portal_nether2, "S" : lava_lake, "O" : None, "UP" : None, "DOWN" : None}

        blaze_spawn.exits = {"N" : None, "E" : None, "S" : None, "O" : portal_nether2, "UP" : None, "DOWN" : None}
        blaze_spawn.inventory_room = {"Blazerod" : Item("Blazerod", "un bâton particulier qui nous servira plus tard", 0.3)}

        portal_nether2.exits = {"N" : None, "E" : blaze_spawn, "S" : None, "O" : portal_nether, "UP" : None, "DOWN" : None}


        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = forest1

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            if self.finished:
                break
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")
        
        command_word = list_of_words[0]
        
        if not command_word :
            return  

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]

            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
