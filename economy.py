class Resources:
    def __init__(self):
        self.food_initial = 300 
        self.initial_wood = 300 
        self.initial_stone = 300 
        self.initial_metal = 300 
        self.time = 0
        self.population_initial = 9 
        self.population_limit = 20
        self.food_stored = 0
        self.wood_stored = 0
        self.stone_stored = 0
        self.metal_stored = 0
        self.population_total = 0
        self.food_collected = 0
        self.wood_collected = 0
        self.stone_collected = 0
        self.metal_collected = 0
        self.food_consumed = 0
        self.wood_consumed = 0
        self.stone_consumed = 0
        self.metal_consumed = 0
        
        
        def show_food(self, food_collected, food_consumed):
            self.food_stored = self.food_initial + self.food_collected - self.food_consumed
            print(self.food_stored)

        def show_wood(self, wood_collected, wood_consumed):
            self.wood_stored = self.wood_initial + self.wood_collected - self.wood_consumed

            print(self.wood_stored)
            
        def show_stone(self, stone_collected, stone_consumed):
            self.stone_stored = self.stone_initial + self.stone_collected - self.stone_consumed
            print(self.stone_stored)
            
        def show_metal(self, metal_collected, metal_consumed):
            self.metal_stored = self.metal_initial + self.metal_collected - self.metal_consumed
            print(self.metal_stored)
        
        def show_population(self, houses_built, town_halls_built, bonus_population, techs):
            self.units_recluted = 0
            self.units_killed = 0
            self.population_limit = (houses_built * 5) + (town_halls_built * 20) + bonus_population + techs
            self.population_total = self.initial_population + self.units_recluted - self.units_killed
            
        
class Relics:
    def __init__(self):
        self.small_food_reliq = 100
        self.medium_food_reliq = 250
        self.big_food_reliq = 500
        self.small_wood_reliq = 100
        self.medium_wood_reliq = 250
        self.big_wood_reliq = 500
        self.small_stone_reliq = 100
        self.medium_stone_reliq = 250
        self.big_stone_reliq = 500
        self.small_gold_reliq = 100
        self.medium_gold_reliq = 250
        self.big_gold_reliq = 500

        