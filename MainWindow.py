import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QGridLayout, QHBoxLayout
from martypy import Marty
from DummyMarty import DummyMarty



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Marty Control")

        self.my_marty = DummyMarty("wifi", "192.168.0.100")
        #self.my_marty = Marty("wifi", "192.168.0.100")
        # Create a QGridLayout instance for arrow buttons
        grid_layout = QGridLayout()
        self.btn_forward = QPushButton("\u2191")  # Up arrow
        self.btn_backward = QPushButton("\u2193")  # Down arrow
        self.btn_right = QPushButton("\u2192")  # Right arrow
        self.btn_left = QPushButton("\u2190")  # Left arrow
        grid_layout.addWidget(self.btn_forward, 0, 1)
        grid_layout.addWidget(self.btn_backward, 2, 1)
        grid_layout.addWidget(self.btn_right, 1, 2)
        grid_layout.addWidget(self.btn_left, 1, 0)

        # Set the size and style of the buttons
        button_size = QSize(50, 50)
        button_style = "QPushButton { background-color: pink; }"
        self.btn_forward.setFixedSize(button_size)
        self.btn_backward.setFixedSize(button_size)
        self.btn_right.setFixedSize(button_size)
        self.btn_left.setFixedSize(button_size)
        self.btn_forward.setStyleSheet(button_style)
        self.btn_backward.setStyleSheet(button_style)
        self.btn_right.setStyleSheet(button_style)
        self.btn_left.setStyleSheet(button_style)

        # Create a QVBoxLayout instance for other buttons
        vbox_layout = QVBoxLayout()
        self.btn_eyes = QPushButton("Set Eyes")
        self.btn_dance = QPushButton("Start Dancing")
        self.btn_celebrate = QPushButton("Start Celebrating")
        self.btn_close = QPushButton("Close")
        vbox_layout.addWidget(self.btn_eyes)
        vbox_layout.addWidget(self.btn_dance)
        vbox_layout.addWidget(self.btn_celebrate)
        vbox_layout.addWidget(self.btn_close)

        # Set the size of the other buttons
        other_button_size = QSize(100, 50)
        self.btn_eyes.setFixedSize(other_button_size)
        self.btn_dance.setFixedSize(other_button_size)
        self.btn_celebrate.setFixedSize(other_button_size)
        self.btn_close.setFixedSize(other_button_size)

        # Create a QHBoxLayout and add the grid and vbox layouts to it
        hbox_layout = QHBoxLayout()
        hbox_layout.addLayout(grid_layout)
        hbox_layout.addLayout(vbox_layout)

        # Connect each button to a method
        self.btn_forward.clicked.connect(self.move_forward)
        self.btn_backward.clicked.connect(self.move_backward)
        self.btn_right.clicked.connect(self.turn_right)
        self.btn_left.clicked.connect(self.turn_left)
        self.btn_eyes.clicked.connect(self.manage_eyes)
        self.btn_dance.clicked.connect(self.dance)
        self.btn_celebrate.clicked.connect(self.celebrate)
        self.btn_close.clicked.connect(self.close)

        # Create a QWidget and set it as the central widget
        widget = QWidget()
        widget.setLayout(hbox_layout)
        self.setCentralWidget(widget)

        self.setFixedSize(QSize(600, 300))  # Change the window size
        self.setStyleSheet("background-color: lightblue;")  # Set the background color to light blue

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
