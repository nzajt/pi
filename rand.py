import pigpio
import random
import time
import threading

class RandomPig:
    def __init__(self, pin):
        self.pi = pigpio.pi()
        self.pin = pin
        self.old_value = self.rand()
        self.star_loop()

    def update_value(self, new_value):
        diff = new_value - self.old_value
        current_value = self.old_value
        for i in range(abs(diff)):
            if diff > 0: # it's positive
                current_value = current_value + 1
                self.set_pin(current_value)
            else: # it's negative
                current_value = current_value - 1
                self.set_pin(current_value)
            time.sleep(5)
        self.old_value = new_value

    def set_pin(self, value):
        print('Pin %s at value %d' %(self.pin, value))
        self.pi.set_PWM_dutycycle(self.pin, value)

    def star_loop(self):
        while True:
            new_value = self.rand()
            sleep_time = self.update_value(new_value)

    def rand():
        return random.randrange(225)

def start_rand(pin):
    randp = RandomPig(pin)

for pin in [17, 22, 24]:
    t = threading.Thread(target=start_rand, args=(pin,))
    t.start()
