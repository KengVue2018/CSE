import random


class Room(object):
    def __init__(self, name, description, north=None, west=None, south=None, east=None, items=None, character=None):
        if items is None:
            items = []
        self.name = name
        self.description = description
        self.north = north
        self.west = west
        self.south = south
        self.east = east
        self.items = items
        self.character = character


class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Rake(Weapon):
    def __init__(self, name):
        super(Rake, self).__init__("Rake", 10)
        self.minimum_damage = 10

    def light_attack(self):
        _number = random.randint(self.minimum_damage, self.minimum_damage)
        if self.damage > 0:
            print("You did", _number)


class BaseballBat(Weapon):
    def __init__(self):
        super(BaseballBat, self).__init__("BaseBall_Bat", 15)
        self.minimum_damage = 15
        self.max_damage = 20

    def light_attack(self):
        _number = random.randint(self.minimum_damage, self.minimum_damage)
        if self.damage > 0:
            print("You swing and you did", _number)

    def heavy_attack(self):
        _number = random.randint(self.minimum_damage, self.max_damage + 1)
        if self.damage > 0:
            print("You swing and you did", _number)


class Hands(Weapon):
    def __init__(self):
        super(Hands, self).__init__("Hands", 5)
        self.minimum_damage = 5

    def light_attack(self):
        _number = random.randint(self.minimum_damage, self.minimum_damage)
        if self.damage > 0:
            print("You did", _number)


class Knife(Weapon):
    def __init__(self, name):
        super(Knife, self).__init__("Knife", 15)
        self.minimum_damage = 15

    def light_attack(self):
        _number = random.randint(self.minimum_damage, self.minimum_damage)
        if self.damage > 0:
            print("You did", _number)


class Sword(Weapon):
    def __init__(self, name):
        super(Sword, self).__init__("Sword", 25)
        self.minimum_damage = 25
        self.max_damage = 30

    def heavy_attack(self):
        _number = random.randint(self.minimum_damage, self.max_damage + 1)
        if self.damage > 0:
            print("You swing and you did", _number)

    def light_attack(self):
        _number = random.randint(self.minimum_damage - 1, self.minimum_damage)
        if self.damage > 0:
            print("You swing and it did", _number)


class Rifle(Weapon):
    def __init__(self, name):
        super(Rifle, self).__init__("Rifle", 35)
        self.max_damage = 35

    def shoot(self):
        _number = random.randint(self.max_damage, self.max_damage)
        if self.damage > 0:
            print("You have fire a shot and you did", _number)


class Shield(Item):
    def __init__(self, shield):
        super(Shield, self).__init__(shield)
        self.duration = 100
        self.blocks_damage = 10
        self.use = False


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


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("%s attacks %s health left." % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" %  (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


class Zombies(object):
    def __init__(self, name):
        super(Zombies, self).__init__(name)
        self.health = 100


class Car(Vehicle):
    def __init__(self, name, milage):
        super(Car, self).__init__(name)
        self.engine_status = False
        self.fuel = 100
        self.milage = milage

    def start_engine(self):
        self.start_engine = True
        print("You can turn the key and the car turns on.")


rake = Rake('Rake')
baseball_bat = BaseballBat()
hands = Hands()
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


house = Room("House", "It's your house. And you are in it. It is some how very quiet. But you hear noise in the "
                      "direction of west.",
             'horse_pin', 'street', 'orange_trees', None, [knife, backpack, rifle, water_bottle])

horse_pin = Room("Horse Pin", "Its the Horse Pin. It stinks but it doesn't smell that bad here. "
                 "Looks like there's a path that keep going up north.", 'garbage', None, 'house', None, [Rake("Rake")])

garbage = Room("Garbage", "This is where the garbage is at. It stink super bad here.", None, None, 'horse pin', None,
               [chest_armor])

street = Room("Street", "The Street is so empty. Nobody takes this street.", 'store', None, None, 'house', [])

orange_trees = Room("Orange Trees", "Its full of orange trees. Some of them are really good. But looks like there's a"
                    "building to the east.", 'house', None, None, 'farm', [Oranges("Oranges")])

farm = Room("Farm", "The Farm is full of items, but a lot of them are for farming only.", 'field', 'orange_trees',
            'slaughter_house', 'storage_house', [Helmet("Helmet"), HealthPotions("HealthPotions")])

field = Room("Field", "The field is full of corn. But you can barely see anything once your inside it.", 'pond', None,
             'farm', None, [Corn("Corn"), rake])

storage_house = Room("Storage House", "There's a lot of stuff in here. But there is also barely any room in here.",
                     'cow_pin', 'farm', None, None, [Sword("Sword"), HealthPotions("HealthPotions"),
                                                     leg_armor, rake])

cow_pin = Room("Cow Pin", "It smells awful but there are barley any cows here. But the pig pin have more pigs.",
               None, None, 'cow_pin', 'pig_pin', [rake])

pig_pin = Room("Pig Pin", "Wow this place smells even worst then the cow pin but its very quiet for how much pigs "
                          "that are here.", 'chicken_pin', 'cow_pin', 'water_storage', None, [])

water_storage = Room("Water Storage", "There are two big tubes here that holds water here. There is also a "
                                      "car here too.", 'pig_pin', None, None, None, [])

chicken_pin = Room("Chicken Pin", "It doesn't smell that bad as the other 2 but it sure is louder then the others.",
                   None, 'apple_trees', 'pig_pin', None, [])

apple_trees = Room("Apple Trees", "There are a lot of apple trees here. This could be a good spot to "
                                  "play hide and seek.", None, None, None, 'chicken_pin', [Apple])

store = Room("Store", "There's a lot of good stuff to eat here. But I don't like the food there.", None,
             None, 'street', None, [])


pond = Room("Pond", "It looks like the pond has a pretty clear water but no animals or fish are in there.", None,
            None, 'field', None, [])

slaughter_house = Room("Slaughter House", "It stinks and there's a lot of blood here. But there is a lot tof weapons "
                                          "here.", 'farm', None, None, None, [knife, rifle, rake])


class Player(object):
    def __init__(self, starting_location, current_class, pick_up, drop, weapon):
        self.health = 100
        self.name = player
        self.current_location = starting_location
        self.player_class = current_class
        self.inventory = []
        self.pick_up = pick_up
        self.drop = drop
        self.weapon = weapon

    def move(self, new_location):
        """This moves the player to a new room

        :param new_location: The variable containing a room object
        """
        if new_location is not None:
            self.current_location = new_location

        else:
            print("You can't go that way.")

    def find_next_room(self, direction):
        """This method searches the current room so see if a room exists in that direction.

        :param self:
        :param direction:The direction you want to move to.
        :return The Room object if it exists, or None if it does not.
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("%s attacks %s health left." % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" %  (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


player = Player(house)

playing = True
directions = ['north', 'west', 'south', 'east', 'up', 'down']
short_directions = ['n', 'w', 's', 'e', 'u', 'd']


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
    if command.lower() in short_directions:
        pos =short_directions.index(command.lower())
        command = directions[pos]
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

    if "Take " in command:
        item_name = command[5:]
        item_object = None

        for item in player.current_location.items:
            if item.name == item_name:
                item_object = item

        if item_object is None:
            player.inventory.append(item_object)
            player.current_location.items.remove(item_object)
            print("You have added to your inventory.")

    if "Drop " in command:
        item_name = command[5:]
        item_object = None

        for item in player.inventory:
             if item.name == item_name:
                 item_object = item

            if item_object is not None:
                player.inventory.remove(item_object)
                player.current_location.items.append(item_object)
                print("1")


