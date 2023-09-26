from pynput import keyboard
from car import Car

class InputDriver:

    def __init__(self, car)
        self.car = car
        self.listener = keyboard.Listener(
        on_press=self.on_press,
        on_release=self.on_release)

    def on_press(self, key):
        if key.char == 'a':
            print("Rotate left")
            self.car.control_car(-self.car.power, self.car.power)
        elif key.char == 'd':
            print("Rotate right")
            car.control_car(self.car.power, -self.car.power)
        elif key.char == 'w':
            print("Forward")
            self.car.control_car(self.car.power, self.car.power)
        elif key.char == 's':
            print("Backwards")
            self.car.control_car(-self.car.power, -self.car.power)

    def on_release(self, key):
        if key.char in "wasd"
            self.car.control_car(0, 0)

    def enable(self, isOn):
        if isOn:
            self.listener.start()
        else:
            self.listener.stop()

    # ...or, in a non-blocking fashion: