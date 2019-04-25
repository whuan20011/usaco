"""
ID: whuan2001
LANG: PYTHON2
TASK: ariprog
"""
def solution():
    fin = open("ariprog.in", "r")
    fout = open("ariprog.out", "w")
    length, limit = map(int, fin.readlines())
    squares = []
    for l in range(limit + 1):
        squares.append(l * l)
    dic = set()
    bisquares = []
#    print "a"
    for i in range(len(squares)):
        for j in range(i, len(squares)):
            if squares[i] + squares[j] not in dic:
                dic.add(squares[i] + squares[j])
                bisquares.append(squares[i] +squares[j])
    bisquares = sorted(bisquares)
    biggest_diff = (bisquares[-1] - bisquares[0]) / (length - 1) 
    res = []
 #   print "b"
    for diff in range(1, biggest_diff + 1):
        for bisquare in bisquares:
            c = bisquare + diff
            for k in range(length - 1):
                if c not in dic:
                    break
                c += diff
            if k == length - 2 and bisquare + (k + 1) * diff in dic:
                res.append([bisquare, diff])
#    print "c"
    if not res:
        print >>fout, "NONE"
    for r in res:
        print >>fout, r[0], r[1]
if __name__ == "__main__":
    solution()
    