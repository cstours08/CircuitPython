import digitalio  # pylint: disable-msg=import-error
import time
import random
import board

on = True
off = False

class FancyLED:

    def __init__(self, p1, p2, p3):
        print("(#fancyLED pulp fiction version)")
        print("What does Marcelis Wallis look like?!")
        time.sleep(2)
        self.x1 = digitalio.DigitalInOut(p1)
        self.x1.direction = digitalio.Direction.OUTPUT
        self.y1 = digitalio.DigitalInOut(p2)
        self.y1.direction = digitalio.Direction.OUTPUT
        self.z1 = digitalio.DigitalInOut(p3)
        self.z1.direction = digitalio.Direction.OUTPUT

    def alternate(self):  # 2 LEDs on at same time other off and flip
        print("WHAT? WHAT AINT NO COUNTRY I EVER HEARD OF! (alternate)")
        time.sleep(1)
        print("THEY SPEAK English IN WHAT?")
        time.sleep(1)
        self.x1.value = on
        self.y1.value = off
        self.z1.value = on
        time.sleep(.5)
        self.x1.value = off
        self.y1.value = on
        self.z1.value = off
        time.sleep(.5)
        self.x1.value = off
        self.y1.value = off
        self.z1.value = off

    def blink(self):  # off on off
        print("SAY WHAT AGAIN! (blink)")
        self.x1.value = on
        self.y1.value = on
        self.z1.value = on
        time.sleep(.5)
        self.x1.value = off
        self.y1.value = off
        self.z1.value = off
        time.sleep(1)

    def chase(self):
        print("I DOUBLE DOG DARE YA YOU MOTHERF*KER!")
        time.sleep(1)
        print("SAY WHAT ONE MORE G@DDAM TIME! (chase)")
        time.sleep(.5)
        self.x1.value = on
        self.y1.value = off
        self.z1.value = off
        time.sleep(.5)
        self.x1.value = off
        self.y1.value = on
        self.z1.value = off
        time.sleep(.5)
        self.x1.value = off
        self.y1.value = off
        self.z1.value = on
        time.sleep(.5)
        self.x1.value = off
        self.y1.value = off
        self.z1.value = off

    def sparkle(self):
        for whatever in range(0, 50):
            print("WHAT DOES Marcelis Wallis LOOK LIKE? (sparkle)")
            n = random.randint(1, 3)
            if n == 1:
                self.x1.value = on
                self.y1.value = off
                self.z1.value = off

            elif n == 2:
                self.x1.value = off
                self.y1.value = on
                self.z1.value = off

            elif n == 3:
                self.x1.value = off
                self.y1.value = off
                self.z1.value = on
            time.sleep(.05)
            self.x1.value = off
            self.y1.value = off
            self.z1.value = off