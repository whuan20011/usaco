"""
ID: whuan2001
LANG: PYTHON2
TASK: ttwo
"""
def solution():
    fin = open("ttwo.in", "r")
    fout = open("ttwo.out", "w")
    grid = []
    for line in fin.readlines():
        grid.append(list(line.strip()))
    for i in range(10):
        for j in range(10):
            if grid[i][j] == "F":
                fx = i
                fy = j
            if grid[i][j] == "C":
                cx = i
                cy = j
    f_dir = "N"
    c_dir = "N"
    time = 0
    dic = {}
    while fx != cx or fy != cy:
        time += 1
        if (fx, fy, f_dir) in dic:
            if (cx, cy, c_dir) in dic[(fx, fy, f_dir)]:
                time = 0
                break
            else:
                dic[(fx, fy, f_dir)].append((cx, cy, c_dir))
        else:
            dic[(fx, fy, f_dir)] = [(cx, cy, c_dir)]
        fx, fy, f_dir = next_step(grid, fx, fy, f_dir)
        cx, cy, c_dir = next_step(grid, cx, cy, c_dir)
    print >>fout, time
def next_step(grid, x, y, direction):
    grid[x][y] = "."
    if direction == "N":
        if x - 1 >= 0 and grid[x - 1][y] != "*":
            x -= 1
        else:
            direction = "E"
    elif direction == "E":
        if y + 1 < 10 and grid[x][y + 1] != "*":
            y += 1
        else:
            direction = "S"
    elif direction == "S":
        if x + 1 < 10 and grid[x + 1][y] != "*":
            x += 1
        else:
            direction = "W"
    elif direction == "W":
        if y - 1 >= 0 and grid[x][y - 1] != "*":
            y -= 1
        else:
            direction = "N"
    return x, y, direction
if __name__ == "__main__":
    solution()
