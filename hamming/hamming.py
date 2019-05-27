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
    binary_num = []
    str_num = []
    recursive(N, B, D, 0, binary_num, str_num)
    p = N / 10
    q = N % 10
    a = 0
    b = 10
    if N <= 10:
        print >>fout, " ".join(str_num[:])
    else:
        for _ in range(p):
            print >>fout, " ".join(str_num[a:b])
            a += 10
            b += 10
        if q != 0:
            print >>fout, " ".join(str_num[(p * 10):])       
def recursive(N, B, D, num, binary_num, str_num):
    if len(str_num) == N:
        return
    temp = []
    a = num + 1
    if num == 0:
        for _ in range(B):
            temp.append(0)
        binary_num.append(temp)
        str_num.append(str(num))
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
        for r in binary_num:
            if hamming(D, temp, r) < D:
                tag = 1
                break
        if tag == 0:
            binary_num.append(temp)
            str_num.append(str(a - 1))
    recursive(N, B, D, a, binary_num, str_num)
def hamming(D, temp, r):
    diff = 0
    for i in range(len(r)):
        if temp[i] != r[i]:
            diff += 1
    return diff
if __name__ == "__main__":
    solution()
