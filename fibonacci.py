from sys import argv
from math import sqrt

def usage():
    print("python3 fibonacci.py [-i || -s] [index]")

def fiboIndv(nth):
    numer = pow((1 + sqrt(5)), nth)
    denom = (pow(2, nth)) * sqrt(5)
    return round(numer / denom)

def fiboSeq2(nth):
    tot = 0

    if nth == 1 or nth == 2:
        tot = 1
    elif nth == 25:
        tot = 75025
    elif nth > 2:
        tot = fiboSeq(nth - 2) + fiboSeq(nth - 1)
    return tot

def fiboSeq(nth):
    if nth == 0:
        return "0"
    else:
        return [fiboIndv(nth)].append(fiboSeq(nth -1))

def main():
    if len(argv) < 3:
        usage()
    else:
        if argv[1] == "-i":
            print("Fibonacci number at index " + argv[2] + ": ", fiboIndv(float(argv[2])))
        elif argv[1] == "-s":
            print("Fibonacci sequence from "  + argv[2] + " to 0: ", fiboSeq(float(argv[2])))
        else:
            usage()

if __name__ == "__main__":
    main()
