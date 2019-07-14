"""
ID: whuan2001
LANG: PYTHON2
TASK: butter
"""
from heapq import *
def solution():
    fin = open("butter.in", "r")
    fout = open("butter.out", "w")
    N, P, C = map(int, fin.readline().strip().split())
    cow_in_pasture = []
    for _ in range(N):
        cow_in_pasture.append(int(fin.readline().strip()))
    dic = {}
    for _ in range(C):
        a, b, dis = map(int, fin.readline().strip().split())
        if a not in dic:
            dic[a] = {}
        dic[a][b] = dis
        if b not in dic:
            dic[b] = {}
        dic[b][a] = dis
    minimum_dis = 10000000
    for pasture in range(1, P + 1):
        pasture_dis = dijkstra(P, dic, pasture)
        cur_dis = 0
        for cow_grazing in cow_in_pasture:
            cur_dis += pasture_dis[cow_grazing]
        minimum_dis = min(minimum_dis, cur_dis)
    print >>fout, minimum_dis
def dijkstra(P, dic, src):
    visited = set()
    src_dis = {src: 0}
    heap = []
    heappush(heap, (0, src))
    for _ in range(P):
        temp = heappop(heap)
        while temp[1] in visited:
            temp = heappop(heap)
        cur_mini_dis, next_p = temp
        for n, d in dic[next_p].items():
            if n not in src_dis:
                src_dis[n] = cur_mini_dis + d
                heappush(heap, (src_dis[n], n))
            else:
                if cur_mini_dis + d < src_dis[n]:
                    src_dis[n] = cur_mini_dis + d
                    heappush(heap, (src_dis[n], n))
        visited.add(next_p)
    return src_dis
if __name__ == "__main__":
    solution()             
             