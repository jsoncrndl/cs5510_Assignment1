from pydualsense import pydualsense, TriggerModes, PlayerID, LedOptions, PulseOptions, Brightness

class ControllerInput:
    def __init__(self):
        self.ds = pydualsense()
        self.controlSchemes = []
        self.currentControlScheme = 0
        self.bindingLookup = {
            'dpad_down': self.ds.dpad_down,
            'dpad_left': self.ds.dpad_left,
            'dpad_right': self.ds.dpad_right,
            'dpad_up': self.ds.dpad_up,
            'left_stick': self.ds.left_joystick_changed,
            'right_stick': self.ds.right_joystick_changed,
            'r1': self.ds.r1_changed,
            'r2': self.ds.r2_changed,
            'r3': self.ds.r3_changed,
            'l1': self.ds.l1_changed,
            'l2': self.ds.l2_changed,
            'l3': self.ds.l3_changed,
            'cross': self.ds.cross_pressed,
            'triangle': self.ds.triangle_pressed,
            'circle': self.ds.circle_pressed,
            'square': self.ds.square_pressed
        }

    def enable(self, isOn = True):
        if isOn:
            self.ds.init()
            self.ds.light.setBrightness(Brightness.low)

            if len(self.controlSchemes) == 0:
                print("ControllerInput should not be enabled without any control schemes")
                return
            self.set_control_scheme(self.currentControlScheme)
            self.ds.triangle_pressed += self._triangle_pressed
        else:
            self.ds.triangle_pressed -= self._triangle_pressed
            self.ds.close()

    def add_control_scheme(self, controlScheme):
        self.controlSchemes.append(controlScheme)

    def set_control_scheme(self, index):
        self._remove_bindings

        print(f"Using control scheme {index}")

        self.currentControlScheme = index
        controlScheme = self.controlSchemes[index]
        
        # Update LED color
        self.ds.light.setColorT(controlScheme.color)

        # Update trigger haptics        
        motorForce = max(0, min(controlScheme.motorForce, 255))

        if controlScheme.motorForce == 0:
            self.ds.triggerL.setMode(TriggerModes.Off)
            self.ds.triggerR.setMode(TriggerModes.Off)
            self.ds.triggerL.setForce(1, 0)
            self.ds.triggerR.setForce(1, 0)
        else:
            self.ds.triggerL.setMode(TriggerModes.Rigid)
            self.ds.triggerR.setMode(TriggerModes.Rigid)
            self.ds.triggerL.setForce(1, motorForce)
            self.ds.triggerR.setForce(1, motorForce)

        # Update bindings
        self._add_bindings()

    def toggle_control_scheme(self):
        index = (self.currentControlScheme + 1) % (len(self.controlSchemes))
        self.set_control_scheme(index)

    def _remove_bindings(self):
        for bindingKey, bindingValue in self.controlSchemes[self.currentControlScheme].bindings.items():
            if not bindingKey in self.bindingLookup:
                continue
            elif bindingKey == "triangle":
                continue
            self.bindingLookup[bindingKey] -= (bindingValue)

    def _add_bindings(self):
        for bindingKey, bindingValue in self.controlSchemes[self.currentControlScheme].bindings.items():
            if not bindingKey in self.bindingLookup:
                print(f"Invalid binding {bindingKey}")
                continue
            elif bindingKey == "triangle":
                print(f"Triangle is reserved for changing control schemes")
                continue
            self.bindingLookup[bindingKey] += (bindingValue)
            print(f"Binding {bindingKey}")

    def _triangle_pressed(self, down):
        if down:
            self.toggle_control_scheme()

    class ControlScheme:
        def __init__(self, bindings, color = (0, 0, 255), motorForce = 255):
            self.color = color
            self.motorForce = motorForce
            self.bindings = bindings