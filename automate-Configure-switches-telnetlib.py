#!/usr/bin/env python

import getpass
import sys
import telnetlib

user = raw_input("Enter your telnet username: ")
password = getpass.getpass()


for n in range (4,200):
    print "Telnet to host" + str(n)
    HOST = "192.168.1." + str(n)
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("enable \n")
    tn.write("mmm \n")
    tn.write("conf t\n")

    
    tn.write("ntp server 172.20.25.4 p " + "\n")
    tn.write("ntp server 172.20.25.5" + "\n")

    tn.write("end\n")
    tn.write("exit\n")

    print tn.read_all()
