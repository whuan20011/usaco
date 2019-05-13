"""
ID: whuan2001
LANG: PYTHON2
TASK: frac1
"""
def solution():
    fin = open("frac1.in", "r")
    fout = open("frac1.out", "w")
    num = int(fin.readline().strip())
    res = []
    find_frac(0, 1, 1, 1, num, res)
    print >>fout, "0/1"
    for r in res:
        print >>fout, r
    print >>fout, "1/1"
def find_frac(p1, q1, p2, q2, num, res):
    if q1 + q2 > num:
        return
    find_frac(p1, q1, p1 + p2, q1 + q2, num, res)
    res.append(str((p1 + p2)) + "/" + str((q1 + q2)))
    find_frac(p1 + p2, q1 + q2, p2, q2, num, res)
if __name__ == "__main__":
    solution()
    