"""
ID: whuan2001
LANG: PYTHON2
TASK: preface
"""
import collections
import sys   
sys.setrecursionlimit(4000)
def solution():
    fin = open("preface.in", "r")
    fout = open("preface.out", "w")
    N = int(fin.readline().strip())
    dic = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    num = 1
    all_characters = ""
    while num <= N:    
        t = -1
        a = num
        while num != 0:
            m = num % 10
            num /= 10
            t += 1
            if m == 1:
                all_characters += dic[pow(10, t)]
            if m == 2:
                all_characters += dic[pow(10, t)] + dic[pow(10, t)]
            if m == 3:
                all_characters += dic[pow(10, t)] + dic[pow(10, t)] + dic[pow(10, t)]
            if m == 4:
                all_characters += dic[pow(10, t)] + dic[5 * pow(10, t)]
            if m == 5:
                all_characters += dic[5 * pow(10, t)]
            if m == 6:
                all_characters += dic[5 * pow(10, t)] + dic[pow(10, t)]
            if m == 7:
                all_characters += dic[5 * pow(10, t)] + dic[pow(10, t)] + dic[pow(10, t)]
            if m == 8:
                all_characters += dic[5 * pow(10, t)] + dic[pow(10, t)] + dic[pow(10, t)] + dic[pow(10, t)]
            if m == 9:
                all_characters += dic[pow(10, t)] + dic[pow(10, (t + 1))]
        num = a + 1
    res = collections.Counter(all_characters)
    for char in "IVXLCDM":
        if char in res:
            print >>fout, char, res[char]
if __name__ == "__main__":
    solution()
    