"""
ID: whuan2001
LANG: PYTHON2
TASK: prefix
"""
def solution():
    fin = open("prefix.in", "r")
    fout = open("prefix.out", "w")
    primitives = set()
    all_input = fin.readlines()
    longest_pri = 0
    for i, line in enumerate(all_input):
        if line.strip() == ".":
            break
        for primitive in line.strip().split():
            primitives.add(primitive)
            longest_pri = max(longest_pri, len(primitive))
    S = ""
    for j in range(i + 1, len(all_input)):
        S += all_input[j].strip()
    dic = {}
    for idx in range(len(S), -1, -1):
        dfs(S, primitives, longest_pri, idx, dic)
    print >>fout, dic[0]
def dfs(S, primitives, longest_pri, idx, dic):
    if idx in dic:
        return dic[idx]
    if idx == len(S):
        return 0
    temp = []
    for point in range(idx + 1, idx + longest_pri + 1):
        if point > len(S):
            break
        if S[idx:point] in primitives:
            tag = 1
            temp.append(point - idx + dfs(S, primitives, longest_pri, idx + point - idx, dic))
    rest_longest = 0
    for t in temp:
        rest_longest = max(rest_longest, t)
    dic[idx] = rest_longest
    return rest_longest
if __name__ == "__main__":
    solution()
