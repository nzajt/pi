import pigpio
import time

pi = pigpio.pi()

i = 0

while i < 225:
    pi.set_PWM_dutycycle(17, i)
    pi.set_PWM_dutycycle(22, i)
    pi.set_PWM_dutycycle(24, i)
    i += 1
    print i
    time.sleep(1)

pi.stop()
