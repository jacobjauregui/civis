from gaia import Food, Wood, Stone, Metal

class Citizen:
    def __init__(self, food, wood, stone, metal, time, population):
        self.food = food
        self.wood = wood
        self.stone = stone
        self.metal = metal
        self.time = time
        self.population = population
        self.be_trainig_in = ["Centro civico"]
        self.unit_type = "civil"
        self.fase_to_train = "Fase I"
        self.health = 100.00
        self.hack_resistance = 1.0
        self.pierce_resistance = 1.0
        self.crush_resistance = 1.0
        self.walk = 9.00
        self.run = 15.00
        self.swim = 35.00

class Worker:
    def __init__(self, building, farming, felling, harvesting, hunting, mining_stone, mining_metal, storage):
        self.building = building
        self.farming = farming
        self.felling = felling
        self.harvesting = harvesting
        self.hunting = hunting
        self.mining_stone = mining_stone
        self.mining_metal = mining_metal
        self.storage = storage
        self.worker_type = [
            "constructor",
            "cosechador",
            "talador",
            "cazador",
            "minero"
        ]

class Militar:
    def __init__(self, weapon, hack, pierce, crush, distance, speed):
        self.weapon = weapon 
        self.hack = hack
        self.pierce = pierce
        self.crush = crush
        self.distance = distance
        self.speed = speed
        self.militar_type = "Soldado"
        self._range = "Cuerpo a cuerpo"
        self._class = "Infantería"
        
class Machines:
    def __init__(self, time_to_build, guarnition_limit):
        self.time_to_build = time_to_build
        self.guarnition_limit = guarnition_limit

class Woman(Citizen, Worker, Militar):
    def __init__(self, unit_name):
        self.unit_name = unit_name
        self.cost = Citizen(50, 0, 0, 0, 8, 1)
        self.speed = Worker(1, 0.50, 0.70, 1.00, 1.00, 0.25, 0.25, 10)
        self.attack = Militar("daga",2,1,1,3,1)
        self.militar_type = "apoyo"
        self.health = 35.00
        self.hack_resistance = 1.00
        self.pierce_resistance = 1.00
        self.crush_resistance = 1.00
        self.walk = 9.00
        self.run = 15.00
        self.swim = 35.00
        self.be_trainig_in = ["Centro civico", "Casa"]

'''
woman = Worker(0.50, 0.70, 1.00, 1.00, 0.00, 0.25, 0.25)
woman.unit_name = "Ciudadana"
woman.worker_type = [
    'Granjera',
    'Recolectora',
    'Cazadora',
    'Leñadora',
    'Minera'
]

man = Worker(0.25, 0.75, 0.50, 1.00, 1.00, 0.50, 0.50)
man.unit_name = "Ciudadano"
man.worker_type=[
    'Granjero',
    'Recolector',
    'Cazador',
    'Talador',
    'Minero'
]
hunter_horse = Worker(0.00, 0.00, 0.00, 5.00, 0.00, 0.00, 0.00)
hunter_horse.unit_name = 'Cazador a caballo'
hunter_horse.worker_type = [
    'Ciudadano',
    'Explorador',
    'Cazador'
'''

'''
citizen = uni.Militar("Daga")
citizen.unit_name = "Mujer"
citizen.unit_class = "Ciudadana"
citizen.militar_class = "Apoyo"
citizen.food_cost = 50
citizen.wood_cost = 0
citizen.stone_cost = 0
citizen.metal_cost = 0
citizen.training_time = 8

spearman = uni.Militar("Lanza")
spearman.unit_name = "Lancero"
spearman.food_cost = 50
spearman.wood_cost = 50
spearman.stone_cost = 0
spearman.metal_cost = 0
spearman.training_time = 10

swordman = uni.Militar("Espada")
swordman.unit_name = "Espadachín"
swordman.food_cost = 50
swordman.wood_cost = 40
swordman.stone_cost = 0
swordman.metal_cost = 10
swordman.training_time = 10

pikeman = uni.Militar("Picaro")
pikeman.unit_name = "Piquero"
pikeman.food_cost = 50
pikeman.wood_cost = 50
pikeman.stone_cost = 0
pikeman.metal_cost = 00
pikeman.training_time = 10

archer = uni.Militar("Arco")
archer.unit_name = "Arquero"
archer.attack_range = "A distancia"
archer.food_cost = 50
archer.wood_cost = 50
archer.stone_cost = 0
archer.metal_cost = 0
archer.training_time = 10

crossbowman = uni.Militar("Ballesta")
crossbowman.unit_name = "Ballestero"
crossbowman.attack_range = "A distancia"
crossbowman.food_cost = 50
crossbowman.wood_cost = 50
crossbowman.stone_cost = 0
crossbowman.metal_cost = 0
crossbowman.training_time = 10

slinger = uni.Militar("Honda")
slinger.unit_name = "Hondero"
slinger.attack_range = "A distancia"
slinger.food_cost = 50
slinger.wood_cost = 20
slinger.stone_cost = 30
slinger.metal_cost = 0
slinger.training_time = 10

skirmisher = uni.Militar("Jabalina")
skirmisher.unit_name = "Jabalinero"
skirmisher.attack_range = "A distancia"
skirmisher.food_cost = 50
skirmisher.wood_cost = 20
skirmisher.stone_cost = 30
skirmisher.metal_cost = 0
skirmisher.training_time = 10

javelinhorse = uni.Militar("Jabalina")
javelinhorse.unit_name = "Jabalinero a caballo"
javelinhorse.militar_class = "Caballería"
javelinhorse.attack_range = 'A distancia'
javelinhorse.food_cost = 100
javelinhorse.wood_cost = 50
javelinhorse.stone_cost = 0
javelinhorse.metal_cost = 0
javelinhorse.training_time = 15

knight = uni.Militar("Espada")
knight.unit_name = "Espadachín a caballo"
knight.militar_class = "Caballería"
knight.food_cost = 100
knight.wood_cost = 40
knight.stone_cost = 0
knight.metal_cost = 10
knight.training_time = 15

spearhorse = uni.Militar("Lanza")
spearhorse.unit_name = "Lancero a caballo"
spearhorse.militar_class = "Caballería"
spearhorse.food_cost = 100
spearhorse.wood_cost = 50
spearhorse.stone_cost = 0
spearhorse.metal_cost = 0
spearhorse.training_time = 15

mercenary = uni.Militar("Espada")
mercenary.unit_name = "Espadachín mercenario"
mercenary.unit_type = "Mercenario"
mercenary.food_cost = 0
mercenary.wood_cost = 0
mercenary.stone_cost = 0
mercenary.metal_cost = 60
mercenary.training_time = 7

mercenary_cavalry = uni.Militar("Mazo")
mercenary_cavalry.unit_name = "Macero noba"
mercenary_cavalry.unit_type = "Mercenario"
mercenary_cavalry.food_cost = 20
mercenary_cavalry.wood_cost = 0
mercenary_cavalry.stone_cost = 0
mercenary_cavalry.metal_cost = 90
mercenary_cavalry.training_time = 11


unit_gatherer = woman
print(unit_gatherer.hunting_speed, unit_gatherer.unit_name)
    
unit_to_train = input("Qué unidad quieres crear?\n1.Mujer\n2.Lancero\n3.Arquero\n4.Caballería\n--> ")
if unit_to_train == "1":
    unit_to_train = citizen
elif unit_to_train == "2":
    unit_to_train = spearman
elif unit_to_train == "3":
    unit_to_train = archer
elif unit_to_train == "4":
    unit_to_train = spearhorse
else:
    print("No existe esa unidad")
number_of_trains = int(input(f"Cuantos {unit_to_train.unit_name}s quires crear?\n"))

print(f"Unidad: {unit_to_train.unit_name}")
print(f"Alimento: {unit_to_train.food_cost}")
print(f"Madera: {unit_to_train.wood_cost}")
print(f"Piedra: {unit_to_train.stone_cost}")
print(f"Metal: {unit_to_train.metal_cost}")
print(f"Tiempo de entrenamiento: {unit_to_train.training_time} segundos\n")

if number_of_trains > 1:
    print(f"Para reclutar {number_of_trains} {unit_to_train.unit_name}s cada {unit_to_train.training_time * number_of_trains} segundos necesitas:")
    if unit_to_train.food_cost > 0:
        print(f"{unit_to_train.food_cost * number_of_trains} de comida")
    if unit_to_train.wood_cost > 0:
        print(f"{unit_to_train.wood_cost * number_of_trains} de madera")
    if unit_to_train.stone_cost > 0:
        print(f"{unit_to_train.stone_cost * number_of_trains} de piedra")
    if unit_to_train.metal_cost > 0:
        print(f"{unit_to_train.metal_cost * number_of_trains} de metal")
else:
    print(f"Para reclutar {number_of_trains} {unit_to_train.unit_name} cada {unit_to_train.training_time * number_of_trains} segundos necesitas:")
    if unit_to_train.food_cost > 0:
        print(f"{unit_to_train.food_cost * number_of_trains} de comida")
    if unit_to_train.wood_cost > 0:
        print(f"{unit_to_train.wood_cost * number_of_trains} de madera")
    if unit_to_train.stone_cost > 0:
        print(f"{unit_to_train.stone_cost * number_of_trains} de piedra")
    if unit_to_train.metal_cost > 0:
        print(f"{unit_to_train.metal_cost * number_of_trains} de metal")


resource_to_collect = input("Qué tipo de recurso quieres calcular? [1.Comida, 2.Madera, 3.Piedra, 4.Metal]\n")
if resource_to_collect == "1":
    food_type = input("Qué tipo de alimento quieres calcular? [1.Grano, 2.Frutos, 3.Carne]\n")
    if food_type == "1":
        unit_to_farm = input("Con qué trabajador quires recoger grano? [1.Granjera, 2.Granjero]\n")
        if unit_to_farm == "1":
            unit_to_farm = woman
        elif unit_to_farm == "2":
            unit_to_farm = man
    elif food_type == "2":
        unit_to_gather_fruit = input("Con qué trabajador quires recoger fruta? [1.Recolectora, 2.Recolector]\n")
        if unit_to_gather_fruit == "1":
            unit_to_gather_fruit = woman
        elif unit_to_gather_fruit == "2":
            unit_to_gather_fruit = man
    elif food_type == "3":
        unit_to_hunt = input("Con qué trabajador quires cazar? [1.Cazador, 2.Cazadora, 3.Cazador a caballo]\n")
        if unit_to_hunt == "1":
            unit_to_hunt == woman
        elif unit_to_hunt == "2":
            unit_to_hunt = man
        elif unit_to_hunt == "3":
            unit_to_hunt = hunter_horse
elif resource_to_collect == "2":
    unit_to_lumberjack = input("Con qué trabajador quires talar? [1.Leñadora, 2.Leñador]\n")
    if unit_to_lumberjack == "1":
        unit_to_lumberjack = woman
    elif unit_to_lumberjack == "2":
        unit_to_lumberjack = man   
elif resource_to_collect == "3":
    unit_to_mine_stone = input("Con qué trabajador quires minar piedra? [1.Minero, 2.Minera]\n")
    if unit_to_mine_stone == "1":
        unit_to_mine_stone = woman
    elif unit_to_mine_stone == "2":
        unit_to_mine_stone = man
elif resource_to_collect == "4":
    unit_to_mine_metal = input("Con qué trabajador quires minar oro? [1.Minero, 2.Minera]")
    if unit_to_mine_metal == "1":
        unit_to_mine_metal = woman
    elif unit_to_mine_metal == "2":
        unit_to_mine_metal = man


collecters_needed = int((number_of_trains*unit_to_train.training_time)/unit_to_farm.farming_speed)

print(f"Necesitas {collecters_needed} {unit_to_farm.unit_name} para crear {number_of_trains} {unit_to_train.unit_name}")
'''