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
    res = max_sum(numtri, row, numtri[0][0], (0, 0), dic)
    print >>fout, res
def max_sum(numtri, row, cur_num, cur_index, dic):
    if cur_index in dic:
        return dic[cur_index]
    if cur_index[0] == row - 1:
        return cur_num
    cur_num1 = numtri[cur_index[0] + 1][cur_index[1]]
    cur_index1 = (cur_index[0] + 1, cur_index[1])
    cur_num2 = numtri[cur_index[0] + 1][cur_index[1] + 1]
    cur_index2 = (cur_index[0] + 1, cur_index[1] + 1)
    res = max(cur_num + max_sum(numtri, row, cur_num1, cur_index1, dic),
              cur_num + max_sum(numtri, row, cur_num2, cur_index2, dic))
    dic[cur_index] = res
    return res
if __name__ == "__main__":
    solution()
    