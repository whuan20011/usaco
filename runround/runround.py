"""
ID: whuan2001
LANG: PYTHON2
TASK: runround
"""
def solution():
    global point
    fin = open("runround.in", "r")
    fout = open("runround.out", "w")
    M = int(fin.readline().strip())
    for num in range(M + 1, M + 999999):
        point = 0
        digits = []
        dic_digits = {}
        dic = {}
        tag = 0
        res = num
        while num != 0:
            m = num % 10
            num /= 10
            if m == 0:
                tag = 1
                break
            if m not in dic_digits:
                dic_digits[m] = True
            else:
                tag = 1
                break
            digits.append(m)
        if tag == 1:
            continue
        digits = list(reversed(digits))
        if is_runround(digits, dic, 0):
            print >>fout, res
            break
def is_runround(arr, dic, point):
    if point not in dic:
        dic[point] = True
    else:
        if point == 0 and len(dic) == len(arr):
            return True
        else:
            return False
    return is_runround(arr, dic, (point + arr[point] % len(arr)) % len(arr))
if __name__ == "__main__":
    solution()
