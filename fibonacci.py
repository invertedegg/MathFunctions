from sys import argv
from math import sqrt

# Usage statement for file
def usage():
    print("python3 fibonacci.py [-i || -s] [index]")

# Function to find the Fibonacci number at index n
def fiboIndv(nth):
    numer = pow((1 + sqrt(5)), nth)
    denom = (pow(2, nth)) * sqrt(5)
    return round(numer / denom)

# Function to find the Fibonacci sequence of numbers from n to 0
def fiboSeq(nth):
    seq = []

    if nth == 0:
        return [fiboIndv(nth)]
    else:
        seq.append(fiboIndv(nth))
        for n in fiboSeq(nth - 1):
            seq.append(n)
        return seq

# Main function
def main():
    if len(argv) < 3:
        usage()
    else:
        if argv[1] == "-i":
            print("Fibonacci number at index " + argv[2] + ": ", fiboIndv(float(argv[2])))
        elif argv[1] == "-s":
            seq = fiboSeq(float(argv[2]))
            seq.reverse()
            print("Fibonacci sequence from 0 to " + argv[2] + ": ", seq)
        else:
            usage()

if __name__ == "__main__":
    main()
