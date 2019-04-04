"""
ID: whuan2001
LANG: PYTHON2
TASK: milk
"""
def solution():
    fin = open("milk.in", "r")
    sum_milk, num_farmers = map(int, fin.readline().strip().split())
    prices = []
    dic = {}
    for line in fin.readlines():
        price, produce = map(int, line.strip().split())
        prices.append(price)
        if price not in dic:
            dic[price] = produce
        else:
            dic[price] += produce
    prices = set(prices)
    prices = sorted(list(prices))
    cur_sum_milk = 0
    res = 0
    for i in range(len(prices)):
        if cur_sum_milk + dic[prices[i]] <= sum_milk:
            res += prices[i] * dic[prices[i]]
            cur_sum_milk += dic[prices[i]]
        else:
            res += prices[i] * (sum_milk - cur_sum_milk)
            break
    fout = open("milk.out", "w")
    print >> fout, res
if __name__ == "__main__":
    solution()
    