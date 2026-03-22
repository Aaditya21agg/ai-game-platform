from tictactoe.game import check_winner

def is_moves_left(board):
    return any(cell ==" " for row in board for cell in row)

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif not is_moves_left(board):
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score
    
def best_move(board):
        best_score = -float('inf')
        move = (0,0)

        for i in range(3):
            for j in range(3):
                if board[i][j] ==" ":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = " "

                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move