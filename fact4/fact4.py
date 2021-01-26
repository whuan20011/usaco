"""
ID: whuan2001
LANG: PYTHON2
TASK: fact4
"""
def solution():
    fin = open("fact4.in", "r")
    fout = open("fact4.out", "w")
    N = int(fin.readline().strip())
    num = 1
    temp = 1
    count_2 = 0
    count_5 = 0
    while num <= N:
        a = num
        while num % 2 == 0 or num % 5 == 0:
            if num % 2 == 0:
                num /= 2
                count_2 += 1
            if num % 5 == 0:
                num /= 5
                count_5 += 1
        temp *= num
        temp %= 10
        num = a + 1
    for _ in range(count_2 - count_5):
        temp *= 2
        temp %= 10
    print >>fout, temp
if __name__ == "__main__":
    solution()
    