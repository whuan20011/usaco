"""
ID: whuan2001
LANG: PYTHON2
TASK: holstein
"""
import copy
min_scoop = 15
def solution():
    fin = open("holstein.in", "r")
    fout = open("holstein.out", "w")
    V = int(fin.readline().strip())
    requirements = map(int, fin.readline().strip().split())
    G = int(fin.readline().strip())
    scoops = []
    for line in fin.readlines():
        scoops.append(map(int, line.strip().split()))
    arr = [0] * V
    temp = []
    res = []
    gen_scoops(V, requirements, G, scoops, temp, arr, res)
    res = sorted(res)
    idx = [str(min_scoop)]
    for p, q in enumerate(res[-1]):
        if q == 1:
            idx.append(str(p + 1))
    print>> fout, " ".join(idx)           
def gen_scoops(V, requirements, G, scoops, temp, arr, res):
    global min_scoop
    if is_satisfy(requirements, arr):
        if sum(temp) < min_scoop:
            res[:] = []
            min_scoop = sum(temp)
        if sum(temp) == min_scoop:
            res.append(copy.deepcopy(temp))
            return
    else:
        if len(temp) == G:
            return
        for j in range(2):
            if j == 1:
                for k in range(V):
                    arr[k] += scoops[len(temp)][k]
            temp.append(j)
            gen_scoops(V, requirements, G, scoops, temp, arr, res)
            temp.pop()
            if j == 1:
                for k in range(V):
                    arr[k] -= scoops[len(temp)][k]
def is_satisfy(requirements, arr):
    for i in range(len(arr)):
        if arr[i] < requirements[i]:
            return False
    return True
if __name__ == "__main__":
    solution()
