"""
ID: whuan2001
LANG: PYTHON2
TASK: sort3
"""
def solution():
    fin = open("sort3.in", "r")
    fout = open("sort3.out", "w")
    num = int(fin.readline().strip())
    numbers = []
    for line in fin.readlines():
        numbers.append(int(line.strip()))
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(num):
        if numbers[i] == 1:
            count1 += 1
        elif numbers[i] == 2:
            count2 += 1
        elif numbers[i] == 3:
            count3 += 1
    temp = []
    exchange_times = 0
    for j in range(num - 1, num - 1 - count3, -1):
        if numbers[j] != 3:
            exchange_times += 1
            temp.append(numbers[j])
    temp = sorted(temp)
    h = 0
    for k in range(count1 + count2):
        if numbers[k] == 3:
            numbers[k] = temp[h]
            h += 1
    for p in range(count1):
        if numbers[p] != 1:
            exchange_times += 1
    print >>fout, exchange_times
if __name__ == "__main__":
    solution()
