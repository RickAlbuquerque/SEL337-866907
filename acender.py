from gpiozero import LED

import sys

import time

import math

red = LED(15)

x=[]

for i in range(2):
	x.append(0)

try:
	entrada=int(input("Digite o tempo em segundos: "))
	if entrada<0:
		raise ValueError
except ValueError:
	print("formato inválido")
	sys.exit()

x[1] = math.floor(entrada / 60)
x[0] = entrada - x[1]*60

while True:
	formatado = f"{x[1]:02d}:{x[0]:02d}"
	print(formatado)

	if x[1]==0 and x[0]==0:
		print("término do tempo")
		red.on()
		time.sleep(2)
		try:
			while True:
				pass
		except KeyboardInterrupt:
			GPIO.cleanup()
	time.sleep(1)
	x[0]=x[0]-1

	if x[0]==-1:
		x[0]=59
		x[1]=x[1]-1
