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
        hex_color = str(self.my_marty.get_color_sensor_hex("LeftColorSensor"))
        red = int(hex_color[0:2], 16)
        green = int(hex_color[2:4], 16)
        blue = int(hex_color[4:6], 16)

        color_ranges = {
            "red": {"r": 110, "g": 19, "b": 20, "tolerance": 10},
            "green": {"r": 40, "g": 35, "b": 26, "tolerance": 10},
            "purple": {"r": 37, "g": 18, "b": 20, "tolerance": 10},
            "yellow": {"r": 242, "g": 94, "b": 49, "tolerance": 10},
            "black": {"r": 21, "g": 10, "b": 8, "tolerance": 10},
            "dark_blue": {"r": 30, "g": 18, "b": 22, "tolerance": 10},
            "light_blue": {"r": 66, "g": 64, "b": 73, "tolerance": 10},
            "pink": {"r": 126, "g": 27, "b": 38, "tolerance": 10},
        }
        for color, values in color_ranges.items():
            if (within_tolerance(red, values["r"], values["tolerance"]) and
                    within_tolerance(green, values["g"], values["tolerance"]) and
                    within_tolerance(blue, values["b"], values["tolerance"])):
                return color
        return "unknown"

    def baterry_percentage(self):
        battery_percentage = self.my_marty.get_battery_remaining()
        return battery_percentage


def within_tolerance(value, target, tolerance):
    return abs(value - target) <= tolerance
