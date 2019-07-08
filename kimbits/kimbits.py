"""
ID: whuan2001
LANG:PYTHON2
TASK: kimbits
"""
def solution():
    fin = open("kimbits.in", "r")
    fout = open("kimbits.out", "w")
    N, L, I = map(int, fin.readline().strip().split())
    string = ""
    if I == 1:
        for _ in range(N):
            string += "0"
        print >>fout, string
    else:
        count = 1
        dic = {}
        for first_1 in range(1, N + 1):
            m = count
            for behind_1 in range(0, min(L - 1, first_1 - 1) + 1):
                count += dp(first_1 - 1, behind_1, dic)
            if count >= I:
                break
        cur = I - m
        a = first_1
        for _ in range(N - a):
            string += "0"
        string += "1"
        num_of_chosen1 = 1
        for i in range(a - 2, -1, -1):
            if i == 0:
                if cur == 1:
                    string += "0"
                if cur == 2:
                    string += "1"
                break
            temp = 0
            for j in range(0, min(L - num_of_chosen1, a - 1) + 1):
                temp += dp(i, j, dic)
            if temp >= cur:
                string += "0"
            else:
                string += "1"
                num_of_chosen1 += 1
                cur -= temp
        print >>fout, string
def dp(x, y, dic):
    if (x, y) in dic:
        return dic[(x, y)]
    if x == 1 and y == 1:
        return 1
    if x == 2 and y == 1:
        return 2
    if x == 2 and y == 2:
        return 1
    if x < y:
        return 0
    if y == 0:
        return 1
    dic[(x, y)] = dp(x - 1, y, dic) + dp(x - 1, y - 1, dic)
    return dic[(x, y)] 
if __name__ == "__main__":
    solution()
        
            
        