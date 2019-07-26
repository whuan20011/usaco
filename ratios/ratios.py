"""
ID: whuan2001
LANG: PYTHON2
TASK: ratios
"""
def solution():
    fin = open("ratios.in", "r")
    fout = open("ratios.out", "w")
    goal_ratios = map(int, fin.readline().strip().split())
    three_mixtures = []
    for line in fin.readlines():
        three_mixtures.append(map(int, line.strip().split()))
    dic = {}
    arr = []
    for x in range(100):
        for y in range(100):
            for z in range(100):
                if x == 0 and y == 0 and z == 0:
                    continue
                a = x * three_mixtures[0][0] + y * three_mixtures[1][0] + z * three_mixtures[2][0]
                b = x * three_mixtures[0][1] + y * three_mixtures[1][1] + z * three_mixtures[2][1]
                c = x * three_mixtures[0][2] + y * three_mixtures[1][2] + z * three_mixtures[2][2]
                if (a * goal_ratios[1]) ==  (b * goal_ratios[0]) and (b * goal_ratios[2]) == (c * goal_ratios[1]):
                    if goal_ratios[0] != 0 and a / goal_ratios[0] != 0:
                        dic[(x, y, z)] = a / goal_ratios[0]
                    elif goal_ratios[1] != 0 and b / goal_ratios[1] != 0:
                        dic[(x, y, z)] = b / goal_ratios[1]
                    elif goal_ratios[2] != 0 and c / goal_ratios[2] != 0:
                        dic[(x, y, z)] = c / goal_ratios[2]
                    
    if not dic:
        print >>fout, "NONE"
        return
    smallest = 300
    for k in dic:
        if sum(k) < smallest:
            smallest = sum(k)
            tag = k
    print >>fout, tag[0], tag[1], tag[2], dic[tag]
if __name__ == "__main__":
    solution()
                    