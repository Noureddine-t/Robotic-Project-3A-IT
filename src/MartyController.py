from martypy import Marty


class MartyController:
    def __init__(self):
        self.my_marty = Marty("wifi", "192.168.0.103")

    def move_forward(self):
        self.my_marty.walk()

    def move_backward(self):
        self.my_marty.walk(step_length=-20)

    def right_side_step(self):
        self.my_marty.sidestep("right", 2)

    def left_side_step(self):
        self.my_marty.sidestep("left", 2)

    def turn_right(self):
        self.my_marty.walk(turn=-15)

    def turn_left(self):
        self.my_marty.walk(turn=15)

    def manage_eyes(self):
        self.my_marty.eyes('angry')

    def dance(self):
        self.my_marty.dance()

    def celebrate(self):
        self.my_marty.celebrate()

    def close(self):
        self.my_marty.close()

    def stop(self):
        self.my_marty.stop()

    def stand_up(self):
        self.my_marty.stand_straight()

    def get_corlor(self):
        # TODO: define this method
        # color = self.my_marty.get_color()
        hex_color = self.my_marty.get_color_sensor_hex()
        color = int(hex_color, 16)
        return color

    def baterry_percentage(self):
        battery_percentage = self.my_marty.get_battery_remaining()
        return battery_percentage
