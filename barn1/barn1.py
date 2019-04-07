"""
ID: whuan2001
LANG: PYTHON2
TASK: barn1
"""
def solution():
    fin = open("barn1.in", "r")
    fout = open("barn1.out", "w")
    max_purchase, num_stalls, num_occupied = map(int, fin.readline().strip().split())
    arr = []
    for line in fin.readlines():
        arr.append([int(line.strip())])
    arr = sorted(arr)
    if num_occupied <= max_purchase:
        print >> fout, num_occupied
    else:
        gap = 1
        while len(arr) > max_purchase:
            arr = seprate(arr, gap, max_purchase)
            gap += 1
        res = 0
        for s in arr:
            res = res + s[-1] - s[0] + 1
        print >> fout, res

def seprate(arr, gap, max_purchase):
    new = []
    new.append(arr[0])
    count = 0
    for i in range(1, len(arr)):
        if int(arr[i][0]) - int(new[-1][-1]) == gap and count != len(arr) - max_purchase:
            new[-1].extend(arr[i])
            count += 1
        else:
            new.append(arr[i])
    return new
if __name__ == "__main__":
    solution()
               