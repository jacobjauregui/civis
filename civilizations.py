class Civilization:
    def __init__(self, mod):
        self.mod = mod 
        self.name = '' 
        self.name_sp = '' 
        self.emblem = ''
        self.civ_id = 0
        self.units = []
        self.buildings = []
        self.tech_tree = []
    

    def mod_0ad(self):
        if self.mod == "unique":
            self.gen=Civilization('default')
            self.athen=Civilization('default')
            self.brit=Civilization('default')
            self.cart=Civilization('default')
            self.gaul=Civilization('default')
            self.han=Civilization('default')
            self.iber=Civilization('default')
            self.kush=Civilization('default')
            self.mace=Civilization('default')
            self.maur=Civilization('default')
            self.pers=Civilization('default')
            self.ptol=Civilization('default')
            self.rome=Civilization('default')
            self.sele=Civilization('default')
            self.spart=Civilization('default')
            self.group=[
               self.gen,
               self.athen,
               self.brit,
               self.cart,
               self.gaul,
               self.han,
               self.iber,
               self.kush,
               self.mace,
               self.maur,
               self.pers,
               self.ptol,
               self.rome,
               self.sele,
               self.spart,
            ]
            names=[
                "Generic",
                "Athenians",
                "Britons",
                "Carthagians",
                "Gauls",
                "Han",
                "Iberians",
                "Kushites",
                "Macedonians",
                "Mauryas",
                "Persians",
                "Ptolomies",
                "Romans",
                "Seleucids",
                "Spartans",
            ]
            self.names_sp = [
               "General",
               "Atenienses",
               "Britanos",
               "Cartagineses",
               "Galos",
               "Han",
               "Iberos",
               "Cushitas",
               "Macedonios",
               "Mauryas",
               "Persas",
               "Ptolomeos",
               "Romanos",
               "Seleúcidas",
               "Espartanos",
            ]
            for i, civ in enumerate(self.group):
                civ.civ_id = i
                civ.name = names[i]
                civ.name_sp = self.names_sp[i]
                civ.emblem = f"./images/portraits/emblems/emblem_{civ.name.lower()}.png"