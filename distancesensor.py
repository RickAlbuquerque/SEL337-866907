from gpiozero import DistanceSensor, LED
import time

led = LED(18)

sensor = DistanceSensor(echo=7, trigger=8)# pinos da Rasp. escolhidos 8 e 23
while True:
	sensor.when_in_range = led.on
	sensor.when_out_of_range = led.off
	print("distance is:", sensor.distance, "m")
	time.sleep(0.3)
