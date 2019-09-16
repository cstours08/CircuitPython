from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import board
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import CursorMode
import digitalio

counter = 0

# Talk to the LCD at I2C address 0x27.
# The number of rows and columns defaults to 4x20, so those
# arguments could be omitted in this case.
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=4, num_cols=20)

pushbutton = DigitalInOut(board.D2)
pushbutton.direction = digitalio.Direction.INPUT
pushbutton.pull = digitalio.Pull.UP

switch = DigitalInOut(board.A1)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

# Start at the second line, fifth column (numbering from zero).

lcd.set_cursor_pos(1, 0)
lcd.print("Btn's Value:")
lcd.print(str(counter))
# Make the cursor visible as a line.
lcd.set_cursor_mode(CursorMode.LINE)
pushbuttonValue = True

while True:

    if switch.value:
        lcd.set_cursor_pos(0, 0)
        lcd.print("Switch State: UP")
        if not pushbutton.value and pushbuttonValue:
            counter = counter + 1
            lcd.set_cursor_pos(1, 0)
            lcd.print("Btn's Value:")
            lcd.set_cursor_pos(1, 12)
            lcd.print(str(counter))
            lcd.print("   ")
    else:
        lcd.set_cursor_pos(0, 0)
        lcd.print("Switch State:DWN")
        if not pushbutton.value and pushbuttonValue:
            counter = counter - 1
            lcd.set_cursor_pos(1, 0)
            lcd.print("Btn's Value:")
            lcd.set_cursor_pos(1, 12)
            lcd.print(str(counter))
            lcd.print("   ")
    pushbuttonValue = pushbutton.value
#    lcd.set_cursor_pos(1, 0)
#    lcd.print("Btn's Value: ")
#    lcd.print(str(counter))