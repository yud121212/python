#!/usr/bin/python
import os
from socket import *
import optparse
from threading import *
os.system("figlet -f slant  SCAN PORT | toilet -f term  --gay")
def retBanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s= socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
		return banner
	except:
		return 
def main():
	port = 22
	ip = raw_input("[*] Enter the ip to scan: ")
	#s = raw_input("[*] Enter the ip to scan: ")
	#ip= gethostbyname(s)
	banner = retBanner(ip,port)
	if banner:
		print "[+]" + ip + ":" + banner
main()