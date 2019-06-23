"""
ID: whuan2001
LANG: PYTHON2
TASK: humble
"""
def solution():
    fin = open("humble.in", "r")
    fout = open("humble.out", "w")
    K, N = map(int, fin.readline().strip().split())
    S = map(int, fin.readline().strip().split())
    generate_nums = [1]
    pos = [0 for _ in S]
    while len(generate_nums) < N + 1:
        smallest = float('inf')
        for index in range(len(S)):
            for i in xrange(pos[index], len(generate_nums)):
                if S[index] * generate_nums[i] > generate_nums[-1]:
                    pos[index] = i
                    smallest = min(smallest, S[index] * generate_nums[i])
                    break
        generate_nums.append(smallest)
    print >>fout, generate_nums[-1]
if __name__ == "__main__":
    solution()
