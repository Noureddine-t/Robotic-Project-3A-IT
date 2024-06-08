from PyQt6.QtCore import QSize, Qt, QTimer
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QGridLayout, QHBoxLayout, QLabel
from src.Controller.MartyController import MartyController
from src.DummyMarty import DummyMarty


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Marty Control")
        self.controller = MartyController()

        # self.controller = DummyMarty()

        # Create a QLabel for the battery percentage
        self.battery_label = QLabel()
        self.update_battery_label()
        battery_layout = QHBoxLayout()
        battery_layout.addWidget(self.battery_label)
        self.color_label = QLabel()  # Create a QLabel for the color
        # Create a QTimer instance to update the battery label every second
        self.color_timer = QTimer()
        self.color_timer.timeout.connect(self.update_color_label)
        self.color_timer.start(1000)  # Update every second
        # Create a QGridLayout instance for arrow buttons
        grid_layout = QGridLayout()
        self.btn_forward = QPushButton("\u2191")  # Up arrow
        self.btn_backward = QPushButton("\u2193")  # Down arrow
        self.btn_right = QPushButton("\u2192")  # Right arrow
        self.btn_left = QPushButton("\u2190")  # Left arrow
        self.btn_turn_left = QPushButton("\u2196")  # Up-left arrow
        self.btn_turn_right = QPushButton("\u2197")  # Up-right arrow
        grid_layout.addWidget(self.btn_forward, 0, 1)
        grid_layout.addWidget(self.btn_backward, 2, 1)
        grid_layout.addWidget(self.btn_right, 1, 2)
        grid_layout.addWidget(self.btn_left, 1, 0)
        grid_layout.addWidget(self.btn_turn_left, 0, 0)
        grid_layout.addWidget(self.btn_turn_right, 0, 2)
        # Set the size and style of the buttons
        button_size = QSize(50, 50)
        button_style = "QPushButton { background-color: black; }"
        self.btn_forward.setFixedSize(button_size)
        self.btn_backward.setFixedSize(button_size)
        self.btn_right.setFixedSize(button_size)
        self.btn_left.setFixedSize(button_size)
        self.btn_turn_left.setFixedSize(button_size)
        self.btn_turn_right.setFixedSize(button_size)

        self.btn_forward.setStyleSheet(button_style)
        self.btn_backward.setStyleSheet(button_style)
        self.btn_right.setStyleSheet(button_style)
        self.btn_left.setStyleSheet(button_style)
        self.btn_turn_left.setStyleSheet(button_style)
        self.btn_turn_right.setStyleSheet(button_style)

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
        vbox_layout.insertLayout(0, battery_layout)  # Insert the battery layout at the top
        vbox_layout.addWidget(self.color_label)  # Add the color label to the layout

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

        # Connect each button to a method in the controller
        self.btn_forward.clicked.connect(self.controller.move_forward)
        self.btn_backward.clicked.connect(self.controller.move_backward)
        self.btn_right.clicked.connect(self.controller.right_side_step)
        self.btn_left.clicked.connect(self.controller.left_side_step)
        self.btn_eyes.clicked.connect(self.controller.angry_eyes)
        self.btn_dance.clicked.connect(self.controller.dance)
        self.btn_celebrate.clicked.connect(self.controller.celebrate)
        self.btn_close.clicked.connect(self.controller.close)
        self.btn_turn_left.clicked.connect(self.controller.turn_left)
        self.btn_turn_right.clicked.connect(self.controller.turn_right)
        # Create a QWidget and set it as the central widget
        widget = QWidget()
        widget.setLayout(hbox_layout)
        self.setCentralWidget(widget)

        self.setFixedSize(QSize(600, 300))  # Change the window size
        self.setStyleSheet("background-color: lightblue;")  # Set the background color to light blue

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Z:
            self.controller.move_forward()
        elif event.key() == Qt.Key.Key_S:
            self.controller.move_backward()
        elif event.key() == Qt.Key.Key_D:
            self.controller.right_side_step()
        elif event.key() == Qt.Key.Key_Q:
            self.controller.left_side_step()

    def update_battery_label(self):
        battery_percentage = self.controller.battery_percentage()
        self.battery_label.setText(f"Battery: {battery_percentage}%")

    def update_color_label(self):
        color = self.controller.get_color()
        self.color_label.setText(f"Color: {color}")



