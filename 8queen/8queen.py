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
        row = 8 - num
        for col in range(0, 8):
            if search_three_directions(row, col, num, board):
                new_board = copy.deepcopy(board)
                new_board[row][col] = 1
                queen8(num - 1, new_board)
def search_three_directions(row, col, num, board):
    for i in range(0, row):
        if board[i][col] == 1:
            return False
    row_to_leftdown = row
    col_to_leftup = col
    while row_to_leftdown >= 0 and col_to_leftup >= 0:
        if board[row_to_leftdown][col_to_leftup] == 0:
            row_to_leftdown -= 1
            col_to_leftup -= 1
        else:
            return False
    row_to_leftup = row
    col_to_leftup = col
    while row_to_leftup >= 0 and col_to_leftup <= 7:
        if board[row_to_leftup][col_to_leftup] == 0:
            row_to_leftup -= 1
            col_to_leftup += 1
        else:
            return False
    return True
board = []
for h in range(0, 8):
    arr = []
    for w in range(0, 8):
        arr.append(0)
    board.append(arr)
res = 0
queen8(8, board)
print res
