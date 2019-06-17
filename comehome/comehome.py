"""
ID: whuan2001
LANG: PYTHON2
TASK: comehome
"""
def solution():
    fin = open("comehome.in", "r")
    fout = open("comehome.out", "w")
    P = int(fin.readline().strip())
    graph = {}
    for _ in range(P):
        src, dst, length = fin.readline().strip().split()
        if src not in graph:
            graph[src] = {}
        if dst not in graph:
            graph[dst] = {}
        length = min(int(length), graph[src].get(dst, float('inf')))
        graph[src][dst] = length
        graph[dst][src] = length
    dic = dijkstra(graph, "Z")
    print dic
    shortest_path = float('inf')
    for dst in dic:
        if dst.isupper() and dic[dst] < shortest_path and dst != "Z":
            shortest_path = dic[dst]
            fastest_cow = dst
    print >>fout, fastest_cow, shortest_path
def dijkstra(graph, src):
    nodes = [node for node in graph]
    distance = {}
    for n in nodes:
        distance[n] = float('inf')
    distance[src] = 0
    while nodes:
        mid_distance = float('inf')
        mid_node = src
        for d in nodes:
            if distance[d] < mid_distance:
                mid_distance = distance[d]
                mid_node = d
        for v in graph[mid_node]:
            distance[v] = min(distance[v], distance[mid_node] + graph[mid_node][v])
        if mid_node not in nodes:
            break
        nodes.remove(mid_node)
    return distance
if __name__ == "__main__":
    solution()
            