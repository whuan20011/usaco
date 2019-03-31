"""
ID: whuan2001
LANG: PYTHON2
TASK: dualpal
"""
def solution():
    fin = open("dualpal.in", "r")
    fout = open("dualpal.out", "w")
    n, s = map(int, fin.readline().strip().split())
    res = []
    for num in range(s + 1, s + 20000):
        if transfer(num) == 1:
            res.append(num)
            if len(res) == n:
                break
    for r in res:
        print >> fout, r
def transfer(num):
    count = 0
    for b in range(2, 11):
        temp = num
        arr = []
        while temp != 0:
            arr.append(temp % b)
            temp = temp / b
        if palindrome(arr):
            count += 1
        if count >= 2:
            return 1
    if count < 2:
        return 0

def palindrome(arr):
    if arr[0] == 0 or arr[-1] == 0:
        return False
    if len(arr) == 1:
        return True
    for i in range(len(arr) / 2):
        if arr[i] == arr[len(arr) - i - 1]:
            continue
        else:
            return False
    return True
if __name__ == "__main__":
    solution()
