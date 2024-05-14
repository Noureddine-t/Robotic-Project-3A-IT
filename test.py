from martypy import Marty

my_marty = Marty("wifi", "192.168.0.100")
my_marty.hello()
my_marty.walk()
my_marty.arms(45, 0-45, 1000)
my_marty.hello()
my_marty.walk(5, "auto", 0, 25, 1500, False)
my_marty.eyes("angry", 1000)
my_marty.eyes("happy", 1000, False)
my_marty.arms(45, 45, 1000, False)
my_marty.arms(100, -100, 1000, False)
my_marty.arms(-100, 100, 1000, False)
my_marty.close()
