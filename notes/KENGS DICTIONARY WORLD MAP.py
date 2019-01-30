world_map = {
    'R19A': {
        'NAME': "MR.Wiebe's Room",
        'DESCRIPTION': "This is the classroom you are in right now."
                       "There are two doors on the right wall",
        'PATHS': {
            'NORTH': "PARKING_LOT",
        }
    }

},

# Controller
playing = True
current_node = world_map['R19A']
while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower()in ['q', 'quit','exit']:
        playing = False



