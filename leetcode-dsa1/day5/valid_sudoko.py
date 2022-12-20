# class Solution:
def isValidSudoku(board):
    s = set()
    i=j=0
    for i in range(9):
        if board[i][j] in s:
            s.add(board[i][j])
        else:
            return False
        if i == 8:
            s.clear()
    i=j=0
    for j in range(9):
        if board[i][j] in s:
            s.add(board[i][j])
        else:
            return False
        if i == 8:
            s.clear()

    b = board[:3][:3]
    for i in range(3):
        for j in range(3):
            if board[i][j] in s:
                s.add(board[i][j])
            else:
                return False
        if i == 2 and j == 2:
            s.clear()
    
    b = board[:3][3:6]
    for i in range(3):
        for j in range(3):
            if board[i][j] in s:
                s.add(board[i][j])
            else:
                return False
        if i == 2 and j == 2:
            s.clear()
    
    b = board[:3][6:]
    for i in range(3):
        for j in range(3):
            if board[i][j] in s:
                s.add(board[i][j])
            else:
                return False
        if i == 2 and j == 2:
            s.clear()
    
    b = board[3:6][:3]
    for i in range(3):
        for j in range(3):
            if board[i][j] in s:
                s.add(board[i][j])
            else:
                return False
        if i == 2 and j == 2:
            s.clear()
    
    b = board[3:6][3:6]
    for i in range(3):
        for j in range(3):
            if board[i][j] in s:
                s.add(board[i][j])
            else:
                return False
        if i == 2 and j == 2:
            s.clear()
    
    b = board[3:6][6:]
    for i in range(3):
        for j in range(3):
            if board[i][j] in s:
                s.add(board[i][j])
            else:
                return False
        if i == 2 and j == 2:
            s.clear()
    
    b = board[6:][:3]
    for i in range(3):
        for j in range(3):
            if board[i][j] in s:
                s.add(board[i][j])
            else:
                return False
        if i == 2 and j == 2:
            s.clear()
    
    b = board[6:][3:6]
    for i in range(3):
        for j in range(3):
            if board[i][j] in s:
                s.add(board[i][j])
            else:
                return False
        if i == 2 and j == 2:
            s.clear()
    
    b = board[6:][6:]
    for i in range(3):
        for j in range(3):
            if board[i][j] in s:
                s.add(board[i][j])
            else:
                return False
        if i == 2 and j == 2:
            s.clear()
    
    return True
isValidSudoku(print([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
