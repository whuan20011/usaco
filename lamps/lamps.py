"""
ID: whuan2001
LANG: PYTHON2
TASK: lamps
"""
import copy
def solution():
    fin = open("lamps.in", "r")
    fout = open("lamps.out", "w")
    N = int(fin.readline().strip())
    C = int(fin.readline().strip())
    on_lamps = map(int, fin.readline().strip().split())
    on_lamps.pop()
    off_lamps = map(int, fin.readline().strip().split())
    off_lamps.pop()
    temp = []
    button_counts = []
    dfs(C, temp, button_counts)
    res = []
    for button in button_counts:
        lamps_state = [1] * N
        for i in range(4):
            if button[i] == 1:
                button_to_change(N, lamps_state, i)
        if is_satisfy(on_lamps, off_lamps, lamps_state):
            res.append(lamps_state)
    if not res:
        print >>fout, "IMPOSSIBLE"
    res = list(set([tuple(t) for t in res]))
    res = [list(v) for v in res]
    res = sorted(res)
    for r in res:
        for p, num in enumerate(r):
            r[p] = str(num)
    for q in res:
        print >>fout, "".join(q)
def dfs(C, temp, button_counts):
    if C < 0:
        return
    if len(temp) == 3:
        temp.append(C % 2)
        button_counts.append(copy.deepcopy(temp))
        temp.pop()
        return
    for i in range(2):
        temp.append(i)
        dfs(C - i, temp, button_counts)
        temp.pop()
def button_to_change(N, lamps_state, i):
    button_start_tolerance = [(0, 1), (0, 2), (1, 2), (0, 3)]
    start = button_start_tolerance[i][0]
    tolerance = button_start_tolerance[i][1]
    while start < N:
        if lamps_state[start] == 0:
            lamps_state[start] = 1
        else:
            lamps_state[start] = 0
        start += tolerance
    return lamps_state
def is_satisfy(on_lamps, off_lamps, lamps_state):
    for p in on_lamps:
        if lamps_state[p - 1] == 0:
            return False
    for q in off_lamps:
        if lamps_state[q - 1] == 1:
            return False
    return True
if __name__ == "__main__":
    solution()
                