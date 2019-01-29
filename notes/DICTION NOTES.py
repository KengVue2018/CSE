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
