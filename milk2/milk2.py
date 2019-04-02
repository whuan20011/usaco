"""
ID: whuan2001
LANG: PYTHON2
TASK: milk2
"""
fin = open("milk2.in", "r")
num_famers = int(fin.readline().strip())
fout = open("milk2.out", "w")
segments = []
for line in fin.readlines():
    segments.append(tuple(map(int, line.strip().split())))
segments = set(segments)
segments = sorted(segments)
new_segments = [list(segments[0])]
for i  in range(1, len(segments)):
    if segments[i][0] <= new_segments[-1][1] and segments[i][1] > new_segments[-1][1]:
        new_segments[-1][1] = segments[i][1]
    elif segments[i][0] < new_segments[-1][1] and segments[i][1] <= new_segments[-1][1]:
        continue
    elif segments[i][0] > new_segments[-1][1]:
        new_segments.append(list(segments[i]))
if len(new_segments) == 1:
    print >> fout, new_segments[0][1] - new_segments[0][0], 0
else:
    longest_feed = 0
    longest_nofeed = 0
    for new in new_segments:
        longest_feed = max(longest_feed, new[1] - new[0])
    for j in range(1, len(new_segments)):
        longest_nofeed = max(longest_nofeed, new_segments[j][0] - new_segments[j - 1][1])
    print >> fout, longest_feed, longest_nofeed
