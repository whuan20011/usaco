"""
ID: whuan2001
LANG: PYTHON2
TASK: castle
"""
def solution():
    fin = open("castle.in", "r")
    fout = open("castle.out", "w")
    m, n = map(int, fin.readline().strip().split())
    floorplan = []
    for line in fin.readlines():
        row = map(int, line.strip().split())
        floorplan.append(row)
    maps = []
    for _ in range(n):
        arr = []
        for _ in range(m):
            arr.append(0)
        maps.append(arr)
    queue = []
    room = 0
    biggest_size = 0
    room_size = {}
    for p in range(n):
        for q in range(m):
            if maps[p][q] == 0:
                visited = set()
                queue.append((p, q))
                while queue:
                    idx = queue.pop()
                    visited.add(idx)
                    neighboors = find_neighboors(idx, floorplan)
                    for nei in neighboors:
                        if nei not in visited:
                            queue.append(nei)
                room += 1
                room_size[room] = len(visited)
                biggest_size = max(biggest_size, len(visited))
                for v in visited:
                    maps[v[0]][v[1]] = room
    bigger_size, cancel_wall = creat_biggersize(maps, m, n, room_size)
    west = n
    south = 0
    for wall in cancel_wall:
        west = min(wall[1], west)
    for wall in cancel_wall:
        if wall[1] == west:
            south = max(wall[0], south)
    print >> fout, room
    print >>fout, biggest_size
    print >>fout,  bigger_size
    res = []
    for wall in cancel_wall:
        if wall[0] == south and wall[1] == west:
            res.append(wall)
    if len(res) == 1:
        print >>fout, res[0][0], res[0][1], res[0][2]
    else:
        for r in res:
            if r[2] == "N":
                print>> fout, r[0], r[1], r[2]
def creat_biggersize(maps, m, n, room_size):
    bigger_size = 0
    cancel_wall = []
    for i in range(n):
        for j in range(m):
            cur = maps[i][j]
            if j - 1 >= 0 and maps[i][j - 1] != cur:
                if room_size[cur] + room_size[maps[i][j - 1]] > bigger_size:
                    bigger_size = room_size[cur] + room_size[maps[i][j - 1]]
                    cancel_wall = [[i + 1, j + 1, "W"]]
                elif room_size[cur] + room_size[maps[i][j - 1]] == bigger_size:
                    cancel_wall.append([i + 1, j + 1, "W"])
            if i + 1 < n and maps[i + 1][j] != cur:
                if room_size[cur] + room_size[maps[i + 1][j]] > bigger_size:
                    bigger_size = room_size[cur] + room_size[maps[i + 1][j]]
                    cancel_wall = [[i + 1, j + 1, "S"]]
                elif room_size[cur] + room_size[maps[i + 1][j]] == bigger_size:
                    cancel_wall.append([i + 1, j + 1, "S"])
            if i - 1 >= 0 and maps[i - 1][j] != cur:
                if room_size[cur] + room_size[maps[i - 1][j]] > bigger_size:
                    bigger_size = room_size[cur] + room_size[maps[i - 1][j]]
                    cancel_wall = [[i + 1, j + 1, "N"]]
                elif room_size[cur] + room_size[maps[i - 1][j]] == bigger_size:
                    cancel_wall.append([i + 1, j + 1, "N"])
            if j + 1 < m and maps[i][j + 1] != cur:
                if room_size[cur] + room_size[maps[i][j + 1]] > bigger_size:
                    bigger_size = room_size[cur] + room_size[maps[i][j + 1]]
                    cancel_wall = [[i + 1, j + 1, "E"]]
                elif room_size[cur] + room_size[maps[i][j + 1]] == bigger_size:
                    cancel_wall.append([i + 1, j + 1, "E"])
    return bigger_size, cancel_wall
def find_neighboors(idx, floorplan):
    directions = []
    neighboors = []
    val = floorplan[idx[0]][idx[1]]
    while val != 0:
        directions.append(val % 2)
        val = val / 2
    for _ in range(4 - len(directions)):
        directions.append(0)
    if directions[0] == 0:
        neighboors.append((idx[0], idx[1] - 1))
    if directions[1] == 0:
        neighboors.append((idx[0] - 1, idx[1]))
    if directions[2] == 0:
        neighboors.append((idx[0], idx[1] + 1))
    if directions[3] == 0:
        neighboors.append((idx[0] + 1 , idx[1]))
    return neighboors
if __name__ == "__main__":
    solution()
    