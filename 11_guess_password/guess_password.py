#! /usr/bin/evn python


user_choice = raw_input("enter a word  :")


with open ("/usr/share/wordlists/fern-wifi/common.txt", "r") as check_file:
        for line in check_file:
            b = line.strip()
            if b == user_choice:
                print("password found" + "-----"  + user_choice)
                exit()


print("end of the line")
