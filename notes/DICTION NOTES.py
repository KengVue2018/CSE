states = {
    "CA": "California",

    "FL": "Florida",

    "AK": "Alaska",

    "GA": "Georgia"
}

print(states["CA"])
print(states["AK"])

nested_dictional = {
    "CA": {
        "NAME": "CALIFORNIA",
        "POPULAION": 39500000
    },

    "FL": {
        "NAME": "FLORIDA",
        "POPULATION": 21300000
    },

    "AK": {
        "NAME": "ALASKA",
        "POPLUATION": 737000
    },

    "GA": {
        "NAME": "GEROGIA",
        "POPULATION": 10500000
    }
}

print(nested_dictional["GA"]["POPULATION"])
print(nested_dictional["FL"]["NAME"])

gerogia = nested_dictional["GA"]
print(gerogia)

complex_dictional = {
    "CA": {
        "NAME": "CALIFORNIA",
        "POPULAION": 39500000,
        "CITIES": [
            "Fresno",
            "San Francisco",
            "Los Angeles"
        ]
    },

    "FL": {
        "NAME": "FLORIDA",
        "POPULATION": 21300000,
        "CITIES": [
            "Miami",
            "Orlando",
            "Tampa",
            "Jacksonville"
        ]
    },

    "AK": {
        "NAME": "ALASKA",
        "POPLUATION": 737000,
        "CITIES": [
            "Anchorage",
            "Fairbanks",
            "Juneau"
        ]
    },

    "GA": {
        "NAME": "GEROGIA",
        "POPULATION": 10500000,
        "CITIES": [
            "Atlanta",
            "Savannah",
            "Augusta"
        ]
    }
}

print(complex_dictional["AK"]["CITIES"][0])


print(complex_dictional["FL"]["NAME"])
print(complex_dictional["GA"]["CITIES"][0])


print(complex_dictional.keys())


print(complex_dictional.items())
print(nested_dictional.items())

for key, value in complex_dictional.items():
    print(key)
    print(value)
    print("-" * 20)

# This is where it looks pretty
print()
for state, info in complex_dictional.items():
    for label, stats in info.items():
        print(label)
        print(stats)
        print("-" * 20)
    print("=" * 20)

# Other Notes
states["AR"] = "Arizona?" # It isn't Arizona,

states["AR"] = "Arkansas" # FIxed it
print(states['AR'])