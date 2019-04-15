"""
ID: whuan2001
LANG: PYTHON2
TASK: combo
"""
def solution():
    fin = open("combo.in", "r")
    fout = open("combo.out", "w")
    N = int(fin.readline().strip())
    a1, a2, a3 = map(int, fin.readline().strip().split())
    b1, b2, b3 = map(int, fin.readline().strip().split())
    if N >= 5:
        farmer_dail1 = dail(a1, N)
        farmer_dail2 = dail(a2, N)
        farmer_dail3 = dail(a3, N)
        master_dail1 = dail(b1, N)
        master_dail2 = dail(b2, N)
        master_dail3 = dail(b3, N)
        count1 = same_number(farmer_dail1, master_dail1)
        count2 = same_number(farmer_dail2, master_dail2)
        count3 = same_number(farmer_dail3, master_dail3)
        print >>fout, 250 - count1 * count2 * count3
    else:
        print >>fout, N * N * N
def dail(num, N):
    dic = {}
    dic[(num -1 - 1 + N) % N + 1] = True
    dic[(num - 1 - 2 + N) % N + 1] = True
    dic[num] = True
    dic[(num + 1 + 1) % N - 1] = True
    dic[(num + 1 + 2) % N - 1] = True
    return dic
def same_number(dic1, dic2):
    count = 0
    for i in dic1:
        if i in dic2:
            count += 1
    return count
if __name__ == "__main__":
    solution()
        