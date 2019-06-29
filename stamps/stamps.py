"""
ID: whuan2001
LANG: PYTHON2
TASK: stamps
"""
def solution():
    fin = open("stamps.in", "r")
    fout = open("stamps.out", "w")
    K, N = map(int, fin.readline().strip().split())
    prices = []
    for line in fin.readlines():
        prices += map(int, line.strip().split())
    money = 0
    arr = [0] * 2000000
    while arr[money] <= K:
        money += 1
        min_count = 1<<32 - 1
        for p in prices:
            if money - p >= 0 and arr[money-p] < min_count:
                min_count = arr[money-p]
        arr[money] = min_count + 1
    print >>fout, money - 1
if __name__ == "__main__":
    solution()
    