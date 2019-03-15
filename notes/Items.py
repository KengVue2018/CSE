class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name):
        super(Weapon, self).__init__(name)
        self.name = name


class Rake(Weapon):
    def __init__(self, name):
        super(Rake, self).__init__(name)
        self.duration = 100
        self.Rake = Rake
        self.name = name


class BaseballBat(Weapon):
    def __init__(self, baseball_bat):
        super(BaseballBat, self).__init__(baseball_bat)
        self.duration = 100
        self.baseball_bat = baseball_bat


class Hands(Weapon):
    def __init__(self, hands):
        super(Hands, self).__init__(hands)
        self.hands = hands


class Knife(Weapon):
    def __init__(self, knife):
        super(Knife, self).__init__(knife)
        self.duration = 100
        self.knife = knife


class Sword(Weapon):
    def __init__(self, sword):
        super(Sword, self).__init__(sword)
        self.duration = 100
        self.sword = sword


class Rifle(Weapon):
    def __init__(self, rifle, name):
        super(Rifle, self).__init__(name)
        self.duration = 100
        self.rifle = rifle
        self.name = name

class Shield(Item):
    def __init__(self, shields):
        super(Shield, self).__init__(shields)
        self.duration = 100
        self.shields = shields
        self.blocks_damage = 10


class Armor(Item):
    def __init__(self, name, Armor):
        super(Armor, self).__init__(name)
        self.armor_amt = Armor


class Helmet(Armor):
    def __init__(self, Helmet):
        super(Armor, self).__init__(Helmet)
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
    def __init__(self, water_bottle):
        super(WaterBottle, self).__init__(water_bottle)
        self.heal = 5


class Oranges(Consumables):
    def __init__(self, oranges):
        super(Oranges, self).__init__(oranges)
        self.heal = 10


class Corn(Consumables):
    def __init__(self, corn):
        super(Corn, self).__init__(corn)
        self.heal = 10


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage: int):
        if self.armor.armor_amt > damage:
            print("No damage was taken because of some AMAZING armor.")
        else:
            self.health -= damage - self.armor.armor_amt
            print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


# Items
sword = Weapon("Sword")
canoe = Weapon("Canoe")
Kengs_Armor = Armor("Armor of the Legend")


# Character
orc = Character("Orc", 100, sword, Armor("Genertic Armor", 2))
orc2 = Character("Wiebe", 1000, canoe, Armor)


orc.attack(orc2)
orc2.attack(orc)
orc2.attack(orc)
orc2.attack(orc)
