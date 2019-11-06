# CircuitPython
(CircuitPython assignments)
# This Page Includes...
-[Hello Arduino (and Metro and Mu)](#Hello-Arduino-and-Metro-and-Mu)

-[CircuitPython Servo](#CircuitPython-Servo)

-[CircuitPython LCD](#CircuitPython-LCD)

-[CircuitPython Photointerrupters](#CircuitPython-Photointerrupters)

-[CircuitPython Distance Sensor](#CircuitPython-Distance-Sensor)

-[Classes, Objects, and Modules](#Classes-Objects-and-Modules)

-[Hello VS Code](#Hello-VS-Code)

-[FancyLED](#FancyLED)

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

##### [Link to the code I wrote](https://github.com/cstours08/CircuitPython/blob/master/LCD%20counter%20with%20switch.py)

# CircuitPython Photointerrupters 

## Description
In this project we are given the task of utilizing the "nEw FaNCy" Photointurrupters to count how many times they are inturpted. You get to tell this small machine it's one true purpose and it happily does it till the end of time or it burns out.

## Revelations

- These suckers love to burn out, so if you have power running through them ensure that neither wire is touching the other as this will fry the whole thing and you won't even notice until you have completly altered your already working code
- Soddering is fun, do not TOUCH the metal.
- The the numbers need a little fine tuning to prevent it from counting a gazillion times, just increase or decrease by whole numbers until it goes away.

## Image

<img src="Sketchs/Photointerrupter Image.PNG" width="230">

##### [A link to where you can download the exact fzz (fritzing) file](https://github.com/cstours08/CircuitPython/blob/master/Sketchs/Photointerrupter%20Sketch.fzz)

##### [Link to the code I wrote](https://github.com/cstours08/CircuitPython/blob/master/Photo.py)

# CircuitPython Distance Sensor 

## Description
This assignment was very fun and very satisfying, it involved programming a "Bat" to color coordinate a LED based on the distance the "Bat" sent it. The whole spectrum has to be used and it needs to update roughly 10 times a second, so thats pretty cool. 

## Revelations

- Take pride in your work, this stuff is very complicated and difficult to comprehend correctly, I applaud you. Enjoy the little things.
- Use resitors, preferably the correct resitors if you don't you will be greeted with spotted vision for the next hour or so.

## Image

<img src="Sketchs/DistanceSensor Image.PNG" width="300" height="350">

##### [A link to where you can download the exact fzz (fritzing) file](https://github.com/cstours08/CircuitPython/blob/master/Sketchs/DistanceSensor%20Sketch.fzz)

##### [Link to the code I wrote](https://github.com/cstours08/CircuitPython/blob/master/DistanceSensor.py)

# Classes, Objects, and Modules 

## Description

In this mini project we were required to create seperate a module that we could then import into a code written by ours truly (Dr. Shields) We are not allowed to include/add anything else other then import whatever you named your module. For this assignment we were required to write a module that that tells 2 multi-color LEDs to fade through the different colors of the visible specterum. 

## Revelations 

- Coding is cool, it's much cooler (and easier) if you name your files correctly and appropriately
- Do your best to understand the entrie process, it helps in the long run
- This is codeception, a code connected to another code through another code

## Image

<img src="Sketchs/RGB Image.PNG" width="230">

##### [A link to where you can download the exact fzz (fritzing) file](https://github.com/cstours08/CircuitPython/blob/master/Sketchs/RGB%20Sketch.fzz)

##### [Link to the code I wrote](https://github.com/cstours08/CircuitPython/blob/master/rgb.py)

# Hello VS Code 

## Description

For this realtively small assignment you get to go through the Joyous exsperience of figuring out how to use a glorified GitHub, with fancy buttons and figures and easier to understand. You laern through this assignment how to view folders and upload specific files to your GitHub page without using github!

## Revelations

- I am unsure if this is a common issue but VS code would not save itself to my homescreen and I would have to fish through files until I could find it eventually I simply pinned it to my taskbar for quick and easy access, do this from the begging it saves time
- this platform is incredibly helpful for completing certain tasks, such as writing this, it will show a preview of what your typing and how a reader would view it, so this way you can make easy changes and quick fixes, otherwise this platform is useless. GitHub Bash is faster

## Image

?

# FancyLED 

## Description

This time around we are coding 6 LEDs to blink in a series of patterns in 2 groups, again we get to create and use our own modules which greatly shortens the code and allows reuse of the strennuos portion of writing this code.

## Revelations 

- There is a series of shortcuts you can take throughout this project, only utilize them if you actually understand them
- the Main code is simple, the module is not, ensure yourself ample time to complet every portion of this, simply it by writing seprate values for each combination of lights to simplfy the process. 

## Image

<img src="Sketchs/famcyLED Image.PNG" width="230">

##### [A link to where you can download the exact fzz (fritzing) file](https://github.com/cstours08/CircuitPython/blob/master/Sketchs/famcyLED%20Sketch.fzz)

##### [Link to the code I wrote](https://github.com/cstours08/CircuitPython/blob/master/fancyLED.py)






##### Huzzah!!
