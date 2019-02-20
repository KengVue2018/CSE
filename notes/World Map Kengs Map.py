class Room(object):
    def __init__(self, name, north=None, west=None, south=None, east=None):
        self.name = name
        self.north = north
        self.west = west
        self.south = south
        self.east = east


House = Room("It's your house. And you are in it.")
Horse_Pin = Room("Horse_Pin", None, House)

Horse_Pin.north = House

Street = Room("Street", Horse_Pin)

Street.west = House

Orange_Trees = Room("Oranges_Trees", None,  )

