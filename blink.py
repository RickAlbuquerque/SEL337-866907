from gpiozero import LED
import time

red = LED(15)

while True:
	red.on()
	time.sleep(0.5)
	red.off()
	time.sleep(0.5)
