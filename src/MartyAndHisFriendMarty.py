from Controller.MartyController import MartyController


def get_color(marty):
    return marty.get_color()


def move(marty):
    color = marty.get_color()
    if color == "light_blue":
        marty.move_forward()
    elif color == "green":
        marty.right_side_step()
    elif color == "yellow":
        marty.left_side_step()
    elif color == "dark_blue":
        marty.move_backward()
    marty.stop()


my_marty1 = MartyController()
my_marty2 = MartyController()
my_marty1.connect("")
my_marty2.connect("")

colors = []
if get_color(my_marty1) == "pink" and get_color(my_marty2) == "pink":
    while get_color(my_marty1) != "red" and get_color(my_marty2) != "red":
        move(my_marty1)
        move(my_marty2)

        for robot in [my_marty1, my_marty2]:
            color = robot.get_color()
            if color != "black":
                colors.append(color)

if get_color == "red":
    for robot in [my_marty1, my_marty2]:
        robot.celebrate()
