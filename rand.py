import pigpio
import time
import random

pi = pigpio.pi()

i = 0

def light_it_up:
    for pin in [17, 22, 24]:
        pi.set_PWM_dutycycle(pin, random.randrange(225))

while True:
    light_it_up()
    time.sleep(5)

pi.stop()
