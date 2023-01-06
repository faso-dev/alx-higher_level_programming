#!/usr/bin/python3
def print_arg(argv):
    args_len = len(argv) - 1
    if args_len == 0:
        print("{:d} argument.".format(args_len))
        return
    else:
        if args_len == 1:
            print("{:d} argument:".format(args_len))
        else:
            print("{:d} arguments:".format(args_len))
        i = 1
        while i <= args_len:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1

if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
