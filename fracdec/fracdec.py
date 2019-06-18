"""
ID: whuan2001
LANG: PYTHON2
TASK: fracdec
"""
def solution():
    fin = open("fracdec.in", "r")
    fout = open("fracdec.out", "w")
    N, D = map(int, fin.readline().strip().split())
    integer = N / D
    remainder = N % D
    res = str(integer) + "."
    if remainder == 0:
        print >>fout, res + "0"
    else:
        remainders = {}
        after_decimal_point = []
        tag = -1
        idx = 0
        while remainder != 0:
            if remainder in remainders:
                tag = remainders[remainder]
                break
            remainders[remainder] = idx
            idx += 1
            remainder *= 10
            after_decimal_point.append(remainder / D)
            remainder %= D
        if tag == -1:
            for num in after_decimal_point:
                res += str(num)
            for i in range(0, len(res), 76):
                print >>fout, res[i: i + 76]
        else:
            for j in range(len(after_decimal_point)):
                if j == tag:
                    res += "("
                res += str(after_decimal_point[j])
                if j == len(after_decimal_point) - 1:
                    res += ")"
            for i in range(0, len(res), 76):
                print >>fout, res[i: i + 76]
if __name__ == "__main__":
    solution()
    