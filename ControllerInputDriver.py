from pydualsense import pydualsense, TriggerModes

# def cross_pressed(state):
#     print(state)

# ds = pydualsense() # open controller
# ds.init() # initialize controller

# ds.cross_pressed += cross_pressed
# ds.light.setColorI(255,0,0) # set touchpad color to red
# ds.triggerL.setMode(TriggerModes.Rigid)
# ds.triggerL.setForce(1, 255)
# ds.close() # closing the controllerfrom Car import Car

class ControllerInput:

    def __init__(self, car):
        self.car = car
        self.ds = pydualsense()

    def on_press(self, key):
        if key.char == 'a':
            print("Rotate left")
            self.car.control_car(-self.car.power, self.car.power)
        elif key.char == 'd':
            print("Rotate right")
            self.car.control_car(self.car.power, -self.car.power)
        elif key.char == 'w':
            print("Forward")
            self.car.control_car(self.car.power, self.car.power)
        elif key.char == 's':
            print("Backwards")
            self.car.control_car(-self.car.power, -self.car.power)

    def on_release(self, key):
        if key.char in "wasd":
            self.car.control_car(0, 0)

    def enable(self, isOn):
        if isOn:
            self.listener.start()
        else:
            self.listener.stop()


ds = pydualsense()
ds.init()
ds.triggerL.setMode(TriggerModes.Rigid)
ds.triggerL.setForce(1, 255)

while True:
    pass