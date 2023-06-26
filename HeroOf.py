class HeroOf():
    """"Class to Create Hero for our Game"""
    def __init__(self, name, level, race):
        """Initiate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
    def show_hero(self):
        """Print all parametrs of this hero"""
        description = (self.name + ' Level is ' + str(self.level) + ' Race is ' + self.race + ' Health is ' + str(self.health)).title()
        print(description)
    def level_up(self):
        """Upgrade level of Hero"""
        self.level = self.level + 1
        #self.level += 1
    def move(self):
        '''Start moving Hero'''
        print("Hero " + self.name + " Start moving...")
    def set_health(self, new_health):
        self.health = new_health

#-------------------------===========================================
class SuperHero(HeroOfDonbass):
    """Class to Create Super Hero"""
    def __init__(self, name, level, race, magiclevel):
        """Initiate our Super Hero"""
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self._magic = 100
    def makemagic(self):
        """Use magic"""
        self._magic -= 10

    def show_hero(self):
        """Print all parametrs of this hero"""
        description = (self.name + ' Level is ' + str(self.level) + ' Race is ' + self.race + ' Health is ' + str(self.health) +
                       " Mana is " + str(self.magic)).title()
        print(description)
