import pigpio
import random
import time
import threading

class RandomPig:
    def __init__(self, pin):
        self.pi = pigpio.pi()
        self.pin = pin
        self.old_value = 0
        self.star_loop()

    def update_value(self, new_value):
        print(new_value, self.old_value)
        diff = new_value - self.old_value
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

def start_rand(pin):
    randp = RandomPig(pin)

for pin in [17, 22, 24]:
    t = threading.Thread(target=start_rand, args=(pin,))
    t.deamon = true
    t.start()
