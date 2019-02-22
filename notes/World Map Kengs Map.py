class Room(object):
    def __init__(self, name, north=None, west=None, south=None, east=None):
        self.name = name
        self.north = north
        self.west = west
        self.south = south
        self.east = east


House = Room("It's your house. And you are in it.")
Horse_Pin = Room("Horse_Pin", north=None)
Street = Room("Street", west=None)
Orange_Trees = Room("Oranges_Trees", south=None)

House.north = Horse_Pin
House.west = Street
House.south = Orange_Trees

Horse_Pin = Room("Its the Horse Pin. It stinks but it doesn't smell that bad here. "
                 "Looks like there's a path that keep going up north.")
Garbage = Room("Garbage", north=None)
House = Room("House", south=None)

Horse_Pin.north = Garbage
Horse_Pin.south = House

Garbage = Room("This is where the garbage is at. It stink super bad here.")
Horse_Pin = Room("Horse_Pin", south=None)

Garbage.south = Horse_Pin

Street = Room("The Street is so empety. Nobody takes this street.")
Store = Room("Store", north=None)
House = Room("House", east=None)

Street.north = Store
Street.east = House

Orange_Trees = Room("Its full of orange trees. Some of them are really good. But looks like theres a"
                    "building to the east.")

Farm = Room("Farm", east=None)
House = Room("House", north=None)

Farm = Room("The Farm is full of items, but a lot of them are for farming only.")
Field = Room("Field", north=None)
Orange_Trees = Room("Orange_Trees", west=None)
Slaughter_House = Room("Slaughter_House", south=None)
Storage_House = Room("Storage_House", east=None)

Farm.north = Field
Farm.west = Orange_Trees
Farm.south = Slaughter_House
Farm.east = Storage_House

Field = Room("The field is full of corn. But you can barely see anything once your inside it.")
Pond = Room("Pond", south=None)

Field.south = Pond

Storage_House = Room("There's a lot of stuff in here. But there is also barely any room in here.")
Cow_Pin = Room("Cow_Pin", north=None)
Farm = Room("Farm", west=None)

Storage_House.north = Cow_Pin
Storage_House.west = Farm



