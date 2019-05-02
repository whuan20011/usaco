"""
ID: whuan2001
LANG: PYTHON2
TASK: milk3
"""
def solution():
    fin = open("milk3.in", "r")
    fout = open("milk3.out", "w")
    a, b, c = map(int, fin.readline().strip().split())
    capacity = [a, b, c]
    milk = (0, 0, c)
    visited = set()
    recursive(milk, capacity, visited)
    res = []
    for v in visited:
        if v[0] == 0:
            res.append(v[2])
    res = sorted(res)
    res = map(str, res)
    print >>fout, " ".join(res)

def recursive(milk, capacity, visited):
    if milk in visited:
        return
    else:
        visited.add(milk)
        for i in range(3):
            for j in range(3):
                new_milk = list(milk)
                if j != i:
                    pour = min(new_milk[i], capacity[j] - new_milk[j])
                    new_milk[i] -= pour
                    new_milk[j] += pour
                    recursive(tuple(new_milk), capacity, visited)
if __name__ == "__main__":
    solution()
