from martypy import Marty

my_marty = Marty("wifi", "192.168.0.104")

my_marty.walk(2, 'auto', 45, 25, 3000)

# my_marty.set_blocking(False)

#my_marty.walk()
# my_marty.arms(100, -100, 500)

# my_marty.hello()
# my_marty.eyes("angry", 1000)
# my_marty.eyes("happy", 1000, False)
# my_marty.arms(45, 45, 1000, False)

#my_marty.get_distance_sensor()
#my_marty.get_obstacle_sensor_reading("left")
#my_marty.get_color_sensor_color('left')

my_marty.get_color_sensor_hex("left")
my_marty.get_color_sensor_value_by_channel("left", "clear")
my_marty.get_ground_sensor_reading("left")

