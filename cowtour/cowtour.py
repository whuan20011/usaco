"""
ID: whuan2001
LANG: PYTHON2
TASK: cowtour
"""
import math
def solution():
    fin = open("cowtour.in", "r")
    fout = open("cowtour.out", "w")
    #input all datas
    N = int(fin.readline().strip())
    coordinates = []
    for _ in range(N):
        coordinates.append(map(int, fin.readline().strip().split()))
    graph = []
    for _ in range(N):
        graph.append(map(int, list(fin.readline().strip())))
    #change the graph with adjacent distance
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                a = coordinates[i][0] - coordinates[j][0]
                b = coordinates[i][1] - coordinates[j][1]
                graph[i][j] = math.sqrt(a * a + b * b)
            elif i != j and graph[i][j] == 0:
                graph[i][j] = float('inf')
            elif i == j:
                graph[i][j] = 0
    nodes = [i for i in range(len(graph))]
    dic = {}
    ori_longest = 0
    for r in nodes:
        dic[r] = dijkstra(graph, r)
        ori_longest = max(ori_longest, dic[r])
    shortest_diameter = float('inf')
    for p in nodes:
        for q in nodes:
            if graph[p][q] == float('inf'):
                m = coordinates[p][0] - coordinates[q][0]
                n = coordinates[p][1] - coordinates[q][1]
                new_diameter = math.sqrt(m * m + n * n)
                new_diameter += dic[p] + dic[q]
                shortest_diameter = min(shortest_diameter, new_diameter)
    shortest_diameter = max(shortest_diameter, ori_longest)
    print >>fout, "{0:.6f}".format(shortest_diameter)
def dijkstra(graph, src):
    if not graph:
        return 0
    nodes = [i for i in range(len(graph))]
    # using distance to track the distance from src to a note
    distance = {}
    # initiate distance
    for node in nodes:
        distance[node] = float('inf')
    distance[src] = 0
    #keep track of the path from src to a note
    while nodes:
        mid_distance = float('inf')
        mid_idx = 0
        for d in nodes:
            if distance[d] < mid_distance:
                mid_distance = distance[d]
                mid_idx = d
        for v in nodes:
            distance[v] = min(distance[v], distance[mid_idx] + graph[mid_idx][v])
        if mid_idx not in nodes:
            break
        nodes.remove(mid_idx)
    graph[src] = distance
    longest = 0
    for dis in distance:
        if distance[dis] != float('inf'):
            longest = max(longest, distance[dis])
    return longest
if __name__ == "__main__":
    solution()
    
