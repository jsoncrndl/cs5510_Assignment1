from pynput import keyboard

class KeyboardInput:

    def __init__(self):
        self.listener = keyboard.Listener(
        on_press=self.on_press,
        on_release=self.on_release)
        self.listeners = {}

    def on_press(self, key):
        for input, value in self.listeners.items():
            if key == input: 
                value()
                return

    def on_release(self, key):
        if key.char in "wasd":
            self.car.control_car(0, 0)

    def add_press_listener(self, key, function):
        pass
    def add_release_listener(self, key, function):
        pass

    def enable(self, isOn):
        if isOn:
            self.listener.start()
        else:
            self.listener.stop()

    # ...or, in a non-blocking fashion: