#!/usr/bin/python3
def print_arg(argv):
    argslen = len(argv) - 1
    if argslen == 0:
        print("{:d} argument.".format(argslen))
        return
    else:
        if argslen == 1:
            print("{:d} argument:".format(argslen))
        else:
            print("{:d} arguments:".format(argslen))
        i = 1
        while i <= argslen:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1

if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
