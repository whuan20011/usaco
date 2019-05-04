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
        search_accessible_place(num, board)
def search_accessible_place(num, board):
    temp = 8 - num
    for j in range(0, 8):
        tag = 0
        for i in range(0, temp):
            if board[i][j] == 1:
                tag = 1
                break
        if tag == 0:
            row_to_leftdown = temp
            col_to_leftup = j
            while row_to_leftdown >= 0 and col_to_leftup >= 0:
                if board[row_to_leftdown][col_to_leftup] == 0:
                    row_to_leftdown -= 1
                    col_to_leftup -= 1
                else:
                    tag = 1
                    break
        if tag == 0:
            row_to_leftup = temp
            col_to_leftup = j
            while row_to_leftup >= 0 and col_to_leftup <= 7:
                if board[row_to_leftup][col_to_leftup] == 0:
                    row_to_leftup -= 1
                    col_to_leftup += 1
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
