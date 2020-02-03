"""
ID: whuan2001
LANG: PYTHON2
TASK: spin
"""
def solution():
    fin = open("spin.in", "r")
    fout = open("spin.out", "w")
    wheels = []
    for line in fin.readlines():
        wheels.append(map(int, line.strip().split()))
    time = 0
    transparents = 0
    while not if_light_pass(wheels, time):
        time += 1
        for wheel in wheels:
            for i in range(wheel[1]):
                wheel[2 * i + 2] = (wheel[0] + wheel[2 * i + 2]) % 360
        if time > 360:
            print >>fout, "none"
            return
    print >>fout, time
def if_light_pass(wheels, time):
    dic = {}
    for wheel in wheels:
        for i in range(wheel[1]):
            for degree in range(wheel[2 * i + 2], wheel[2 * i + 2] + wheel[2 * i + 3] + 1):
                if degree % 360 not in dic:
                    dic[degree % 360] = 0
                dic[degree % 360] += 1
    for i in dic:
        if dic[i] == 5:
            return True
    return False
if __name__ == "__main__":
    solution()
                                           