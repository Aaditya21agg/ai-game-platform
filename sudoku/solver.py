def is_valid(board, row, col, num):
    # Check row
    if num in board[row]:
        return False
    
    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False
        
    # Check 3x3 box
    start_row = row - row%3
    start_col = col - col%3

    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col+j]==num:
                return False
            
    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i,j
    return None

def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True
    
    row, col =empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True
            
            board[row][col] = 0
    return False