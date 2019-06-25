"""
ID: whuan2001
LANG: PYTHON2
TASK: inflate
"""
def solution():
    fin = open("inflate.in", "r")
    fout = open("inflate.out", "w")
    M, N = map(int, fin.readline().strip().split())
    points_minutes = []
    for line in fin.readlines():
        points_minutes.append(map(int, line.strip().split()))
    chart = []
    for _ in range(N):
        chart.append([0] * (M + 1))
    for j in range(1, M + 1):
        for i in range(N):
            if i == 0:
                if j >= points_minutes[i][1]:
                    chart[i][j] = (j / points_minutes[i][1]) * points_minutes[i][0]
                else:
                    chart[i][j] = 0
            else:
                if j >= points_minutes[i][1]:
                    chart[i][j] = max(chart[i][j - points_minutes[i][1]] + points_minutes[i][0], chart[i - 1][j])
                else:
                    chart[i][j] = chart[i - 1][j]
    print >>fout, chart[N -1][M]
if __name__ == "__main__":
    solution()
    