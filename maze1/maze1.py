"""
ID: whuan2001
LANG: PYTHON2
TASK: maze1
"""
def solution():
    fin = open("maze1.in", "r")
    fout = open("maze1.out", "w")
    W, H = map(int, fin.readline().strip().split())
    maze = []
    for line in fin.readlines():
        maze.append(list(line.strip("/n")))
    exits = []
    for row in [0, 2 * H]:
        for j in range(1, W + 1):
            col = 2 * j - 1
            if maze[row][col] == " ":
                exits.append((row, col))
    for i in range(1, H + 1):
        row = 2 * i - 1
        for col in [0, 2 * W]:
            if maze[row][col] == " ":
                exits.append((row, col))
    a = find_farthest_route(W, H, maze, exits[0])
    b = find_farthest_route(W, H, maze, exits[1])
    longest = 0
    for point in a:
        longest = max(min(a[point], b[point]), longest)
    print >>fout, longest
def find_farthest_route(W, H, maze, exitt):
    visited = set()
    queue = []
    if exitt[0] == 0:
        queue.append(((1, exitt[1]), 1))
    elif exitt[0] == 2 * H:
        queue.append(((2 * H - 1, exitt[1]), 1))
    elif exitt[1] == 0:
        queue.append(((exitt[0], 1), 1))
    elif exitt[1] == 2 * W:
        queue.append(((exitt[0], 2 * W - 1), 1))
    dic = {}
    while queue:
        first = queue.pop(0)
        if first[0] not in visited:
            visited.add(first[0])
            dic[first[0]] = first[1]
        else:
            continue
        x = first[0][0]
        y = first[0][1]
        dis = first[1]
        if maze[x - 1][y] == " " and x >= 3:
            queue.append(((x - 2, y), dis + 1))
        if maze[x + 1][y] == " " and x <= 2 * H - 3:
            queue.append(((x + 2, y), dis + 1))
        if maze[x][y - 1] == " " and y >= 3:
            queue.append(((x, y - 2), dis + 1))
        if maze[x][y + 1] == " " and y <= 2 * W - 3:
            queue.append(((x, y + 2), dis + 1))
    return dic
if __name__ == "__main__":
    solution()
         