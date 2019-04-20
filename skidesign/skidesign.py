"""
ID: whuan2001
LANG: PYTHON2
TASK: skidesign
"""
fin = open("skidesign.in", "r")
fout = open("skidesign.out", "w")
N = int(fin.readline().strip())
hills = []
for elevation in fin.readlines():
    hills.append(int(elevation.strip()))
hills = sorted(hills)
res = 100000000
for left in range(84):
    right = left + 17
    cost = 0
    for i in range(len(hills)):
        if hills[i] < left:
            cost += (left - hills[i]) * (left - hills[i])
        if hills[i] > right:
            cost += (hills[i] - right) * (hills[i] - right)
    res = min(res, cost)
print >>fout, res
