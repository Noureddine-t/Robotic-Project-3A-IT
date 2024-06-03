import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QTimer

class RobotInterface(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Interface Robot Marty")
        self.setGeometry(100, 100, 800, 400)
        self.setStyleSheet("background-color: #33FFB8;")

        # Styles CSS et couleurs pour les boutons
        button_style = "QPushButton { background-color: %s; border: 2px solid %s; border-radius: 10px; color: #fff; font-size: 18px; padding: 10px; margin: 5px; } QPushButton:hover { background-color: #bbb; } QPushButton:pressed { background-color: #999; }"
        blue_color, green_color, red_color, yellow_color = "#007bff", "#28a745", "#dc3545", "#ffc107"

        # Création des widgets
        self.connect_button = QPushButton("Connecter")
        self.disconnect_button = QPushButton("Déconnecter")
        self.battery_label = QLabel("Battery: 100%")
        self.sensor_color_label = QLabel("Couleur: ")
        self.sensor_distance_label = QLabel("Distance: ")
        self.sensor_obstacle_label = QLabel("Obstacle: ")
        self.btn_forward = QPushButton("↑")
        self.btn_backward = QPushButton("↓")
        self.btn_left = QPushButton("←")
        self.btn_right = QPushButton("→")
        self.btn_eyes = QPushButton("Set Eyes")
        self.btn_dance = QPushButton("Start Dancing")
        self.btn_celebrate = QPushButton("Start Celebrating")
        self.btn_close = QPushButton("Close")

        # Appliquer les styles CSS aux boutons
        def set_button_style(button, color, font_size=16):
            button.setStyleSheet(f"background-color: {color}; color: black; font-size: {font_size}px; padding: 5px; margin: 2px; border-radius: 5px;")

        set_button_style(self.connect_button, green_color)
        set_button_style(self.disconnect_button, red_color)

        set_button_style(self.btn_forward, blue_color, 25)
        set_button_style(self.btn_backward, blue_color, 25)
        set_button_style(self.btn_left, blue_color, 25)
        set_button_style(self.btn_right, blue_color, 25)

        for button in [self.btn_eyes, self.btn_dance, self.btn_celebrate, self.btn_close]:
            button.setStyleSheet(button_style % (yellow_color, yellow_color))

        # Réduire la taille de la police et fixer la taille des boutons de déplacement
        font = QFont()
        font.setPointSize(20)
        for button in [self.btn_forward, self.btn_backward, self.btn_left, self.btn_right]:
            button.setFont(font)
            button.setFixedSize(70, 70)

        # Mise en page pour les boutons de déplacement
        move_buttons_layout = QVBoxLayout()
        move_buttons_layout.addWidget(self.btn_forward)
        move_buttons_layout.addWidget(self.btn_backward)
        horizontal_buttons_layout = QHBoxLayout()
        horizontal_buttons_layout.addWidget(self.btn_left)
        horizontal_buttons_layout.addLayout(move_buttons_layout)
        horizontal_buttons_layout.addWidget(self.btn_right)

        # Mise en page pour les autres boutons
        other_buttons_layout = QVBoxLayout()
        for button in [self.btn_eyes, self.btn_dance, self.btn_celebrate, self.btn_close]:
            other_buttons_layout.addWidget(button)

        # Mise en page pour la connexion/déconnexion et les informations des capteurs
        info_layout = QVBoxLayout()
        for widget in [self.connect_button, self.disconnect_button, self.battery_label, self.sensor_color_label, self.sensor_distance_label, self.sensor_obstacle_label]:
            info_layout.addWidget(widget)

        # Créer des espaces entre les éléments
        main_layout = QHBoxLayout()
        main_layout.addLayout(horizontal_buttons_layout)
        main_layout.addSpacing(150)
        main_layout.addLayout(other_buttons_layout)
        main_layout.addSpacing(150)
        main_layout.addLayout(info_layout)

        # Appliquer la mise en page principale à la fenêtre
        self.setLayout(main_layout)

        # Configurer le timer pour mettre à jour les valeurs périodiquement
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_sensor_values)
        self.timer.start(10000)

        # Connecter les boutons à leurs fonctions respectives
        self.connect_button.clicked.connect(self.connect_robot)
        self.disconnect_button.clicked.connect(self.disconnect_robot)
        self.btn_forward.clicked.connect(self.move_up)
        self.btn_backward.clicked.connect(self.move_down)
        self.btn_left.clicked.connect(self.move_left)
        self.btn_right.clicked.connect(self.move_right)
        self.btn_eyes.clicked.connect(self.set_eyes)
        self.btn_dance.clicked.connect(self.start_dancing)
        self.btn_celebrate.clicked.connect(self.start_celebrating)
        self.btn_close.clicked.connect(self.close_application)

    def get_battery_level(self):
         return "Battery: 88%"

    def get_sensor_color(self):
        return "Couleur: Rouge"

    def get_sensor_distance(self):
        return "Distance: 15 cm"

    def get_sensor_obstacle(self):
        return "Obstacle: Oui"

    def update_sensor_values(self):
        self.battery_label.setText(self.get_battery_level())
        self.sensor_color_label.setText(self.get_sensor_color())
        self.sensor_distance_label.setText(self.get_sensor_distance())
        self.sensor_obstacle_label.setText(self.get_sensor_obstacle())

    # Méthodes pour les actions des boutons
    def connect_robot(self):
        print("Connecting to the robot...")

    def disconnect_robot(self):
        print("Disconnecting from the robot...")

    def move_up(self):
        print("Moving up...")

    def move_down(self):
        print("Moving down...")

    def move_left(self):
        print("Moving left...")

    def move_right(self):
        print("Moving right...")

    def set_eyes(self):
        print("Setting eyes...")

    def start_dancing(self):
        print("Starting dance...")

    def start_celebrating(self):
        print("Starting celebration...")

    def close_application(self):
        print("Closing application...")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    interface = RobotInterface()
    interface.show()
    sys.exit(app.exec())