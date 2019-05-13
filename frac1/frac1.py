"""
ID: whuan2001
LANG: PYTHON2
TASK: frac1
"""
from fractions import Fraction
from fractions import gcd
def solution():
    fin = open("frac1.in", "r")
    fout = open("frac1.out", "w")
    num = int(fin.readline().strip())
    frac = []
    for i in range(1, num):
        for j in range(num, i, -1):
            if gcd(i, j) == 1:
                frac.append(Fraction(i, j))
    frac = sorted(frac)
    print>> fout, "0/1"
    for k in frac:
        print>> fout, Fraction(k)
    print>> fout, "1/1"
if __name__ == "__main__":
    solution()    
