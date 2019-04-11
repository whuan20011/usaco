"""
ID: whuan2001
LANG: PYTHON2
TASK: barn1
"""
def solution():
    fin = open("barn1.in", "r")
    fout = open("barn1.out", "w")
    max_purchase, total_barns, occupied = map(int, fin.readline().strip().split())
    if max_purchase >= occupied:
        print >>fout, occupied
        return
    gates = []
    for gate in fin.readlines():
        gates.append(int(gate.strip()))
    gates = sorted(gates)
    spaces = [cur - pre for cur, pre in zip(gates[1:], gates)]
    spaces = sorted(spaces, reverse=True)
    count = sum(spaces[:max_purchase - 1])
    print >>fout, gates[-1] - gates[0] + 1 - count + max_purchase - 1
if __name__ == "__main__":
    solution()
    