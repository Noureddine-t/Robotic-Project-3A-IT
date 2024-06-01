# Fichier dummyMarty.py

class DummyMarty:
    def __init__(self, connection_method, locator):
        print(f"DummyMarty initialized with connection_method={connection_method}, locator={locator}")

    def move_forward(self):
        print("DummyMarty is moving forward")

    def move_backward(self):
        print("DummyMarty is moving backward")

    def right_side_step(self):
        print("DummyMarty is side stepping right")

    def left_side_step(self):
        print("DummyMarty is side stepping left")

    def manage_eyes(self):
        print("DummyMarty's eyes are set")

    def dance(self):
        print("DummyMarty is dancing")

    def celebrate(self):
        print("DummyMarty is celebrating")

    def close(self):
        print("DummyMarty is closing")

    def turn_left(self):
        print("DummyMarty is turning left")

    def turn_right(self):
        print("DummyMarty is turning right")

    def baterry_percentage(self):
        battery_percentage = 100
        return battery_percentage

    def key_press_event(self, event):
        print(f"Key press event: {event}")

