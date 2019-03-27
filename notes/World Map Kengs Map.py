class Room(object):
    def __init__(self, name, description, north=None, west=None, south=None, east=None):
        self.name = name
        self.description = description
        self.north = north
        self.west = west
        self.south = south
        self.east = east


house = Room("House", "It's your house. And you are in it. It is some how very quiet. But you hear noise in the "
                      "direction of west.",
             'Horse_Pin', 'Street', 'Orange_Trees')

horse_pin = Room("Horse_Pin", "Its the Horse Pin. It stinks but it doesn't smell that bad here. "
                 "Looks like there's a path that keep going up north.", 'Garbage', '', 'House')

garbage = Room("Garbage", "This is where the garbage is at. It stink super bad here.", '', '', 'Horse_Pin')

street = Room("Street", "The Street is so empety. Nobody takes this street.", 'Store', '', '', 'House')

orange_trees = Room("Orange_Trees", "Its full of orange trees. Some of them are really good. But looks like there's a"
                    "building to the east.", 'House', '', '', 'Farm')

farm = Room("Farm", "The Farm is full of items, but a lot of them are for farming only.", 'Field', 'Orange_Trees',
            'Slaughter_House', 'Storage_House')

field = Room("Field", "The field is full of corn. But you can barely see anything once your inside it.", 'Pond', '',
             'Farm', '')

storage_house = Room("Storage_House", "There's a lot of stuff in here. But there is also barely any room in here.",
                     'Cow_Pin', 'Farm', '', '')

cow_pin = Room("Cow_Pin", "It smells awful but there are barley any cows here. But the pig pin have more pigs.",
               '', '', 'Cow_Pin', 'Pig_Pin')

pig_pin = Room("Pig_Pin", "Wow this place smells even worst then the cow pin but its very quiet for how much pigs "
                          "that are here.", 'Chicken_Pin', 'Cow_Pin', 'Water_Storage', '')

water_storage = Room("Water_Storage", "There are two big tubes here that holds water here. There is also a "
                                      "car here too.", 'Pig_Pin', '', '', '')

chicken_pin = Room("Chicken_Pin", "It doesn't smell that bad as the other 2 but it sure is louder then the others.",
                   '', 'Apple_Trees', 'Pig_Pin', '')

apple_trees = Room("Apple_Trees", "There are a lot of apple trees here. This could be a good spot to "
                                  "play hide and seek.", '', '', '', 'Chicken_Pin')

store = Room("Store", "There's a lot of good stuff to eat here.", '', '', 'Street', '')


pond = Room("Pond", "It looks like the pond has a pretty clear water but no animals or fish are in there.", '', '',
            'Field', '')
