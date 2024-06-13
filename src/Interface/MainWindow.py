import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, \
    QProgressBar
from PyQt6.QtGui import QFont, QIcon, QColor
from PyQt6.QtCore import QTimer, Qt
from src.Controller.MartyController import MartyController


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Interface Robot Marty")
        self.setGeometry(100, 100, 800, 400)
        self.setStyleSheet("background-color: #61DFD8;")

        # Initialisation du contrôleur Marty
        self.marty_controller = MartyController()

        # Styles CSS et couleurs pour les boutons
        button_style = "QPushButton { background-color: %s; border: 2px solid %s; border-radius: 10px; color: #fff; font-size: 18px; padding: 10px; margin: 5px; } QPushButton:hover { background-color: #bbb; } QPushButton:pressed { background-color: #999; }"
        blue_color, red_color, yellow_color = "#00AF87", "#dc3545", "#269993"

        # Création des widgets
        self.disconnect_button = QPushButton("Déconnecter")
        self.battery_label = QLabel()
        self.battery_progress = QProgressBar()
        self.battery_progress.setRange(0, 100)
        self.battery_progress.setTextVisible(False)
        self.sensor_color_label = QLabel()
        self.sensor_color_square = QLabel()
        self.sensor_color_square.setFixedSize(30, 30)
        self.btn_forward = QPushButton("\u2191")  # Flèche vers le haut
        self.btn_backward = QPushButton("\u2193")  # Flèche vers le bas
        self.btn_left = QPushButton("\u2190")  # Flèche vers la gauche
        self.btn_right = QPushButton("\u2192")  # Flèche vers la droite
        self.btn_turn_left = QPushButton("\u2196")  # Flèche en haut à gauche
        self.btn_turn_right = QPushButton("\u2197")  # Flèche en haut à droite
        self.btn_eyes = QPushButton("Set Eyes")
        self.btn_dance = QPushButton("Start Dancing")
        self.btn_celebrate = QPushButton("Start Celebrating")
        self.btn_close = QPushButton("Close")

        # Appliquer les styles CSS aux boutons
        def set_button_style(button, color, font_size=16):
            button.setStyleSheet(
                f"background-color: {color}; color: black; font-size: {font_size}px; padding: 5px; margin: 2px; border-radius: 5px;")

        set_button_style(self.disconnect_button, red_color)

        set_button_style(self.btn_forward, blue_color, 25)
        set_button_style(self.btn_backward, blue_color, 25)
        set_button_style(self.btn_left, blue_color, 25)
        set_button_style(self.btn_right, blue_color, 25)
        set_button_style(self.btn_turn_left, blue_color, 25)
        set_button_style(self.btn_turn_right, blue_color, 25)

        for button in [self.btn_eyes, self.btn_dance, self.btn_celebrate, self.btn_close]:
            button.setStyleSheet(button_style % (yellow_color, yellow_color))

        # Réduire la taille de la police et fixer la taille des boutons de déplacement
        font = QFont()
        font.setPointSize(20)
        for button in [self.btn_forward, self.btn_backward, self.btn_left, self.btn_right, self.btn_turn_left,
                       self.btn_turn_right]:
            button.setFont(font)
            button.setFixedSize(70, 70)

        # Mise en page pour les boutons de déplacement (QGridLayout)
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.btn_forward, 0, 1)
        grid_layout.addWidget(self.btn_backward, 2, 1)
        grid_layout.addWidget(self.btn_right, 1, 2)
        grid_layout.addWidget(self.btn_left, 1, 0)
        grid_layout.addWidget(self.btn_turn_left, 0, 0)
        grid_layout.addWidget(self.btn_turn_right, 0, 2)

        # Mise en page pour les autres boutons
        other_buttons_layout = QVBoxLayout()
        for button in [self.btn_eyes, self.btn_dance, self.btn_celebrate, self.btn_close]:
            other_buttons_layout.addWidget(button)

        # Mise en page pour la déconnexion et les informations des capteurs
        info_layout = QVBoxLayout()
        battery_layout = QHBoxLayout()
        battery_layout.addWidget(self.battery_label)
        battery_layout.addWidget(self.battery_progress)
        info_layout.addWidget(self.disconnect_button)
        info_layout.addLayout(battery_layout)
        color_layout = QHBoxLayout()
        color_layout.addWidget(self.sensor_color_label)
        color_layout.addWidget(self.sensor_color_square)
        info_layout.addLayout(color_layout)

        # Créer des espaces entre les éléments
        main_layout = QHBoxLayout()
        main_layout.addLayout(grid_layout)
        main_layout.addSpacing(150)
        main_layout.addLayout(other_buttons_layout)
        main_layout.addSpacing(150)
        main_layout.addLayout(info_layout)

        # Appliquer la mise en page principale à la fenêtre
        self.setLayout(main_layout)

        # Configurer le timer pour mettre à jour les valeurs périodiquement
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_sensor_values)
        self.timer.start(1000)

        # Connecter les boutons à leurs fonctions respectives
        self.disconnect_button.clicked.connect(self.disconnect_robot)
        self.btn_forward.clicked.connect(self.marty_controller.move_forward)
        self.btn_backward.clicked.connect(self.marty_controller.move_backward)
        self.btn_left.clicked.connect(self.marty_controller.left_side_step)
        self.btn_right.clicked.connect(self.marty_controller.right_side_step)
        self.btn_turn_left.clicked.connect(self.marty_controller.turn_left)
        self.btn_turn_right.clicked.connect(self.marty_controller.turn_right)
        self.btn_eyes.clicked.connect(self.marty_controller.excited_eyes)  # Changer selon le besoin
        self.btn_dance.clicked.connect(self.marty_controller.dance)
        self.btn_celebrate.clicked.connect(self.marty_controller.celebrate)
        self.btn_close.clicked.connect(self.close_application)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Z:
            self.marty_controller.move_forward()
        elif event.key() == Qt.Key.Key_S:
            self.marty_controller.move_backward()
        elif event.key() == Qt.Key.Key_D:
            self.marty_controller.right_side_step()
        elif event.key() == Qt.Key.Key_Q:
            self.marty_controller.left_side_step()

    def update_sensor_values(self):
        battery_level = self.marty_controller.battery_percentage()
        self.battery_label.setText(f"Battery: {battery_level}%")
        self.battery_progress.setValue(battery_level)

        if battery_level >= 70:
            self.battery_progress.setStyleSheet("QProgressBar::chunk { background-color: #4CAF50; }")
        elif battery_level >= 30:
            self.battery_progress.setStyleSheet("QProgressBar::chunk { background-color: #FFC107; }")
        else:
            self.battery_progress.setStyleSheet("QProgressBar::chunk { background-color: #F44336; }")

        sensor_color = self.marty_controller.get_color()
        self.sensor_color_label.setText(f"Couleur : {sensor_color}")
        color = QColor(sensor_color)
        self.sensor_color_square.setStyleSheet(f"background-color: {color.name()};")

    def disconnect_robot(self):
        print("Disconnecting from the robot...")
        self.marty_controller.close()

    def close_application(self):
        print("Closing application...")
        self.close()


'''if __name__ == "__main__":
    app = QApplication(sys.argv)
    interface = MainWindow()
    interface.show()
    sys.exit(app.exec())'''