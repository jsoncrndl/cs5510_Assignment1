from KeyboardInputDriver import KeyboardInput
from ControllerInputDriver import ControllerInput
from Car import Car

def drive_forward():
    car.control_car(car.power, car.power)
def turn_left():
    car.control_car(-car.power, car.power)
def turn_right():
    car.control_car(car.power, -car.power)
def drive_backward():
    car.control_car(-car.power, -car.power)


if __name__ == '__main__':
    car = Car()
    keyboardInput = KeyboardInput()
    keyboardInput.add_press_listener('w', drive_forward)
    keyboardInput.add_press_listener('a', turn_left)
    keyboardInput.add_press_listener('s', drive_backward)
    keyboardInput.add_press_listener('d', turn_right)

    controllerInput = ControllerInput()