import ClearScreen
import paramiko
from paramiko import SSHClient, AutoAddPolicy
from sys import stderr, stdin, stdout

host = '192.168.0.100'
port = 22
username = 'admin'
password = 'wago'

while True:
  print("WAGO Linux Terminal on PFC200V3-4E4BD9.")  
  print ("root@PFC200V3-4E4BD9:~")  
  commando = input("Welk Commando wil je uitvoeren?: ")

  client = paramiko.client.SSHClient()
  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  client.connect(host, username=username, password=password)
  _stdin, _stdout, _stderr = client.exec_command(commando)
  print(_stdout.read().decode())
  client.close()
  input ("stoppen? j voor ja, enter om verder te gaan : ")
  if input == "j":
    break
