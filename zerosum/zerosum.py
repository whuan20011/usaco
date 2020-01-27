"""
ID: whuan2001
LANG: PYTHON2
TASK: zerosum
"""
def solution():
    fin = open("zerosum.in", "r")
    fout = open("zerosum.out", "w")
    N = int(fin.readline().strip())
    nums = []
    res = []
    nums_links = ""
    calculated_nums = []
    dfs(N, 1, 1, calculated_nums, nums_links, res)
    res = sorted(res)
    for r in res:
        print >>fout, r
def dfs(N, cur_num, num, calculated_nums, nums_links, res):
    if num == N:
        if sum(calculated_nums) + cur_num == 0:
            res.append(nums_links + str(num))
        return
    for char in ["+", "-", " "]:
        if char == "+":
            calculated_nums.append(cur_num)
            dfs(N, num + 1, num + 1, calculated_nums, nums_links + str(num) + char, res)
            calculated_nums.pop(-1)
        elif char == "-":
            calculated_nums.append(cur_num)
            dfs(N, -num - 1, num + 1, calculated_nums, nums_links + str(num) + char, res)
            calculated_nums.pop(-1)
        elif char == " ":
            if cur_num > 0:
                dfs(N, cur_num  * 10 + num + 1, num + 1, calculated_nums, nums_links + str(num) + char, res)
            else:
                dfs(N, cur_num  * 10 - num - 1, num + 1, calculated_nums, nums_links + str(num) + char, res)
if __name__ == "__main__":
    solution()
