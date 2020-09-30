import telnetlib
import getpass
import sys

for n in range (126,129,1):


   target = "172.30.241." + str(n)
   print(target)
   try:
       tn = telnetlib.Telnet(target)
   except:
       continue


  #target = "172.30.241." + str(n)
   user = "raafat"
   passwd = "123"
   telnet_port=23

   tn = telnetlib.Telnet(target, telnet_port, timeout=10)
   tn.expect(["Login: ", "login: ", "Username:"], 5)
   tn.write(user + "\r\n")
   tn.expect(["Password: ", "password"], 5)
   tn.write(passwd + "\r\n")

   tn.write("config t\n")

   tn.write("ntp server 172.20.25.4 p\n")
   tn.write("ntp server 172.20.25.5 \n")
   tn.write("end\n")
   tn.write("write\n")
   tn.write("exit\n")
   tn.interact()
