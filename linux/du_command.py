#! /usr/bin/python3

from subprocess import call, Popen, PIPE


def test(dir_name):
    size_file = call(["du", "-sk", dir_name])
    print(size_file)


test("/root/PycharmProjects")
