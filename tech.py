class TechTree():
    def __init__(self, tech_name, food_cost, wood_cost, stone_cost, gold_cost, time_to_research, fase_to_research):
        self.tech_name = tech_name
        self.food_cost = food_cost
        self.wood_cost = wood_cost
        self.stone_cost = stone_cost
        self.gold_cost = gold_cost
        self.time_to_research = time_to_research
        self.fase_to_research = fase_to_research
        self.unit_affected = []
        self.building_affected = []
        self.researched = False
        self.description = None
        self.improve_health = 0
        self.improve_hack_resistance = 0
        self.improve_pierce_resistance = 0
        self.improve_crush_resistance = 0
        self.improve_pierce_attack = 0
        self.improve_hack_attack = 0
        self.improve_crush_attack = 0
        self.improve_aim = 0
        self.improve_attack_speed = 0
        self.improve_movement_speed = 0
        self.improve_gather_speed = 0
        self.improve_build_speed = 0
        self.improve_research_speed = 0
        self.improve_health_speed = 0
        self.improve_attack_max_range = 0
        self.improve_attack_min_range = 0
        self.improve_vision_range = 0
        self.improve_action_range = 0
        self.improve_shoots_per_guarnition = 0
        self.improve_max_guarnition = 0
        self.improve_guarnition_health_regen = 0
        self.improve_extra_population = 0
        self.extra_resources = 0
        self.reduct_costs = 0
        self.improve_gains = 0
        self.affect_self = True
        self.affect_allies = False
        self.affect_enemies = False

class CivBonus(TechTree):
    def __init__(self):
        self.beneficied_civ = None

class TeamBonus(TechTree):
    def __init__(self):
        self.civ_propiety = None