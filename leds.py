import pigpio
import time

pi = pigpio.pi()

i = 0

def light_it_up(i):
    pi.set_PWM_dutycycle(17, i)
    pi.set_PWM_dutycycle(22, i)
    pi.set_PWM_dutycycle(24, i)

while True:
    i += 5
    if i > 255:
        i = 0
    light_it_up(i)
    print i
    time.sleep(1)

light_it_up(0)
pi.stop()
