"""
ID: whuan2001
LANG: PYTHON2
TASK: crypt1
"""
def solution():
    fin = open("crypt1.in", "r")
    fout = open("crypt1.out", "w")
    n = int(fin.readline().strip())
    arr = ""
    for s in fin.readline().strip().split():
        arr += s
    brr = arr
    digits = []
    prefix = ""
    recursive(arr, prefix, digits)
    res = 0
    for d in digits:
        digits_3 = d[0: 3]
        digits_2 = d[3: ]
        first = str_num(digits_3)
        second = str_num(digits_2)
        product1 = first * int(d[-1])
        product2 = first * int(d[3])
        product = first * second
        if product1 / 1000 == 0 and product2 / 1000 == 0:
            if judge(product1, brr) + judge(product2, brr) + judge(product, brr) == 3:
                res += 1
    print >> fout, res
def judge(product, brr):
    produce = ""
    while product != 0:
        produce += str(product % 10)
        product /= 10
    for pro in produce:
        if pro not in brr:
            return 0
    return 1
def recursive(arr, prefix, digits):
    if len(prefix) == 5:
        digits.append(prefix)
        return
    for p in arr:
        recursive(arr, prefix + p, digits)
def str_num(digits):
    num = 0
    for i in digits:
        num = num * 10 + int(i)
    return num
if __name__ == "__main__":
    solution()