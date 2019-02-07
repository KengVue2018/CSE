world_map = {
    'HOUSE': {
        'NAME': "My House",
        'DESCRIPTION': "Its your own house. You hear horse noises up north, you look out the window and see the street"
                       "which is west from your house, and you also see orange trees to the south.",
        'PATHS': {
            'NORTH': "HORSE PIN",
            'WEST': "STREET",
            'SOUTH': "ORANGE TREES",
        }

    },
    'HORSE PIN': {
        'NAME': "HORSE PIN",
        'DESCRIPTION': "It stinks but it doesn't smell that bad here. Looks like there's a path that keep going up"
                       "north. ",
        'PATHS': {
            'NORTH': "GARBAGE",
            'SOUTH': "HOUSE",
        }
    },
    'GARBAGE': {
        'NAME': "GARBAGE",
        'DESCRIPTION': "Its full of stuff but some stuff isn't that useful in here.",
        'PATHS': {
            'SOUTH': "HORSE PIN"
        }
    },
    'STREET': {
        'NAME': "Street",
        'DESCRIPTION': "Its kinda dark but there's barley any car that pass goes on this street.",
        'PATHS': {
            'NORTH': "STORE",
            'EAST': "HOUSE",
        }
    },
    'ORANGE TREES': {
        'NAME': "ORANGE TREES",
        'DESCRIPTION': "Its full of orange trees. Some of them are really good. Looks like there's a building"
                       "if you go East.",
        'PATHS': {
            'EAST': "FARM",
            'NORTH': "HOUSE",
        }
    },
    'FARM': {
        'NAME': "THE FARM",
        'DESCRIPTION': "Looks like everything item in here are for farming except this one item. There's a big field up"
                       "North, a slaughter house on the south, and a storage house on the east.",
        'PATH': {
            'NORTH': "FIELD",
            'WEST': "ORANGE TREES",
            'SOUTH': "Slaughter House",
            'EAST': "STORAGE HOUSE",
        }
    },
    'FIELD': {
        'NAME': "FIELD",
        'DESCRIPTION': "Its full of corn and u can't see that well. But you hear water up North.",
        'PATHS': {
            'NORTH': "POND"
        }
    },
    'POND': {
        'NAME': "POND",
        'DESCRIPTION': "I wonder if there's any fish or ducks that live hear.",
        'PATHS': {
            'SOUTH': "FIELD"
        }
    },
    'STORAGE HOUSE': {
        'NAME': "STORAGE HOUSE",
        'DESCRIPTION': "Its full of stuff. There's barely any room to move. "
                       "But there are a lot of useful items in here. But you hear a cow outside.",
        'PATHS': {
            'NORTH': "COW PIN",
            'WEST': "FARM",
        }
    },
    'COW PIN': {
        'NAME': "COW PIN",
        'DESCRIPTION': "This area smell awful. But there's barely any cows that's here. Looks like the pigs have more",
        'PATHS': {
            'EAST': "PIG PIN",
            'SOUTH': "STORAGE HOUSE",
        }

    },
    'PIG PIN': {
        'NAME': "Pig Pin",
        'DESCRIPTION': "Wow this area smell even worst then the cow's pin but its very quiet for how many pigs that are"
                       "here.",
        'PATHS': {
            'WEST': "COW PIN",
            'SOUTH': "WATER STORAGE",
            'NORTH': "CHICKEN PIN",
        }
    },
    'WATER STORAGE': {
        'NAME': "THE WATER STORAGE",
        'DESCRIPTION': "There's two big tubes that holds water here. But there looks like a car that is also here.",
        'PATHS': {
            'NORTH': "PIG PIN",
        }
    },
    'CHICKEN PIN': {
        'NAME': "CHICKEN PIN",
        'DESCRIPTION': "Its louder then the cow and pig pin. But it doesn't smell that bad like the other two.",
        'PATHS': {
            'WEST': "APPLE TREES",
            'SOUTH': "PIG PIN",
        }
    },
    'APPLE TREES': {
        'NAME': "Apple trees",
        'DESCRIPTION': "There are a lot of apple trees. This could be a good hiding spot if we play hide and seek.",
        'PATHS': {
            'EAST': "Chicken Pin",
        }
    },
    'STORE': {
        'NAME': "STORE",
        'DESCRIPTION': "There's a lot of good stuff tho eat here.",
        'PATHS': {
            'SOUTH': "STREET",
        }
    },
}

playing = True
current_node = world_map['HOUSE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN', 'RIGHT', 'LEFT']

while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Found")
