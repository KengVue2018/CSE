class Room(object):
    def __init__(self, name, description, north=None, south=None, east=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []


def move(self, new_location):
    """This moves the player to a new room


    :param new_location: The room object of which you are going to
    """
    self.current_location = new_location


def find_next_room(self, direction):
    """This method searches the current room so see if a room exists in that direction.


    :param direction:The direction you want to move to.
    :return:The Room object if it exists, or None if it does not.
    """
    return getattr(self.current_location, direction)

# This is option 2
# name_of_room = getattr(self.current_location, direction)
# return globals()[name_of_room]

# Option 1 - Define is we go
R19A = Room("Mr.Wiebe's Room")
parking_lot = Room("parking_lot", None, R19A)


R19A.north = parking_lot


# Option 2 - Set all aat once, modify controller
R19A = Room("Mr.Wiebe's Room", 'parking_lot')
parking_lot = Room("parking_lot", None, "R19A")

player = Player(R19A)

playing = True
directions = ['north', 'west', 'south', 'east', 'up', 'down']


while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Found")






