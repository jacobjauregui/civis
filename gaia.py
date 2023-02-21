class NaturalResources:
    def __init__(self):
        self.tree_selected = False
        self.rock_selected = False
        self.mine_selected = False
        self.fish_selected = False
        self.comestible_fauna_selected = False
        self.fruit_selected = False
        self.fishes = [
            self.atun,
            self.sardina,
            self.fish_bank
        ]
        self.comestible_fauna = [
            self.pavo,
            self.chicken,
            self.sheep,
            self.goat,
            self.pig,
            self.cow
        ]
        self.fruits = [
            self.apple,
            self.kiwi,
            self.uva,
            self.cheer
        ]
        self.trees = [
            self.roble,
            self.pino,
            self.cipres,
            self.palm,
            self.nogal,
            self.old_tree,
            self.big_tree
        ]
        self.rock = [
            self.small_rocks,
            self.medium_rocks,
            self.big_rocks,
            self.megalito
        ]
        self.mines = [
            self.small_mine,
            self.medium_mine,
            self.big_mine,
            self.megalito_mine
        ]
        self.wild_fauna = [
            "bear",
            "wolf",
            "jaguar",
            "lion",
            "tiger",
            "rhino",
            "hippopotamus"
        ]
        self.marine_fauna = [
            "dolphin",
            "shark",
            "whale",
            "seal",
            "turtle",
            "octopus",
            "squid"
        ]

class Wood(NaturalResources):
    def __init__(self):
        self.roble = 200
        self.pino = 500
        self.cipres = 350
        self.palm = 300
        self.nogal = 400
        self.old_tree = 100
        self.big_tree = 850
        self.apple = 100
        self.kiwi = 150
        self.uva = 200
        self.cheer = 250
        
class Food(NaturalResources):
    def __init__(self):
        self.apple = 100
        self.kiwi = 150
        self.uva = 200
        self.cheer = 250
        self.atun = 100
        self.sardina = 50
        self.fish_bank = 200
        self.chicken = 100
        self.pavo = 150
        self.sheep = 200
        self.goat = 300
        self.pig = 350
        self.cow = 500

class Stone(NaturalResources):
    def __init__(self):
        self.small_rocks = 250
        self.medium_rocks = 450
        self.big_rocks = 600
        self.megalito = 2000

class Metal(NaturalResources):
    def __init__(self):
        self.small_mine = 300
        self.medium_mine = 500
        self.big_mine = 700
        self.megalito_mine = 2000