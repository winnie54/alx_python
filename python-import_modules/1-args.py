#!/usr/bin/python3

import sys
num_args = len(sys.argv) - 1
arg_list = sys.argv[1:]
if num_args == 0:
    print("0 arguments.")
elif num_args == 1:
    print("1 argument:")
else:
    print("{}arguments:".format(num_args))
for i in range(num_args):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

"""if __name__ == "__main__":
    #prints the number of and the list of its arguments.
    import sys

    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{}arguments:".format(num_args./1-a   ))

    for i in range(num_args):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
 """