"""
ID: whuan2001
LANG: PYTHON2
TASK: concom
"""
def solution():
    fin = open("concom.in", "r")
    fout = open("concom.out", "w")
    n = int(fin.readline().strip())
    table = []
    for _ in range(101):
        table.append([0] * 101)
    dic = {}
    for line in fin.readlines():
        triple = map(int, line.strip().split())
        if triple[0] == triple[1]:
            continue
        if triple[2] > 50:
            if triple[0] in dic:
                dic[triple[0]].append(triple[1])
            else:
                dic[triple[0]] = [triple[1]]
        else:
            table[triple[0]][triple[1]] = triple[2]
    all_kids(dic)
    while combine_control(dic, table):
        all_kids(dic)
    for father in sorted(dic):
        for child in sorted(dic[father]):
            if father != child:
                print >>fout, father, child
def combine_control(dic, table):
    tag = False
    for k in dic:
        for z in range(1, 101):
            if z != k and z not in dic[k]:
                sum = table[k][z]
                for v in dic[k]:
                    sum += table[v][z]
                if sum > 50:
                    dic[k].append(z)
                    tag = True
    return tag
def all_kids(dic):
    tag = True
    while tag:
        tag = False
        for father in dic:
            for child in dic[father]:
                if child in dic:
                    for grand_child in dic[child]:
                        if grand_child not in dic[father]:
                            dic[father].append(grand_child)
                            tag = True
if __name__ == "__main__":
    solution()
