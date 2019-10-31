# CircuitPython
(CircuitPython assignments)
# This Page Includes...
-[Hello Arduino (and Metro and Mu)](#Hello-Arduino-and-Metro-and-Mu)

# Hello Arduino (and Metro and Mu) 

## Description
Makes LED go from on to off in small intervals that are not noticeable to the human eye or it "fades". using a new circuit board known as MetroExpress and (new) origramming system/language known as Circuitpython. Don't worry you'll learn to hate it. 

## Revelations
- Google good, don't be ashamed/afraid to google even the dumbest things
- CircuitPython is difficult to understand, take your time
- Good practice for using "If" and "else" or the dreaded "elif" statements

## Wiring Image

<img src="Sketchs/Hello Arduino Image.PNG" width="250">

##### [A link to where you can download the exact fzz (fritzing) file](https://github.com/cstours08/CircuitPython/blob/master/Sketchs/Hello%20Arduino%20Sketch.fzz)

##### [Link to the code I wrote](https://github.com/cstours08/CircuitPython/blob/master/Hello%20CircuitPython.py)

# CircuitPython Servo 
## Description
This code tells a Servo to move in a direction based on whether or not there is input from 1 of 2 sources. One wire spins one direction the other wire the opposite. 

## Revelations

- Understand your wiring as you do it, don't look at someone's wiring and trust it works, ensure that you understand it.
- Again Google is your friend, especially other github pages. they are treasure troves of information and explanation on certain parts of a code
- Use Dr.shields, if you don't fully understand something look to Dr.shields and he will do his best to help your understading of it

## Image

<img src="Sketchs/Servo Image.PNG" width="250">

##### [A link to where you can download the exact fzz (fritzing) file](https://github.com/cstours08/CircuitPython/blob/master/Sketchs/Servo%20Sketch.fzz)

##### [Link to the code I wrote](https://github.com/cstours08/CircuitPython/blob/master/Circuitpython%20Servo.py)

# CircuitPython LCD

## Description
in this assignment we had to write a program for a LCD screen instructing it to print out the state or status of a switch depending on it's condiguration and a button that counted both up and down depending on the status of the switch. Simply put the switch is in the "UP" position and you click the button and it counts up, if the switch is in the "DWN" position then clicking the button will count down.

## Revelations

- Buttons and LCDs are really cool, throughout this project every minor step was incredibly satisfying, the moment you get it to do exactly what you want and it begins counting it gives a very nice feeling of accomplishment
- Google and the rest of github is your friend (so is Dr. shields), use these resources as much as you want just ensure that you actually learn from using them
- keep very careful track of your if statements they will bite you in the ass if they are even a little off.

## Image

<img src="Sketchs/Lcd Counter with switch Image.PNG" width="270">

##### [A link to where you can download the exact fzz (fritzing) file](https://github.com/cstours08/CircuitPython/blob/master/Sketchs/Lcd%20Counter%20with%20switch%20Sketch.fzz)

##### [Link to the code I wrote]()

	- Circuitpython Servo.py
	This file instructs a servo to turn based from 0 to 180 degrees.

	- LCD counter with switch.py
	This code tells a lcd screen to print out the UP DWN value of a switch 
	and a button value that goes up or dwn depending on the switch value
	when the button is pressed.

	- Photo.py
	This code uses a photo interrupter and counts the number of times a object
	interrupts and then resumes and prints this value every 4 seconds without using
	time.sleep. 

	- fade.py
	makes a small led go from one color to another depeneding on what you have
	set it to
