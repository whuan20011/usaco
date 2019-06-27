"""
ID: whuan2001
LANG: PYTHON2
TASK: contact
"""
def solution():
    fin = open("contact.in", "r")
    fout = open("contact.out", "w")
    A, B, N = map(int, fin.readline().strip().split())
    string = ""
    for line in fin.readlines():
        string += line.strip()
    dic = {}
    for lens in range(A, B + 1):
        if len(string) - lens >= 0:
            for i in range(len(string) - lens + 1):
                if string[i : i + lens] not in dic:
                    dic[string[i : i + lens]] = 0
                dic[string[i : i + lens]] += 1
    dic1 = {}
    for k, v in dic.items():
        if v not in dic1:
            dic1[v] = []
        dic1[v].append(k)
    arr = sorted(dic1.items(), reverse=True)
    rank = min(N, len(arr))
    for i in range(rank):
        arr[i] = list(arr[i])
        arr[i][1] = sorted(arr[i][1], cmp=compare)
    for i in range(rank):
        print >>fout, arr[i][0]
        if len(arr[i][1]) <= 6:
            print >>fout, " ".join(arr[i][1])
        else:
            for j in range(0, len(arr[i][1]), 6):
                print >>fout, " ".join(arr[i][1][j:j + 6])
def compare(x, y):
    if len(x) < len(y):
        return -1
    elif len(x) > len(y):
        return 1
    else:
        if x < y:
            return -1
        if x > y:
            return 1
if __name__ == "__main__":
    solution()
