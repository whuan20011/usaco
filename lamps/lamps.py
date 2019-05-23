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
                if i == 0:
                    button1(N, lamps_state)
                if i == 1:
                    button2(N, lamps_state)
                if i == 2:
                    button3(N, lamps_state)
                if i == 3:
                    button4(N, lamps_state)
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
def button1(N, lamps_state):
    for j in range(N):
        if lamps_state[j] == 0:
            lamps_state[j] = 1
        else:
            lamps_state[j] = 0
    return lamps_state
def button2(N, lamps_state):
    for j in range(N):
        if j % 2 == 0:
            if lamps_state[j] == 0:
                lamps_state[j] = 1
            else:
                lamps_state[j] = 0
    return lamps_state
def button3(N, lamps_state):
    for j in range(N):
        if j % 2 == 1:
            if lamps_state[j] == 0:
                lamps_state[j] = 1
            else:
                lamps_state[j] = 0
    return lamps_state
def button4(N, lamps_state):
    for j in range(N):
        if j % 3 == 0:
            if lamps_state[j] == 0:
                lamps_state[j] = 1
            else:
                lamps_state[j] = 0
    return lamps_state
def is_satisfy(on_lamps, off_lamps, lamps_state):
    tag = 0
    for p in on_lamps:
        if lamps_state[p - 1] == 0:
            tag = 1
            return False
    if tag == 0:
        for q in off_lamps:
            if lamps_state[q - 1] == 1:
                tag = 1
                return False
        if tag == 0:
            return True
if __name__ == "__main__":
    solution()
                