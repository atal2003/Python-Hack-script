#! /usr/bin/python3

try:
    file1 = open("test.log")
    age = int(input("age: "))
    test_fact = 10 / age
        
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age. ")
else: 
    print("good")
finally:
    file1.close() # this is becuase if the file closing goes under try effect. 

   #timeit is a class that can show the time of python code execution
   # rais exception example 
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("age cannot be 0 or less")
    return 10 / age
