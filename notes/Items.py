class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name):
        super(Weapon, self).__init__(name)
        self.name = name


class Rake(Weapon):
    def __init__(self, rake):
        super(Rake, self).__init__(rake)
        self.duration = 100
        self.damage = 15
        self.Rake = Rake


class BaseballBat(Weapon):
    def __init__(self, baseball_bat):
        super(BaseballBat, self).__init__(baseball_bat)
        self.damage = 10
        self.duration = 100
        self.baseball_bat = baseball_bat


class Hands(Weapon):
    def __init__(self, hands):
        super(Hands, self).__init__(hands)
        self.damage = 5
        self.hands = hands


class Knife(Weapon):
    def __init__(self, knife):
        super(Knife, self).__init__(knife)
        self.damage = 20
        self.duration = 100
        self.knife = knife


class Sword(Weapon):
    def __init__(self, sword):
        super(Sword, self).__init__(sword)
        self.damage = 30
        self.duration = 100
        self.sword = sword


class Shield(Item):
    def __init__(self, shields):
        super(Shield, self).__init__(shields)
        self.duration = 100
        self.shields = shields
        self.blocks_damage = 10


class Armor(Item):
    def __init__(self, name):
        super(Armor, self).__init__(name)
        self.name = name
        

class Helmet(Armor):
    def __init__(self, helmet):
        super(Helmet, self).__init__(helmet)
        self.duration = 10
        self.blocks_damage = 10


class ChestArmor(Armor):
    def __init__(self, chest_armor):
        super(Armor, self).__init__(chest_armor)
        self.duration = 100
        self.blocks_damage = 25


class LegArmor(Armor):
    def __init__(self, leg_armor):
        super(Armor, self).__init__(leg_armor)
        self.duration = 100
        self.blocks_damage = 25


class Boots(Armor):
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


class HealthPotions(Consumables):
    def __init(self, health_potions):
        super(HealthPotions, self).__init__(health_potions)
        self.heal = 20


class WaterBottle(Consumables):
    def __init__(self, Water_Bottle):
        super(WaterBottle, self).__init__(Water_Bottle)
        self.heal = 5


class Oranges(Consumables):
    def __init__(self, oranges):
        super(Oranges, self).__init__(oranges)
        self.heal = 10


class Corn(Consumables):
    def __init__(self, corn):
        super(Corn, self).__init__(corn)
        self.heal = 10











