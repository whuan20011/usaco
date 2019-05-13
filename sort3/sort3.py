"""
ID: whuan2001
LANG: PYTHON2
TASK: sort3
"""
def solution():
    fin = open("sort3.in", "r")
    fout = open("sort3.out", "w")
    num = int(fin.readline().strip())
    arr = []
    for line in fin.readlines():
        arr.append(int(line.strip()))
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(num):
        if arr[i] == 1:
            count1 += 1
        elif arr[i] == 2:
            count2 += 1
        elif arr[i] == 3:
            count3 += 1
    temp = []
    tag = 0
    for j in range(num - 1, num - 1 - count3, -1):
        if arr[j] != 3:
            tag += 1
            temp.append(arr[j])
    temp = sorted(temp)
    h = 0
    for k in range(count1 + count2):
        if arr[k] == 3:
            arr[k] = temp[h]
            h += 1
    for p in range(count1):
        if arr[p] != 1:
            tag += 1
    print >>fout, tag
if __name__ == "__main__":
    solution()
