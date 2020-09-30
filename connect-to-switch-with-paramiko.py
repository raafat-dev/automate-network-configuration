import paramiko
import telnetlib
import time

ip_address = "172.30.241.89"
username = "raafat"
password = "123"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print "Successful connection", ip_address

remote_connection = ssh_client.invoke_shell()

remote_connection.send("configure terminal\n")
remote_connection.send("ntp server 172.20.25.4 p\n")
remote_connection.send("end\n")

time.sleep(1)
output = remote_connection.recv(65535)
print output
