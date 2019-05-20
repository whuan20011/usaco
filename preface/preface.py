"""
ID: whuan2001
LANG: PYTHON2
TASK: preface
"""
import sys   
sys.setrecursionlimit(4000)
def solution():
    fin = open("preface.in", "r")
    fout = open("preface.out", "w")
    N = int(fin.readline().strip())
    res = {}
    dic = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    roman_numerals(N, 1, dic, res)
    for char in "IVXLCDM":
        if char in res:
            print >>fout, char, res[char]
def roman_numerals(N, num, dic, res):
    if num > N:
        return
    temp = []
    t = -1
    a = num
    while num != 0:
        m = num % 10
        num /= 10
        t += 1
        if m == 1:
            temp.append(dic[pow(10, t)])
        if m == 2:
            temp.append(dic[pow(10, t)] + dic[pow(10, t)])
        if m == 3:
            temp.append(dic[pow(10, t)] + dic[pow(10, t)] + dic[pow(10, t)])
        if m == 4:
            temp.append(dic[pow(10, t)] + dic[5 * pow(10, t)])
        if m == 5:
            temp.append(dic[5 * pow(10, t)])
        if m == 6:
            temp.append(dic[5 * pow(10, t)] + dic[pow(10, t)])
        if m == 7:
            temp.append(dic[5 * pow(10, t)] + dic[pow(10, t)] + dic[pow(10, t)])
        if m == 8:
            temp.append(dic[5 * pow(10, t)] + dic[pow(10, t)] + dic[pow(10, t)] + dic[pow(10, t)])
        if m == 9:
            temp.append(dic[pow(10, t)] + dic[pow(10, (t + 1))])
    for p in temp:
        for s in p:
            if s not in res:
                res[s] = 1
            else:
                res[s] += 1
    roman_numerals(N, a + 1, dic, res)
if __name__ == "__main__":
    solution()
    