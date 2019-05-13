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
    for res in create_primes(N, N, primes):
        print >>fout, res
def create_primes(N, num, primes):
    if num == 0:
        return primes
    else:
        cur_digit_primes = []
        if num == N:
            primes = [2, 3, 5, 7]
        else:
            for p in primes:
                for q in (1, 3, 5, 7, 9):
                    if is_prime(p * 10 + q):
                        cur_digit_primes.append(p * 10 + q)
            primes = cur_digit_primes
        return create_primes(N, num - 1, primes)
def is_prime(a):
    if a == 2:
        return True
    for k in range(3, int(math.sqrt(a)) + 1):
        if a % k == 0:
            return False
    return True
if __name__ == "__main__":
    solution()
    