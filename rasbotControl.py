from KeyboardInputDriver import KeyboardInput
from ControllerInputDriver import ControllerInput
from Car import Car
import time

def drive_forward():
    car.control_car(car.power, car.power)
def turn_left():
    car.control_car(-car.power, car.power)
def turn_right():
    car.control_car(car.power, -car.power)
def drive_backward():
    car.control_car(-car.power, -car.power)

def rotate_90(counterclockwise = False):
    TURN_TIME = 2
    TURN_POWER = 30

    if counterclockwise:
        TURN_POWER * -1

    car.control_car(TURN_POWER, -TURN_POWER)
    time.sleep(TURN_TIME)

def move_square(down = True):
    if not down:
        return

    keyboardInput.enable(False)
    controllerInput.enable(False)
    
    STRAIGHT_TIME = 10
    STRAIGHT_POWER = 30

    for i in range(0, 4):
        car.control_car(STRAIGHT_POWER, STRAIGHT_POWER) #Forward
        time.sleep(STRAIGHT_TIME)
        rotate_90()

car = Car()
keyboardInput = KeyboardInput()
controllerInput = ControllerInput()

def left_stick_drive(x_in, y_in):
    pass

def two_stick_drive(right_stick, y_in):
    if right_stick:
        car.control_car(car.last_left, y_in)
    else:
        car.control_car(y_in, car.last_right)

def stop_on_release(isDown, function):
    if not isDown:
        car.control_car(0, 0)
        return

    function()

if __name__ == '__main__':
    keyboardInput.add_press_listener('w', drive_forward)
    keyboardInput.add_press_listener('a', turn_left)
    keyboardInput.add_press_listener('s', drive_backward)
    keyboardInput.add_press_listener('d', turn_right)
    # keyboardInput.add_press_listener('e', )
    keyboardInput.enable()

    controllerInput.add_control_scheme(ControllerInput.ControlScheme(color=(0, 255, 0), motorForce=255, bindings={
        'dpad_left': lambda isDown: stop_on_release(isDown, turn_left),
        'dpad_right': lambda isDown: stop_on_release(isDown, turn_right),
        'dpad_up': lambda isDown: stop_on_release(isDown, drive_forward),
        'dpad_down': lambda isDown: stop_on_release(isDown, drive_backward),
        'square': move_square
    }))

    controllerInput.add_control_scheme(ControllerInput.ControlScheme(color=(0, 255, 255), motorForce=0, bindings={
        'stick_left': lambda x, y: two_stick_drive(False, y),
        'stick_right': lambda x, y: two_stick_drive(True, y)
    }))

    controllerInput.add_control_scheme(ControllerInput.ControlScheme(color=(255, 255, 0), motorForce=128, bindings={}))
    controllerInput.enable()
    while True:
        pass