#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    sum = 0
    myRange = len(sys.argv)
    for i in range(1, myRange):
        sum += int(sys.argv[i])
    print("{}".format(sum))
