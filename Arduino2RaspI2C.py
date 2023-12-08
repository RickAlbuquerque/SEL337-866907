from smbus import SMBus # importa a classe SMBus

addr = 0x8 # bus address - define o endereço do dispositivo I2C como 0x8h
bus = SMBus(1) # /dev/ic2-1 - inicializa o objeto
flag = True # variv. usada p/ controlar o loop
print ("Digite 1 para ON ou 0 para OFF")

while flag:
	ledstate = input(">>>> ") # solicita entrada no terminal
	if ledstate == "1":
		bus.write_byte(addr, 0x1) # se for 1, escreve 0x1 no endereço
	elif ledstate == "0":
		bus.write_byte(addr, 0x0) # ou escreve 0x0, caso 0
	else:
		flag = False # encerra o loop caso digite algo diferente de 0 ou 1

	data = bus.read_i2c_block_data(0x8, 0, 2) # define o endereço de memoria
	value = data[0]*256+data[1] # define o valor registrado no endereço
	print (value)
