from martypy import Marty


class MartyController:
    def __init__(self):
        self.my_marty = Marty("wifi", "192.168.0.101")

    # connection
    def connect(self, ip_addr):
        self.my_marty = Marty("wifi", ip_addr)

    def close(self):
        self.my_marty.close()

    # movement
    def move_forward(self):
        self.my_marty.walk(num_steps=8)
        self.my_marty.stand_straight()

    def move_backward(self):
        self.my_marty.walk(num_steps=8, step_length=-25)
        self.my_marty.stand_straight()

    def right_side_step(self):
        self.my_marty.sidestep("right", 7)
        self.my_marty.stand_straight()

    def left_side_step(self):
        self.my_marty.sidestep("left", 7)
        self.my_marty.stand_straight()

    def turn_right(self):
        self.my_marty.walk(turn=-15)

    def turn_left(self):
        self.my_marty.walk(turn=15)

    def stand_up(self):
        self.my_marty.stand_straight()

    # manage eyes
    def angry_eyes(self):
        self.my_marty.eyes('angry')

    def excited_eyes(self):
        self.my_marty.eyes('excited')

    def wiggle_eyes(self):
        self.my_marty.eyes('wiggle')

    def normal_eyes(self):
        self.my_marty.eyes('normal')

    def wide_eyes(self):
        self.my_marty.eyes('wide')

    # actions
    def dance(self):
        self.my_marty.dance()

    def celebrate(self):
        self.my_marty.celebrate()

    def stop(self):
        self.my_marty.stop()

    # sensor
    def distance_sensor(self):
        distance = self.my_marty.get_distance_sensor()
        return distance

    def get_color(self):
        hex_color = str(self.my_marty.get_color_sensor_hex("LeftColorSensor"))
        red = int(hex_color[0:2], 16)
        green = int(hex_color[2:4], 16)
        blue = int(hex_color[4:6], 16)

        color_ranges = {
            "red": {"r": 107, "g": 18, "b": 21, "tolerance": 13},
            "green": {"r": 42, "g": 37, "b": 29, "tolerance": 13},
            "yellow": {"r": 240, "g": 94, "b": 50, "tolerance": 13},
            "black": {"r": 19, "g": 10, "b": 8, "tolerance": 13},
            "dark_blue": {"r": 29, "g": 18, "b": 25, "tolerance": 13},
            "light_blue": {"r": 66, "g": 8650, "b": 84, "tolerance": 13},
            "pink": {"r": 123, "g": 26, "b": 40, "tolerance": 13},
        }

        for color, values in color_ranges.items():
            if (within_tolerance(red, values["r"], values["tolerance"]) and
                    within_tolerance(green, values["g"], values["tolerance"]) and
                    within_tolerance(blue, values["b"], values["tolerance"])):
                return color
        return "unknown"

    def battery_percentage(self):
        battery_percentage = self.my_marty.get_battery_remaining()
        return battery_percentage


def within_tolerance(value, target, tolerance):
    return abs(value - target) <= tolerance
