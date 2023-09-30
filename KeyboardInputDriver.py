import keyboard

class KeyboardInput:

    def __init__(self):
        keyboard.on_press(callback=self._on_press)
        keyboard.on_release(callback=self._on_press)
        self.listeners = {}
        self.enabled = False

    def _on_press(self, key):
        if self.enabled and key.name in self.listeners:
            self.listeners[key.char](True)

    def _on_release(self, key):
        if self.enabled and key.name in self.listeners:
            self.listeners[key.name](False)

    def add_listener(self, key, function):
        self.listeners[key] = function

    def enable(self, isOn = True):
        self.enabled = isOn