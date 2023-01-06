#!/usr/bin/python3
def add_arg(argv):
    args_len = len(argv) - 1
    if args_len == 0:
        print("{:d}".format(args_len))
        return
    else:
        i = 1
        add = 0
        while i <= args_len:
            add += int(argv[i])
            i += 1
        print("{:d}".format(add))

if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
