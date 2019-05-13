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
                    val = floorplan[idx[0]][idx[1]]
                    neighboors = find_neighboors(idx, val)
                    for nei in neighboors:
                        if nei not in visited:
                            queue.append(nei)
                room += 1
                room_size[room] = len(visited)
                biggest_size = max(biggest_size, len(visited))
                for v in visited:
                    maps[v[0]][v[1]] = room
    bigger_size, cancel_wall = creat_biggersize(maps, m, n, room_size)
    print bigger_size, cancel_wall
    def west_south(a, b):
        if a[1] < b[1]:
            return 1
        elif a[1] == b[1] and a[0] > b[0]:
            return 1
        elif a[1] == b[1] and a[0] == b[0]:
            if a[2] == "N":
                return 1
        return -1
    print >>fout, room
    print >>fout, biggest_size
    print >>fout, bigger_size
    res = sorted(cancel_wall, cmp=west_south)[-1]
    print >>fout, res[0], res[1], res[2]
def creat_biggersize(maps, m, n, room_size):
    bigger_size = 0
    cancel_wall = []
    for i in range(n):
        for j in range(m):
            cur = maps[i][j]
            allneighboors = find_neighboors((i, j), 0)
            for a, neighboor in enumerate(allneighboors):
                #print a, neighboor
                if neighboor[0] >= 0 and neighboor[0] < n and neighboor[1] >= 0 and neighboor[1] < m:
                    if maps[neighboor[0]][neighboor[1]] != cur:
                        if room_size[cur] + room_size[maps[neighboor[0]][neighboor[1]]] > bigger_size:
                            bigger_size = room_size[cur] + room_size[maps[neighboor[0]][neighboor[1]]]
                            cancel_wall = []
                        if room_size[cur] + room_size[maps[neighboor[0]][neighboor[1]]] == bigger_size:
                            if a == 0:
                                cancel_wall.append([i + 1, j + 1, "W"])
                            elif a == 1:
                                cancel_wall.append([i + 1, j + 1, "N"])
                            elif a == 2:
                                cancel_wall.append([i + 1, j + 1, "E"])
                            elif a == 3:
                                cancel_wall.append([i + 1, j + 1, "S"])
    return bigger_size, cancel_wall
def find_neighboors(idx, val):
    directions = []
    neighboors = []
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
    