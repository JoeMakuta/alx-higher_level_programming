#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    myNames = dir(hidden_4)
    print(myNames)
    for myName in myNames:
        if myName[-2:] != "__" :
            print(myName)