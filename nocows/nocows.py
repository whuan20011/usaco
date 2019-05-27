"""
ID: whuan2001
LANG: PYTHON2
TASK: nocows
"""
def solution():
    fin = open("nocows.in", "r")
    N, K = map(int, fin.readline().strip().split())
    nodes = []
    height = 2
    pedigrees = 1
    res = []
    dfs(N, K, height, nodes, pedigrees, res)
    print sum(res)
def dfs(N, K, height, nodes, pedigrees, res):
    if height == 2:
        nodes.append(1)
        nodes.append(2)
        dfs(N, K, height + 1, nodes, pedigrees, res)
    if height > 2 and height < K:
        for i in range(1, nodes[-1]):
            nodes.append(2 * i)
            pedigrees *= combination(nodes[-1], i)
            dfs(N, K, height + 1, nodes, pedigrees, res)
            nodes.pop()
            pedigrees /= combination(nodes[-1], i)
    if height == K:
        if (N - sum(nodes)) >= 2 and (N - sum(nodes)) <= nodes[-1] * 2:
            nodes.append(N - sum(nodes))
            pedigrees *= combination(nodes[-1], (N - sum(nodes) / 2)
            res.append(pedigrees)
            return
        else:
            return
def combination(x, y):
    

            
            
            
        
