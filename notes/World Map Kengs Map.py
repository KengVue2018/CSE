class Room(object):
    def __init__(self, name, description, north=None, west=None, south=None, east=None, items=None):
        if items is None:
            items = []
        self.name = name
        self.description = description
        self.north = north
        self.west = west
        self.south = south
        self.east = east
        self.items = items


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
        self.name = name
        self.damage = 10
        self.use = False

    def duration(self):
        self.use = True
        self.duration -= 1


class BaseballBat(Weapon):
    def __init__(self, baseball_bat):
        super(BaseballBat, self).__init__(baseball_bat)
        self.duration = 100
        self.baseball_bat = baseball_bat
        self.damage = 10
        self.use = False

    def duration(self):
        self.use = True
        self.duration -= 1


class Hands(Weapon):
    def __init__(self, hands):
        super(Hands, self).__init__(hands)
        self.hands = hands
        self.damage = 5
        self.use = False

    def duration(self):
        self.use = True
        self.duration -= 1


class Knife(Weapon):
    def __init__(self, name):
        super(Knife, self).__init__(name)
        self.duration = 100
        self.damage = 20
        self.use = False

    def duration(self):
        self.use = True
        self.duration -= 1


class Sword(Weapon):
    def __init__(self, name):
        super(Sword, self).__init__(name)
        self.duration = 100
        self.damage = 35
        self.name = name
        self.use = False

    def duration(self):
        self.use = True
        self.duration -= 1


class Rifle(Weapon):
    def __init__(self, name):
        super(Rifle, self).__init__(name)
        self.duration = 100
        self.name = name
        self.damage = 40
        self.use = False

    def duration(self):
        self.use = True
        self.duration -= 1


class Shield(Item):
    def __init__(self, shield):
        super(Shield, self).__init__(shield)
        self.duration = 100
        self.blocks_damage = 10
        self.use = False

    def duration(self):
        self.use = True
        self.duration -= 1


class Armor(Item):
    def __init__(self, name, armor):
        super(Armor, self).__init__(name)
        self.armor = armor


class Helmet(Armor):
    def __init__(self, helmet):
        super(Armor, self).__init__(helmet)
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


class Backpack(Item):
    def __init__(self, name):
        super(Backpack, self).__init__(name)
        self.backpack_space = 10


rake = Rake('Rake')
baseball_bat = BaseballBat('BaseBallBat')
hands = Hands('Hands')
knife = Knife('Knife')
sword = Sword('Sword')
rifle = Rifle('Rifle')
shield = Shield('Shield')
helmet = Helmet('Helmet')
chest_armor = ChestArmor('ChestArmor')
leg_armor = LegArmor('LegArmor')
boots = Boots('Boots')
backpack = Backpack('Backpack')
corn = Corn('Corn')
oranges = Oranges('Orange')
water_bottle = WaterBottle('WaterBottle')
health_potion = HealthPotions('HealthPotion')
apple = Apple('Apple')


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


house = Room("House", "It's your house. And you are in it. It is some how very quiet. But you hear noise in the "
                      "direction of west.",
             'horse_pin', 'street', 'orange_trees', None, [knife, backpack, rifle, WaterBottle])

horse_pin = Room("Horse Pin", "Its the Horse Pin. It stinks but it doesn't smell that bad here. "
                 "Looks like there's a path that keep going up north.", 'garbage', None, 'house', None, [Rake,
                                                                                                         WaterBottle])

garbage = Room("Garbage", "This is where the garbage is at. It stink super bad here.", None, None, 'horse pin', None,
               [])

street = Room("Street", "The Street is so empty. Nobody takes this street.", 'store', None, None, 'house', [])

orange_trees = Room("Orange Trees", "Its full of orange trees. Some of them are really good. But looks like there's a"
                    "building to the east.", 'house', None, None, 'farm', [Oranges])

farm = Room("Farm", "The Farm is full of items, but a lot of them are for farming only.", 'field', 'orange_trees',
            'slaughter_house', 'storage_house', [Helmet, HealthPotions])

field = Room("Field", "The field is full of corn. But you can barely see anything once your inside it.", 'pond', None,
             'farm', None, [Corn])

storage_house = Room("Storage House", "There's a lot of stuff in here. But there is also barely any room in here.",
                     'cow_pin', 'farm', None, None, [Sword, HealthPotions])

cow_pin = Room("Cow Pin", "It smells awful but there are barley any cows here. But the pig pin have more pigs.",
               None, None, 'cow_pin', 'pig_pin', [])

pig_pin = Room("Pig Pin", "Wow this place smells even worst then the cow pin but its very quiet for how much pigs "
                          "that are here.", 'chicken_pin', 'cow_pin', 'water_storage', None, [])

water_storage = Room("Water Storage", "There are two big tubes here that holds water here. There is also a "
                                      "car here too.", 'pig_pin', None, None, None, [WaterBottle])

chicken_pin = Room("Chicken Pin", "It doesn't smell that bad as the other 2 but it sure is louder then the others.",
                   None, 'apple_trees', 'pig_pin', None, [])

apple_trees = Room("Apple Trees", "There are a lot of apple trees here. This could be a good spot to "
                                  "play hide and seek.", None, None, None, 'chicken_pin', [Apple])

store = Room("Store", "There's a lot of good stuff to eat here. But I don't like the food there.", None,
             None, 'street', None, [])


pond = Room("Pond", "It looks like the pond has a pretty clear water but no animals or fish are in there.", None,
            None, 'field', None, [])


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        """This moves the player to a new room

        :param self:
        :param new_location: The room object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """This method searches the current room so see if a room exists in that direction.

        :param self:
        :param direction:The direction you want to move to.
        :return The Room object if it exists, or None if it does not.
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]


player = Player(house)

playing = True
directions = ['north', 'west', 'south', 'east', 'up', 'down']


while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    print()
    if len(player.current_location.items) > 0:
        print("The following items are in the room:")
        for item in player.current_location.items:
            print(item.name)
        print()
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            if next_room is None:
                raise AttributeError
            player.move(next_room)
        except AttributeError:
            print("That path does not exist")
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Found")
