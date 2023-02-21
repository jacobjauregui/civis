class Building:
    def __init__(self, building_name, building_type, build_time, wood_cost, stone_cost, gold_cost, health, build_fase):
        self.bulding_name = building_name
        self.building_type = building_type 
        self.wood_cost = wood_cost
        self.stone_cost = stone_cost
        self.gold_cost = gold_cost
        self.build_time = build_time
        self.build_fase = build_fase
        self.health = health
        self.recruitable_units = []
        self.tech_tree = []
        self.available_for_civ = []
        self.can_attack = False
        self.hack_resistance = 0
        self.pierce_resistance = 0
        self.crush_resistance = 0
        self.pierce_attack = 0
        self.attack_min_range = 0
        self.attack_max_range = 0
        self.speed_attack = 0
        self.shoots_pred = 0
        self.shoots_per_guarnition = 0
        self.max_guarnition = 0
        self.actual_guarnition = 0
        self.guarnition_health_regen = 0
        self.extra_population = 0
        self.vision_range = 0
        self.is_building = False
        self.building_selected = False
        self.enabled_to_build = False
        self.guarnition_enabled = False