import copy
def queen8(num, board):
    if num == 0:
        global res
        res += 1
        print "------------------------------------------------"
        for c in range(8):
            print board[c]
        return
    else:
        temp = 8 - num
        for j in range(0, 8):
            tag = 0
            for i in range(0, temp):
                if board[i][j] == 1:
                    tag = 1
                    break
            if tag == 0:
                p = temp
                q = j
                while p >= 0 and q >= 0:
                    if board[p][q] == 0:
                        p -= 1
                        q -= 1
                    else:
                        tag = 1
                        break
            if tag == 0:
                u = temp
                k = j
                while u >= 0 and k <= 7:
                    if board[u][k] == 0:
                        u -= 1
                        k += 1
                    else:
                        tag = 1
                        break
            if tag == 0:
                new_board = copy.deepcopy(board)
                new_board[temp][j] = 1
                queen8(num - 1, new_board)
board = []
for h in range(0, 8):
    arr = []
    for w in range(0, 8):
        arr.append(0)
    board.append(arr)
res = 0
queen8(8, board)
print res
