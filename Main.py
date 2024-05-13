from martypy import Marty

my_marty = Marty("wifi", "")

my_marty.hello()
my_marty.__init__("wifi", "")

# avancer
my_marty.walk(5, 'auto', 0)

# reculer
my_marty.walk(5, 'auto', 180)

# tourner a droite
my_marty.walk(5, 'auto', -90)

# tourner a gauche
my_marty.walk(5, 'auto', 90)

# gerer le regard
my_marty.eyes('happy', 1000, False)

# danser
my_marty.dance()

# celebrer
my_marty.celebrate()


niveau_batterie = my_marty.get_battery_remaining()

lecture_obstacle_couleur = my_marty.get_obstacle_sensor_reading()

distance = my_marty.get_distance_sensor()

# flux video
