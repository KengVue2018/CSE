world_map = {
    'HOUSE': {
        'NAME': "My House",
        'DESCRIPTION': "Its your own house",
        'PATHS': {
            'NORTH': "HORSE PIN",
            'WEST': "Steet",
            'SOUTH': "Orange Trees"
        }

    },
    'HORSE PIN': {
        'NAME': "HORSE PIN",
        'DESCRIPTION': "It skinks but it doesn't smell that bad",
        'PATHS': {
            'NORTH': "GARBAGE",
        }
    },
    'GARBAGE': {
        'NAME': "GARBAGE",
        'DESCRIPTION': "Its full of stuff but some stuff isn't that useful",
        'PATHS': {
            'SOUTH': "HORSE PIN"
        }
    },
    'STREET': {
        'NAME': "Street",
        'DESCRITION': "Its kinda dark but theres barley any car that goes on it",
        'PATHS': {
            'NORTH': "STORE",
            'EAST': "HOUSE",
        }
    },
    'ORANGE TREES': {
        'NAME': "ORANGE TREES",
        'DESCRTITION': "Its full of orange trees. Some of them are really good.",
        'PATHS': {
            'EAST': "FARM",
            'NORTH': "HOUSE",
        }
    },
    'FARM': {
        'NAME': "The Farm",
        'DESCRITITTION': "Looks like everything in there are for fariming except this one idem",
        'PATH': {
            'NORTH': "FIELD",
            'WEST': "ORANGE TREES",
            'SOUTH': "Slaughter House",
            'EAST': "STORAGE HOUSE",
        }
    },
    'FIELD': {
        'NAME': "FIELD",
        'DESCRITITION': "Its full of corns and u can't see that well",
        'PATHS': {
            'NORTH': "POND"
        }
    },
    'POND': {
        'NAME': "POND",
        'DESCRITION': "Its kinda dirty but animals still can live there",
        'PATHS': {
            'SOUTH': "FIELD"
        }
    },
    ''
}