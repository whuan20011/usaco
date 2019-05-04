"""
ID: whuan2001
LANG: PYTHON2
TASK: pprime
"""
import math
import cProfile
def solution():
    fin = open("pprime.in", "r")
    fout = open("pprime.out", "w")
    a, b = map(int, fin.readline().strip().split())
    res = []
    if a < 10:
        for k in range(a, 10):
            if prime(k):
                res.append(k)
    for num in range(1, 10000):
        palindromes = creat_palindrome(num, a, b)
        for palindrome in palindromes:
            if palindrome % 2 != 0 and prime(palindrome):
                res.append(palindrome)
    res = sorted(res)
    for r in res:
        print >>fout, r
def creat_palindrome(num, a, b):
    arr = []
    new_num1 = int(str(num) + str(num)[::-1])
    if new_num1 >= a and new_num1 <= b:
        arr.append(new_num1)
    for m in range(0, 10):
        new_num2 = int(str(num) + str(m) + str(num)[::-1])
        if new_num2 >= a and new_num2 <= b:
            arr.append(new_num2)
    return arr
def prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
if __name__ == "__main__":
    solution()
	