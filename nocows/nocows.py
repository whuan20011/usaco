"""
ID: whuan2001
LANG: PYTHON2
TASK: nocows
"""
import math
def solution():
    fin = open("nocows.in", "r")
    fout = open("nocows.out", "w")
    N, K = map(int, fin.readline().strip().split())
    dic = {}
    print >>fout, (dfs(N, K, N, K, dic) - dfs(N, K, N, K - 1, dic) + 9901) % 9901
def dfs(N, K, nodes, height, dic):
    if (nodes, height) in dic:
        return dic[(nodes, height)]
    if height == 1 and nodes != 1:
        return 0
    if nodes == 1:
        return 1
    if nodes == 3 and height > 1:
        return 1
    pedigrees = []
    for nodes_left in range(1, nodes - 1):
        nodes_right = nodes - 1 - nodes_left
        cur_pedigrees = dfs(N, K, nodes_left, height - 1, dic)
        cur_pedigrees *= dfs(N, K, nodes_right, height - 1, dic)
        pedigrees.append(cur_pedigrees)
    dic[(nodes, height)] = sum(pedigrees) % 9901
    return dic[(nodes, height)]
if __name__ == "__main__":
    solution()
