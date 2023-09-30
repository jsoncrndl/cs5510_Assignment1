from pynput import keyboard

class KeyboardInput:

    def __init__(self):
        self.listener = keyboard.Listener(
        on_press=self._on_press,
        on_release=self._on_release)
        self.listeners = {}

    def _on_press(self, key):
        if hasattr(key, "char") and key.char in self.listeners:
            self.listeners[key.char](True)

    def _on_release(self, key):
        if hasattr(key, "char") and key.char in self.listeners:
            self.listeners[key.char](False)

    def add_listener(self, key, function):
        self.listeners[key] = function

    def enable(self, isOn = True):
        if isOn:
            self.listener.start()
        else:
            self.listener.stop()

    # ...or, in a non-blocking fashion: