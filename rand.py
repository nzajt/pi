import pigpio
import random

pi = pigpio.pi()

i = 0

def light_it_up(pin):
    pi.set_PWM_dutycycle(pin, random.randrange(225))

for pin in [17, 22, 24]:
    while True:
        light_it_up(pin)
        time.sleep(random.randrange(10))

pi.stop()
