import SPECIAL_Random


class Phone(object):
    def __init__(self, carrier, charge_left=50):
        # There are attributes that a phone has.
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


def smash_phone(self):
    print("SMASH!!!!!!!!")
    print("It broke.")
    self.screen = False


# Initialize Object
my_phone = Phone("AT&T", 100)
your_phone = Phone("Bell", 0)
default_phone = Phone("Verizon")


my_phone.make_call(60)
my_phone.make_call(10)
my_phone.charge(100)
my_phone.make_call(10)
your_phone.smash_phone()
your_phone.make_call(1)


print(SPECIAL_Random.RandomWiebe.my_random())




