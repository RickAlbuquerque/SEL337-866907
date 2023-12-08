from gpiozero import PWMLED
from time import sleep

led = PWMLED(18)

while True:
	i = 0
	for i in range(101):
		led.value = i/100
		sleep(0.1)
