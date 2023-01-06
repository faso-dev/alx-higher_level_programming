#!/usr/bin/python3
import hidden_4


def find_hidden_names():
    names = dir(hidden_4)
    for name in names:
        if name[:2] != '__':
            print("{:s}".format(name))


if __name__ == "__main__":
    find_hidden_names()
