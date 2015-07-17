import sys


def colorlist(filename):
    text_file = open(filename)
    text_file = text_file.read().split("\n")
    return text_file

print colorlist('colorlist.txt')