import random 
moves = ['melee', 'spell', 'block', 'dodge']
elements = ['fire', 'earth', 'water', 'air']

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 0
        self.defense = 0
    def damage(self):
        points = random.randint(1, 15)
        self.health -= points
    def move_choice(self):
        choice = int(input(
            """What is your move?
               1- melee
               2- spell
               3- block
               4- dodge
                """
            ))
        self.choice = choice - 1
    def element_choice(self):
        choice = int(input(
            """ What is your element?
                1- fire
                2- earth
                3- water
                4- air
                """
        ))
        element = choice - 1
class AiPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
    def move_choice(self):
        choice = int(input(
            """What is your move?
               1- melee
               2- spell
               3- block
               4- dodge
                """
            ))
        self.choice = choice - 1
    def element_choice(self):
        choice = random.randint(0, 3)
        element = choice - 1

class Game:
    Gameover = False

player_1 = Player("Lorcas")


print(player_1)