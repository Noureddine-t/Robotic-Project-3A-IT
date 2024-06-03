from PyQt6.QtCore import Qt


class MartyController:
    def __init__(self, marty):
        self.my_marty = marty

    def move_forward(self):
        self.my_marty.walk()

    def move_backward(self):
        self.my_marty.walk(step_length=-20)

    def right_side_step(self):
        self.my_marty.sidestep("right", 4)

    def left_side_step(self):
        self.my_marty.sidestep("left", 4)

    def turn_right(self):
        self.my_marty.walk(turn=-15)

    def turn_left(self):
        self.my_marty.walk(turn=15)

    def manage_eyes(self):
        self.my_marty.eyes('angry', 2, False)

    def dance(self):
        self.my_marty.dance()

    def celebrate(self):
        self.my_marty.celebrate()

    def key_press_event(self, event):
        if event.key() == Qt.Key.Key_Z:
            self.move_forward()
        elif event.key() == Qt.Key.Key_S:
            self.move_backward()
        elif event.key() == Qt.Key.Key_D:
            self.right_side_step()
        elif event.key() == Qt.Key.Key_Q:
            self.left_side_step()

    def close(self):
        self.my_marty.close()

    def baterry_percentage(self):
        battery_percentage = self.my_marty.get_battery_remaining()
        return battery_percentage
