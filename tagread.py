from mfrc522 import SimpleMFRC522
from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

leitor = SimpleMFRC522()

print("Aproxime tag para leitura.")
while True: #loop

	id, texto = leitor.read()
	print("ID: {}\nTexto: {}".format(id, texto))
	sleep(3)
