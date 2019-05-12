"""
ID: whuan2001
LANG: PYTHON2
TASK: numtri
"""
import sys
sys.setrecursionlimit(1005)
def solution():
    fin = open("numtri.in", "r")
    fout = open("numtri.out", "w")
    row = int(fin.readline().strip())
    numtri = []
    for line in fin.readlines():
        arr = map(int, line.strip().split())
        numtri.append(arr)
    dic = {}
    res = max_sum(numtri, row, (0, 0), dic)
    print >>fout, res
def max_sum(numtri, row, cur_index, dic):
    cur_num = numtri[cur_index[0]][cur_index[1]]
    if cur_index in dic:
        return dic[cur_index]
    if cur_index[0] == row - 1:
        return cur_num
    left_index = (cur_index[0] + 1, cur_index[1])
    right_index = (cur_index[0] + 1, cur_index[1] + 1)
    res = max(cur_num + max_sum(numtri, row, left_index, dic),
              cur_num + max_sum(numtri, row, right_index, dic))
    dic[cur_index] = res
    return res
if __name__ == "__main__":
    solution()
    