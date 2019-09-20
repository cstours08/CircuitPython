import board
import digitalio
import time

counter = 0

# Talk to the LCD at I2C address 0x27.
# The number of rows and columns defaults to 4x20, so those
# arguments could be omitted in this case.

photo = digitalio.DigitalInOut(board.D2)
photo.direction = digitalio.Direction.INPUT
photo.pull = digitalio.Pull.UP
intial = time.monotonic()


# Start at the second line, fifth column (numbering from zero).


pushbuttonValue = True

while True:
    now = time.monotonic()
    if now > intial + 4:
        print("Photo Value:", counter)
        intial = now
    if photo.value and not pushbuttonValue:
        counter = counter + 1
    pushbuttonValue = photo.value
#    lcd.set_cursor_pos(1, 0)
#    lcd.print("Btn's Value: ")
#    lcd.print(str(counter))