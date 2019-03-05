class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, sword):
        self.duration = 100
        self.sword = sword
        self.damage = 10


class shield(Item):
    def __init__(self, name, shield):
        super(shield, self).__init__(name)
        self.duration = 100
        self.shield = shield
        self.blocks_damage = 10


class Armor(Item):
    def __init__(self, Helmet):
        super(Armor, self).__init__(Helmet)
        self.duration = 100
        self.blocks_damage = 10

    def __init__(self, Chest_Armor):
        super(Armor, self).__init__(Chest_Armor)
        self.duration = 100
        self.blocks_damage = 25

    def __init__(self, Leg_Armor):
        super(Armor, self).__init__(Leg_Armor)
        self.duration = 100
        self.blocks_damage = 25









