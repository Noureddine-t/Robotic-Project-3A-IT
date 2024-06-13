from src.Controller.MartyController import MartyController

'''def get_color(marty):
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
my_marty1.connect("192.168.0.106")
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
        robot.celebrate()'''
'''from Controller.MartyController import MartyController


def get_color(marty):
    return marty.get_color()


def move(marty):
    color = marty.get_color()
    if color == "green":
        marty.move_forward()
    elif color == "dark_blue":
        marty.right_side_step()
    elif color == "pink":
        marty.left_side_step()
    elif color == "yellow":
        marty.move_backward()
    marty.stop()


my_marty1 = MartyController()

colors = []
start_color = get_color(my_marty1)
if get_color(my_marty1) == "light_blue":
    print("***" + get_color(my_marty1))

    my_marty1.move_forward()
    while get_color(my_marty1) != "red":
        print("***" + get_color(my_marty1))

        move(my_marty1)

        color = get_color(my_marty1)
        if color != "black":
            colors.append(color)

if get_color(my_marty1) == "red":
    my_marty1.celebrate()'''

"""
def get_color(marty):
    return marty.get_color()


def move(marty, color):
    if color == "green":
        marty.move_forward()
    elif color == "dark_blue":
        marty.right_side_step()
    elif color == "pink":
        marty.left_side_step()
    elif color == "yellow":
        marty.move_backward()
    marty.stop()


def traverse_grid(marty):
    colors = []

    # Avancer 2 fois et enregistrer les couleurs
    for _ in range(2):
        color = get_color(marty)
        colors.append(color)
        marty.move_forward()
    color = get_color(marty)
    colors.append(color)
    # Tourner à gauche
    marty.left_side_step()

    # Reculer 2 fois et enregistrer les couleurs
    for _ in range(2):
        color = get_color(marty)
        colors.append(color)
        marty.move_backward()

    color = get_color(marty)
    colors.append(color)
    # Tourner à gauche
    marty.left_side_step()

    # Avancer 2 fois et enregistrer les couleurs
    for _ in range(2):
        color = get_color(marty)
        colors.append(color)
        marty.move_forward()
    color = get_color(marty)
    colors.append(color)
    return colors


def replay_moves(marty, colors):
    for color in colors:
        move(marty, color)


my_marty1 = MartyController()
my_marty1.connect("192.168.0.102")

colors_recorded = traverse_grid(my_marty1)
print("Colors recorded:", colors_recorded)

# Replay moves if the initial color is ligh_blue
start_color = get_color(my_marty1)
if start_color == "light_blue":
    replay_moves(my_marty1, colors_recorded)
    my_marty1.celebrate()
"""


def get_color(marty):
    return marty.get_color()


def move(marty, direction):
    if direction == "forward":
        marty.move_forward()
    elif direction == "backward":
        marty.move_backward()
    elif direction == "left":
        marty.left_side_step()
    elif direction == "right":
        marty.right_side_step()
    marty.stand_up()


def color_move(marty, color):
    if color == "light_blue":
        marty.move_forward()
    if color == "green":
        marty.move_forward()
    elif color == "dark_blue":
        marty.right_side_step()
    elif color == "pink":
        marty.left_side_step()
    elif color == "yellow":
        marty.move_backward()
    elif color == "red":
        my_marty1.celebrate()
    marty.stand_up()


def traverse_grid_parallel(marty1, marty2):
    grid1 = [
        ["black", "black", "black"],
        ["black", "black", "black"],
        ["black", "black", "black"]
    ]
    grid2 = [
        ["black", "black", "black"],
        ["black", "black", "black"],
        ["black", "black", "black"]
    ]

    directions = [
        ("forward", (0, 1)), ("forward", (0, 1)), ("left", (1, 0)),
        ("backward", (0, -1)), ("backward", (0, -1)), ("left", (1, 0)),
        ("forward", (0, 1)), ("forward", (0, 1))
    ]

    m1_x, m1_y = 0, 0
    m2_x, m2_y = 0, 0

    for move_direction, (dx, dy) in directions:
        color1 = get_color(marty1)
        color2 = get_color(marty2)

        grid1[m1_x][m1_y] = color1
        grid2[m2_x][m2_y] = color2

        move(marty1, move_direction)
        move(marty2, move_direction)

        m1_x += dx
        m1_y += dy
        m2_x += dx
        m2_y += dy

    # Get the final color for both robots
    color1 = get_color(marty1)
    color2 = get_color(marty2)

    grid1[m1_x][m1_y] = color1
    grid2[m2_x][m2_y] = color2

    return grid1, grid2


def merge_color_grids(grid1, grid2):
    merged_grid = [
        ["black", "black", "black"],
        ["black", "black", "black"],
        ["black", "black", "black"]
    ]

    for i in range(3):
        for j in range(3):
            if grid1[i][j] == "black":
                merged_grid[i][j] = grid2[i][j]
            elif grid2[i][j] == "black":
                merged_grid[i][j] = grid1[i][j]
            elif grid1[i][j] == grid2[i][j]:
                merged_grid[i][j] = grid1[i][j]
            else:
                merged_grid[i][j] = grid1[i][j]  # or grid2[i][j], depending on preference
    return merged_grid


def replay_moves(marty, grid):
    directions = [
        ("forward", (0, 1)), ("forward", (0, 1)), ("left", (1, 0)),
        ("backward", (0, -1)), ("backward", (0, -1)), ("left", (1, 0)),
        ("forward", (0, 1)), ("forward", (0, 1))
    ]

    m_x, m_y = 0, 0
    for move_direction, (dx, dy) in directions:
        color = grid[m_x][m_y]
        move(marty, color)
        m_x += dx
        m_y += dy

    # Get the final color and move
    color = grid[m_x][m_y]
    move(marty, color)


# Initialisation des robots
my_marty1 = MartyController()
my_marty2 = MartyController()

my_marty1.connect("192.168.0.102")
my_marty2.connect("192.168.0.103")

# Traverser les grilles avec les deux robots en parallèle
grid1, grid2 = traverse_grid_parallel(my_marty1, my_marty2)
print("Grid recorded by Marty1:", grid1)
print("Grid recorded by Marty2:", grid2)

# Fusionner les grilles de couleurs
final_grid = merge_color_grids(grid1, grid2)
print("Final merged grid:", final_grid)

# Rejouer le chemin avec le premier robot si la couleur initiale est light_blue
start_color = get_color(my_marty1)
if start_color == "light_blue":
    replay_moves(my_marty1, final_grid)
