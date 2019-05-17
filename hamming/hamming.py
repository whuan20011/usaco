"""
ID: whuan2001
LANG: PYTHON2
TASK: hamming
"""
import sys   
sys.setrecursionlimit(1000000)
def solution():
    fin = open("hamming.in", "r")
    fout = open("hamming.out", "w")
    N, B, D = map(int, fin.readline().strip().split())
    res = []
    resres = []
    recursive(N, B, D, 0, res, resres)
    p = N / 10
    q = N % 10
    a = 0
    b = 10
    if N <= 10:
        print >>fout, " ".join(resres[:])
    else:
        for _ in range(p):
            print >>fout, " ".join(resres[a:b])
            a += 10
            b += 10
        if q != 0:
            print >>fout, " ".join(resres[(p * 10):])       
def recursive(N, B, D, num, res, resres):
    if len(resres) == N:
        return
    temp = []
    a = num + 1
    if num == 0:
        for _ in range(B):
            temp.append(0)
        res.append(temp)
        resres.append(str(num))
    else:
        bin = []
        b = num
        while num != 0:
            m = num % 2
            num /= 2
            bin.append(m)
        if len(bin) > B:
            return
        else:
            for _ in range(B - len(bin)):
                temp.append(0)
        temp.extend(list(reversed(bin)))
        tag = 0
        for r in res:
            if not hamming(D, temp, r):
                tag = 1
                break
        if tag == 0:
            res.append(temp)
            resres.append(str(a - 1))
    recursive(N, B, D, a, res, resres)
def hamming(D, temp, r):
    diff = 0
    for i in range(len(r)):
        if temp[i] != r[i]:
            diff += 1
    if diff >= D:
        return True
    else:
        return False
if __name__ == "__main__":
    solution()
