from gpiozero import LED
from gpiozero import Button

red = LED(15)

botao = BUTTON(23)

while True:
	if botao:
		rec.toggle()
