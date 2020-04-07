#!/usr/bin/env python
#_*_ coding: utf8 _*_


from time import sleep
import socket, sys, subprocess, argparse, sockets
from datetime import datetime


hello = "Hola amigo"
for char in hello:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

subprocess.call('clear', shell=True)


parser = argparse.ArgumentParser(description="Simple escaner de puertos, usa el parámetro -t y una ip a continuación")
parser.add_argument('-t','--target',help="Objetivo")
parser = parser.parse_args()



def main():
	if parser.target:
		try:
			for port in range(1,100):
				ip = parser.target
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				conexion = sock.connect_ex((ip, port))
				if conexion==0:
					print ("Puerto {}: abierto".format(port))
				sock.close()
		except :
			print("No me pude conectar")
			sys.exit()
	else:
		print("No hay objetivo")

if __name__ == '__main__':
	main()

