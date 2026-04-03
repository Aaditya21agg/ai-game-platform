from tictactoe.utils import check_winner

def is_moves_left(board):
    return any(cell ==" " for row in board for cell in row)

def minimax_alpha_beta(board,depth, alpha, beta ,is_maximizing, ai_player):
    human ="O" if ai_player == "X" else "X"
    winner = check_winner(board)
    if winner == ai_player:
        return 1 - depth
    elif winner == human:
        return -1 + depth
    elif not is_moves_left(board):
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = ai_player
                    score = minimax_alpha_beta(board,depth+1, alpha,beta ,False, ai_player)
                    board[i][j] = " "
                    best_score = max(score, best_score)
                    alpha = max(alpha,score)

                    if beta<=alpha:
                        break
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = human
                    score = minimax_alpha_beta(board,depth+1, alpha,beta, True, ai_player)
                    board[i][j] = " "
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                if beta<=alpha:
                        break
            if beta<= alpha:
                break

        return best_score
    
def best_move(board, ai_player):
        best_score = -float('inf')
        move = (0,0)

        human  = "O" if ai_player == "X" else "X"
        for i in range(3):
            for j in range(3):
                if board[i][j] ==" ":
                    board[i][j] = ai_player
                    score = minimax_alpha_beta(board,0,-float('inf'),float('inf'), False, ai_player)
                    board[i][j] = " "

                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move