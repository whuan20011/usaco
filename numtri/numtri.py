"""
ID: whuan2001
LANG: PYTHON2
TASK: numtri
"""
import copy
def solution():
    fin = open("numtri.in", "r")
    fout = open("numtri.out", "w")
    row = int(fin.readline().strip())
    numtri = []
    for line in fin.readlines():
        arr = map(int, line.strip().split())
        numtri.append(arr)
    if len(numtri) == 1:
        print >>fout, sum(numtri[0])
    else:
        res = []
        diff_path_sum(numtri, row, [], [], res)
        print >>fout, max(res)
def diff_path_sum(numtri, row, cur_list, cur_index, res):
    if len(cur_list) == row:
        res.append(sum(cur_list))
        return
    else:
        if not cur_list:
            cur_index.append([0, 0])
            cur_list.append(numtri[0][0])
            diff_path_sum(numtri, row, cur_list, cur_index, res)
        else:
            cur_index1 = copy.deepcopy(cur_index)
            cur_list1 = copy.deepcopy(cur_list)
            cur_index1.append([cur_index[-1][0] + 1, cur_index[-1][1]])
            cur_list1.append(numtri[cur_index[-1][0] + 1][cur_index[-1][1]])
            diff_path_sum(numtri, row, cur_list1, cur_index1, res)
            cur_index2 = copy.deepcopy(cur_index)
            cur_list2 = copy.deepcopy(cur_list)
            cur_index2.append([cur_index[-1][0] + 1, cur_index[-1][1] + 1])
            cur_list2.append(numtri[cur_index[-1][0] + 1][cur_index[-1][1] + 1])
            diff_path_sum(numtri, row, cur_list2, cur_index2, res)
if __name__ == "__main__":
    solution()  
    