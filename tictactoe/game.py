def print_board(board):
    for row in board:
        print("|".join(row))
        print("-"*5)

def check_winner(board):
            # rows
            for row in board:
                if row[0] == row[1] == row[2] and row[0]!=" ":
                    return row[0]
                
            # columns
            for col in range(3):
                if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
                    return board[0][col]
                
            # Diagonals
            if board[0][0] == board[1][1] == board[2][2]  and board[0][0] !=" ":
                return board[0][0]
            
            if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
                return board[0][2]
            
            return None
from tictactoe.ai import best_move      
def play_game():
            board = [[" "]*3 for _ in range(3)]
            current = "X"

            while True:
                print_board(board)

                if current == "X":
                     # Human Move
                     try: 
                          
                          row = int(input("Enter row (0-2): "))
                          col = int(input("Enter col (0-2): "))
                     except ValueError:
                          print("Invalid input!")
                          continue
                     if not (0<= row <=2 and 0<=col <=2):
                          print("Out of range!")
                          continue
                else:
                     # AI move
                     print("AI is thinking...")
                     row, col = best_move(board)

                if board[row][col]!= " ":
                     print("Invalid move!")
                     continue
                
                board[row][col] = current

                winner = check_winner(board)
                if winner:
                     print_board(board)
                     print(f"{winner} wins!")
                     break
                
                
                if all(cell !=" " for row in board for cell in row):
                     print_board(board)
                     print("Draw!")
                     break
                
                current ="O" if current =="X" else "X"
                