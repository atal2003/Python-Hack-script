#! /local/bin/env python    


test_dict = {}
a = input("pleas enter a file >  ")
with open(a, "r") as file_test:
    b = file_test.read()
    for line in b:
        line1 = line.split()
        print(line1)

       # test_dict[line1] = test_dict.get(line1, 0) + 1

#print(test_dict)

