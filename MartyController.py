from PyQt6.QtCore import Qt

class MartyController:
    def __init__(self, marty):
        self.my_marty = marty


    def move_forward(self):
        self.my_marty.walk(2, 'auto', 0)

    def move_backward(self):
        self.my_marty.walk(2, 'auto', 180)

    def turn_right(self):
        self.my_marty.walk(2, 'auto', -90)

    def turn_left(self):
        self.my_marty.walk(2, 'auto', 90)

    def manage_eyes(self):
        self.my_marty.eyes('angry', 2, False)

    def dance(self):
        self.my_marty.dance()

    def celebrate(self):
        self.my_marty.celebrate()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Z:
            self.move_forward()
        elif event.key() == Qt.Key.Key_S:
            self.move_backward()
        elif event.key() == Qt.Key.Key_D:
            self.turn_right()
        elif event.key() == Qt.Key.Key_Q:
            self.turn_left()

    def close(self):
        self.my_marty.close()