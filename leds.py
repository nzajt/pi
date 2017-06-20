import pigpio
import time

pi = pigpio.pi()
pi.set_PWM_dutycycle(17, 225)

time.sleep(25)

pi.close()
