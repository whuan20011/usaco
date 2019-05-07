"""
ID: whuan2001
LANG: PYTHON2
TASK: sprime
"""
import math
def solution():
    fin = open("sprime.in", "r")
    fout = open("sprime.out", "w")
    N = int(fin.readline().strip())
    primes = []
    for res in creat_primes(N, N, primes):
        print >>fout, res
def creat_primes(N, num, primes):
    if num == 0:
        return primes[N - 1]
    else:
        cur_digits_primes = []
        if num == N:
            cur_digits_primes = [2, 3, 5, 7]
            primes.append(cur_digits_primes)
        else:
            for p in primes[-1]:
                for q in (1, 3, 5, 7, 9):
                    if is_prime(p * 10 + q):
                        cur_digits_primes.append(p * 10 + q)
            primes.append(cur_digits_primes)
        return creat_primes(N, num - 1, primes)
def is_prime(a):
    if a == 2:
        return True
    for k in range(3, int(math.sqrt(a)) + 1):
        if a % k == 0:
            return False
    return True
if __name__ == "__main__":
    solution()
        