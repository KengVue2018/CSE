class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, sword):
        super(Weapon, self).__init__(sword)
        self.duration = 100
        self.sword = sword
        self.damage = 25


class Rake(Weapon):
    def __init__(self, rake):
        super(Rake, self).__init__(rake)
        self.duration = 100
        self.damage = 15
        self.Rake = Rake


class Baseball_Bat(Weapon):
    def __init__(self, baseball_bat):
        super(Baseball_Bat, self).__init__(baseball_bat)
        self.damage = 10
        self.duration = 100
        self.Baseball_Bat = Baseball_Bat


class Hands(Weapon):
    def __init__(self):



class Shield(Item):
    def __init__(self, Shield):
        super(Shield, self).__init__(Shield)
        self.duration = 100
        self.shield = Shield
        self.blocks_damage = 10


class Armor(Item):
    def __init__(self, helmet):
        super(Armor, self).__init__(helmet)
        self.duration = 100
        self.blocks_damage = 10


class ChestArmor(Armor):
    def __init__(self, chest_armor):
        super(Armor, self).__init__(chest_armor)
        self.duration = 100
        self.blocks_damage = 25


class Leg_Armor(Armor):
    def __init__(self, leg_armor):
        super(Armor, self).__init__(leg_armor)
        self.duration = 100
        self.blocks_damage = 25


class boots(Armor):
    def __init__(self, boots):
        super(Armor, self).__init__(boots)
        self.duration = 100
        self.blocks_damage = 10


class Consumables(Item):
    def __init__(self, name):
        super(Consumables, self).__init__(name)
        self.name = name


class Apple(Consumables):
    def __init__(self, apple):
        super(Consumables, self).__init__(apple)
        self.heal = 10


class health_potions(Consumables):
    def __init(self, health_potions):
        super(health_potions, self).__init__(health_potions)
        self.heal = 20










