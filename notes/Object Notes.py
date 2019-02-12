class Phone(object):
    def __init__(self, carrier, charge_left):
        # There are sttributes that a phone has.
        # These should be relevant to our process.
        self.screen = True
        self.camera = 2
        self.microphone = True
        self.carrier = carrier
        self.battery_left = charge_left

    def charge(self, time):
        self.battery_left += time
        if self.battery_left > 100:
            self.battery_left = 100

    def make_call(self, duration):
        if not self.screen:
            print("You can't. The phone is dead.")
            return
        battery_loss_per_minute = 5
        self.battery_left -= duration * battery_loss_per_minute
        if self.battery_left < 0:
            self.battery_left = 0
            print("Your phone died during a conversation.")
        elif self.battery_left == 0:
            print("Your phone dies at the end of the conversation.")
        else:
            print("You successfully make the phone call.")
            print("Your phone is now at %s" % self.battery_left)


sy_phone = Phone("AT&T", 100)
your_phone = Phone("Bell", 0)
