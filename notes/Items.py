class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, sword):
        super(Weapon, self).__init__(sword)
        self.duration = 100
        self.sword = sword
        self.damage = 10

    def __init__(self, shield):
        super(shield, self).__init__(shield)
        self.duration = 100
        self.shield = shield
        self.blocks_damage = 10


class Armor(Item):
    def __init__(self, helmet):
        super(Armor, self).__init__(helmet)
        self.duration = 100
        self.blocks_damage = 10

    def __init__(self, chest_armor):
        super(Armor, self).__init__(chest_armor)
        self.duration = 100
        self.blocks_damage = 25

    def __init__(self, leg_armor):
        super(Armor, self).__init__(leg_armor)
        self.duration = 100
        self.blocks_damage = 25

    def __init__(self, boots):
        super(Armor, self).__init__(boots)
        self.duration = 100
        self.blocks_damage = 10

class Consumables(Item):
    def __init__(self):









