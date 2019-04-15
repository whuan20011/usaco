"""
ID: whuan2001
LANG: PYTHON2
TASK: combo
"""
def solution():
    fin = open("combo.in", "r")
    fout = open("combo.out", "w")
    N = int(fin.readline().strip())
    farmers = map(int, fin.readline().strip().split())
    masters = map(int, fin.readline().strip().split())
    if N >= 5:
        farmers_dail = map(lambda x: dail(x, N), farmers)
        masters_dail = map(lambda x: dail(x, N), masters)
        count = map(lambda dic1, dic2: same_number(dic1, dic2), farmers_dail, masters_dail)
        res = 1
        for i in count:
            res *= i
        print >>fout, 250 - res
    else:
        print >>fout, N * N * N
def dail(num, N):
    dic = {}
    dic[(num -1 - 1 + N) % N + 1] = True
    dic[(num - 1 - 2 + N) % N + 1] = True
    dic[num] = True
    dic[(num - 1 + 1) % N + 1] = True
    dic[(num - 1 + 2) % N + 1] = True
    return dic
def same_number(dic1, dic2):
    count = 0
    for i in dic1:
        if i in dic2:
            count += 1
    return count
if __name__ == "__main__":
    solution()
        