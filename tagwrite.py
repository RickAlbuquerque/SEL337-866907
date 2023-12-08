#Arquivo para gravar tag

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)

leitor = SimpleMFRC522()

texto = "Tag de 866907"

print("Aproxime a tag para gravar.")
leitor.write(texto)
print("Done!")
