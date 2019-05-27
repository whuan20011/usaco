"""
ID: whuan2001
LANG: PYTHON2
TASK: subset
"""
def solution():
    fin = open("subset.in", "r")
    fout = open("subset.out", "w")
    N = int(fin.readline().strip())
    arr = []
    for i in range(1, N + 1):
        arr.append(i)
    total = ((1 + N) * N) / 2
    if total % 2 != 0:
        print >>fout, 0
        return
    dic = {}
    res = partition(N, total, arr, 0, 0, dic)
    print >>fout, res
def partition(N, total, arr, idx, cur_sum, dic):
    if (idx, cur_sum) in dic:
        return dic[(idx, cur_sum)]
    if idx == N:
        return 0
    if cur_sum == total / 2:
        return 1
    if cur_sum > total / 2:
        return 0
    res = partition(N, total, arr, idx + 1, cur_sum + arr[idx], dic)
    res += partition(N, total, arr, idx + 1, cur_sum, dic)
    dic[(idx, cur_sum)] = res
    return res
if __name__ == "__main__":
    solution()
            