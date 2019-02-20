class Room(object):
    def __init__(self, name, north=None, south=None, east=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east


# Option 1 - Define is we go
R19A = Room("Mr.Wiebe's Room")
parking_lot = Room("parking_lot", None, R19A)

R19A.north = parking_lot


# Option 2 - Set all aat once, modify controller
R19A = Room("Mr.Wiebe's Room", 'parking_lot')
parking_lot = Room("parking_lot", None, "R19A")








