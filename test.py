from martypy import Marty

my_marty = Marty("wifi", "192.168.0.103")

#my_marty.walk(2, 'auto', 45, 25, 3000)

# my_marty.set_blocking(False)

#my_marty.walk()
# my_marty.arms(100, -100, 500)

# my_marty.eyes("angry", 1000)
# my_marty.eyes("happy", 1000, False)
# my_marty.arms(45, 45, 1000, False)

#my_marty.get_distance_sensor()
#my_marty.get_obstacle_sensor_reading("left")
#my_marty.get_color_sensor_color('left')

hex_color = my_marty.get_color_sensor_hex("left")
print("hex_color: " + hex_color)

color_sensor_val = my_marty.get_color_sensor_value_by_channel("left", "clear")
print("color_sensor_val: " + str(color_sensor_val))

get_ground_sensor = my_marty.get_ground_sensor_reading("left")
print("get_ground_sensor: " + str(get_ground_sensor))

#violet
'''hex_color: 3b1c28
color_sensor_val: 46.0
get_ground_sensor: 36'''
'''hex_color: 391b27
color_sensor_val: 44.0
get_ground_sensor: 35'''

#bleu
'''hex_color: 433a4b
color_sensor_val: 77.0
get_ground_sensor: 41'''
'''hex_color: 433b4c
color_sensor_val: 78.0
get_ground_sensor: 41'''
'''hex_color: 42394b
color_sensor_val: 76.0
get_ground_sensor: 40'''

#jaune