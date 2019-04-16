"""
ID: whuan2001
LANG: PYTHON2
TASK: wormhole
"""
def solution():
    fin = open("wormhole.in", "r")
    fout = open("wormhole.out", "w")
    N = int(fin.readline().strip())
    ori = []
    i = 0
    for l in fin.readlines():
        x, y = map(int, l.strip().split())
        i += 1
        ori.append((x, y))
    ori = sorted(ori, key = lambda x: (x[1], x[0]))
    right = {}
    for h in range(len(ori) - 1):
        if ori[h][1] == ori[h + 1][1]:
            right[ori[h]] = ori[h + 1]
    pairs = []
    permutation(ori, {}, pairs)
    res = 0
    for pair in pairs:
        if circle(pair, right):
            res += 1
    print >>fout, res 
def permutation(ori, prefix, pairs):
    if len(prefix) == len(ori):
        pairs.append(prefix)
        return
    for j in range(len(ori)):
        if ori[j] not in prefix:
            break
    for k in range(j + 1, len(ori)):
        if ori[k] not in prefix:
            new_prefix = prefix.copy()        
            new_prefix[ori[j]] = ori[k]
            new_prefix[ori[k]] = ori[j]
            permutation(ori, new_prefix, pairs)        
def circle(pair, right):
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
    