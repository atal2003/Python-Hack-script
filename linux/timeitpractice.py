#! /usr/bin/python3

from timeit import timeit

code1 = """
print("hello")

"""

print(timeit(code1, number=1000))

