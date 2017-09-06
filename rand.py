import pigpio
import random
import time

class RandomPig:
    def __init__(self, pin):
        self.pi = pigpio.pi()
        self.pin = pin
        self.old_value = 0

    def update_value(self, new_value):
        print(new_value, self.old_value)
        diff = self.old_value - new_value
        for i in range(abs(diff)):
            if diff > 0: # it's positive
                self.set_pin(self.old_value + i)
            else: # it's negative
                self.set_pin(self.old_value - i)

        time.sleep(1)
        self.old_value = new_value
        return abs(diff)

    def set_pin(self, value):
        print('Pin %s at value %d' %(self.pin, value))
        self.pi.set_PWM_dutycycle(self.pin, value)

    def star_loop(self):
        while True:
            new_value = random.randrange(225)
            sleep_time = self.update_value(new_value)
            time.sleep(sleep_time)

for pin in [17, 22, 24]:
    randp = RandomPig(pin)
    randp.star_loop()

pi.stop()
