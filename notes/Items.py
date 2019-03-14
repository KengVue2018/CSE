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

    Rake = Weapon("Rake", 10)


class BaseballBat(Weapon):
    def __init__(self, baseball_bat):
        super(BaseballBat, self).__init__(baseball_bat)
        self.duration = 100
        self.baseball_bat = baseball_bat

    BaseballBat = Weapon("Baseball_Bat", 10)

class Hands(Weapon):
    def __init__(self, hands):
        super(Hands, self).__init__(hands)
        self.hands = hands

    Hands = Weapon("Hands", 5)


class Knife(Weapon):
    def __init__(self, knife):
        super(Knife, self).__init__(knife)
        self.duration = 100
        self.knife = knife

    Knife = Weapon("Knife", 15)


class Sword(Weapon):
    def __init__(self, sword):
        super(Sword, self).__init__(sword)
        self.duration = 100
        self.sword = sword

    Sword = Weapon("Sword", 40)


class Rifle(Weapon):
    def __init__(self, rifle, name):
        super(Rifle, self).__init__(name)
        self.duration = 100
        self.rifle = rifle
        self.name = name

    Rifle = Weapon("Rifle", 40)

class Shield(Item):
    def __init__(self, shields):
        super(Shield, self).__init__(shields)
        self.duration = 100
        self.shields = shields
        self.blocks_damage = 10


class Armor(Item):
    def __init__(self, name, armor_amt, Armor):
        super(Armor, self).__init__(name)
        self.armor_amt = armor_amt


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
sword = Weapon("Sword", 10)
canoe = Weapon("Canoe", 42)
wiebe_armor = Armor("Armor of the Gods", 10000000000000000000000)


# Character
orc = Character("Orci", 100, sword, Armor("Genertic Armor", 2))
orc2 = Character("Wiebe", 1000, canoe, wiebe_armor)


orc.attack(orc2)
orc2.attack(orc)
orc2.attack(orc)
orc2.attack(orc)
