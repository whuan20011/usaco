"""
ID: whuan2001
LANG: PYTHON2
TASK: money
"""
import sys
sys.setrecursionlimit(1000000)
def solution():
    fin = open("money.in", "r")
    fout = open("money.out", "w")
    V, N = map(int, fin.readline().strip().split())
    coinage = []
    for line in fin.readlines():
        coinage += map(int, line.strip().split())
    coinage = sorted(coinage)
    dic = {}
    print >>fout, ways_to_construct(V, N, coinage, dic)
def ways_to_construct(V, N, coinage, dic):
    if (N, tuple(coinage)) in dic:
        return dic[(N, tuple(coinage))]
    if not coinage:
        return 0
    else:
        if N == coinage[0]:
            return 1
        if N < coinage[0]:
            return 0
        ways = 0
        ways = ways_to_construct(V, N - coinage[0], coinage, dic)
        if coinage:
            first = coinage.pop(0)
            ways += ways_to_construct(V, N, coinage, dic)
            coinage.append(first)
            coinage.sort()
        dic[(N, tuple(coinage))] = ways
        return ways
if __name__ == "__main__":
    solution()
