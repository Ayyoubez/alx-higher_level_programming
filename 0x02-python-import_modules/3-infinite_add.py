#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    res = 0
    for arg in argv:
       res += int(arg)
    print(res)
