"""
ID: whuan2001
LANG: PYTHON2
TASK: msquare
"""
def solution():
    fin = open("msquare.in", "r")
    fout = open("msquare.out", "w")
    a = map(int, fin.readline().strip().split())
    target = [[a[0], a[1], a[2], a[3]], [a[7], a[6], a[5], a[4]]]
    initial = [[1, 2, 3, 4], [8, 7, 6, 5]]
    queue = [(initial, 0, "")]
    visited = set()
    while queue:
        cur = queue.pop(0)
        x = tuple(cur[0][0])
        y = tuple(cur[0][1])
        if (x, y) in visited:
            continue
        else:
            visited.add((x, y))
        if cur[0] == target:
            print >>fout, cur[1]
            print >>fout, cur[2]
            return
        else:
            temp_A = exchange_top_bottom(cur[0])
            queue.append((temp_A, cur[1] + 1, cur[2] + "A"))
            temp_B = single_right_shift(cur[0])
            queue.append((temp_B, cur[1] + 1, cur[2] + "B"))
            temp_C = rotation_middle4(cur[0])
            queue.append((temp_C, cur[1] + 1, cur[2] + "C"))
def exchange_top_bottom(arr):
    a, b, c, d, e, f, g, h = arr[0][0], arr[0][1], arr[0][2], arr[0][3], arr[1][0], arr[1][1], arr[1][2], arr[1][3]
    return [[e, f, g, h], [a, b, c, d]]
def single_right_shift(arr):
    a, b, c, d, e, f, g, h = arr[0][0], arr[0][1], arr[0][2], arr[0][3], arr[1][0], arr[1][1], arr[1][2], arr[1][3]
    return [[d, a, b, c], [h, e, f, g]]
def rotation_middle4(arr):
    a, b, c, d, e, f, g, h = arr[0][0], arr[0][1], arr[0][2], arr[0][3], arr[1][0], arr[1][1], arr[1][2], arr[1][3]
    return [[a, f, b, d], [e, g, c, h]]
if __name__ == "__main__":
    solution()
