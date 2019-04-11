"""
ID: whuan2001
LANG: PYTHON2
TASK: barn1
"""
def solution():
    fin = open("barn1.in", "r")
    fout = open("barn1.out", "w")
    max_purchase, total_barns, occupied = map(int, fin.readline().strip().split())
    if max_purchase >= occupied:
        print >> fout, occupied
        return
    arr = []
    for gate in fin.readlines():
        arr.append(int(gate.strip()))
    arr = sorted(arr)
    brr = []
    for i in range(1, len(arr)):
        brr.append(arr[i] - arr[i - 1])
    brr = sorted(brr)
    brr = brr[:: -1]
    count = 0
    for j in range(max_purchase - 1):
        count += brr[j]
    print >> fout, arr[-1] - arr[0] + 1 - count + max_purchase - 1
if __name__ == "__main__":
    solution()
    