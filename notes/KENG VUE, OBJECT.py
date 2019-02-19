class TV(object):
    def __init__(self, remote, resolution):
        self.button = 5
        self.size = 60
        self.screen = True
        self.controller = remote
        self.resolution = resolution

    def screen(self):
        if not self.screen:
            print("The TV is off. You have to turn it on.")

    def button(self, onButton):
        if self.button:
            onButton







