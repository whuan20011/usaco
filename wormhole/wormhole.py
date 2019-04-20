"""
ID: whuan2001
LANG: PYTHON2
TASK: wormhole
"""
def solution():
    fin = open("wormhole.in", "r")
    fout = open("wormhole.out", "w")
    N = int(fin.readline().strip())
    points = []
    for l in fin.readlines():
        x, y = map(int, l.strip().split())
        points.append((x, y))
    points = sorted(points, key = lambda x: (x[1], x[0]))
    right = {}
    for h in range(len(points) - 1):
        if points[h][1] == points[h + 1][1]:
            right[points[h]] = points[h + 1]
    pairs = []
    pair_wormholes(points, {}, pairs)
    res = 0
    for pair in pairs:
        if has_circle(pair, right):
            res += 1
    print >>fout, res 
def pair_wormholes(points, prefix, pairs):
    if len(prefix) == len(points):
        pairs.append(prefix)
        return
    for first in range(len(points)):
        if points[first] not in prefix:
            break
    for second in range(first + 1, len(points)):
        if points[second] not in prefix:
            new_prefix = prefix.copy()        
            new_prefix[points[first]] = points[second]
            new_prefix[points[second]] = points[first]
            pair_wormholes(points, new_prefix, pairs)        
def has_circle(pair, right):
    for p in pair:
        path = {}
        tag = 0
        while p in right:
            if p not in path:
                path[p] = True
            else:
                tag = 1
                break
            p = pair[right[p]]
        if tag == 1:
            return True
    return False    
if __name__ == "__main__":
    solution()
    