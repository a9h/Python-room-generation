import random
import time
class generation:
    def __init__(self,doors):
        self.doors = doors

generator = generation(0)
def e():
    generator.doors = random.randint(1,3)
    print(generator.doors)

e()
time.sleep(4)
e()
