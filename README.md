# cs5510_Assignment1

## Required Dependencies:
* smbus2
* pynput

## Instructions for running program

Connect to the Rasbot using ssh

Add the code to the Rasbot (cloning the repo works well)

Install dependencies in virtual environment

Run `rasbotControl.py` 

## Controls
```
w - move forward
s - move backward
a - rotate left
d - rotate right
q - turn 90 degrees ccw
e - turn 90 degrees cw
r - move in square
```

## Code structure
The main code is located in [rasbot.py](raspbot.py). Input callbacks can be registered using events in the [KeyboardInput](KeyboardInputDriver.py) class. Code to control the car is located in is located in the [Car](Car.py) class.
