class DummyMarty:
    def __init__(self, connection_method, locator):
        print(f"DummyMarty initialized with connection_method={connection_method}, locator={locator}")

    def walk(self, steps, turn_type, angle):
        print(f"DummyMarty is walking with steps={steps}, turn_type={turn_type}, angle={angle}")

    def eyes(self, expression, duration, blocking):
        print(f"DummyMarty's eyes are set to expression={expression}, duration={duration}, blocking={blocking}")

    def dance(self):
        print("DummyMarty is dancing")

    def celebrate(self):
        print("DummyMarty is celebrating")

    def close(self):
        print("DummyMarty is closing")