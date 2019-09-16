# Corin Saint Ours
# Hello circuit python

import board
import time
import analogio

led = analogio.AnalogOut(board.A0)
B = 65000
# the value of how bright the light can become
amount = 1000
# the number added to change the B value
#and thus the brightness of the LED
ceiling = 50000
# the highest I allow the value to go,
#this allows the light to flash much more quickly
floor = 20000
# the minium brightness the LED can go, since nothing really happens
# until 20000 I have started the value there to quicken the process
# of the LED changing brightness

while True:
    led.value = B
# sets the LED value to B a.k.a. brightness
    B -= amount
# this begins the process of decreaseing the LED value
    time.sleep(.01)
# a slight delay to prolong the light change
    if B < floor:
# starts the reverse process
        amount = -1000
    elif B > ceiling:
        amount = 1000
    time.sleep(.01)
