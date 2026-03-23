from sudoku.solver import solve_sudoku
from sudoku.generator import generate_puzzle

def play_sudoku():
    puzzle = generate_puzzle()
    print("\nSOlve this sudoku:")
    print_board(puzzle)

    user_board=[]
    print("\nEnter your solution:")

    for i in range(9):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        user_board.append(row)

    # Check if solution is correct

    solution = [row[:] for row in puzzle]
    solve_sudoku(solution)

    if user_board == solution:
        print("\n Correct Solution!")
    else:
        print("\n incorrect Solution.")
        print("\nCorrect Answer:")
        print_board(solution)
        
def print_board(board):
    for i in range(9):
        if ((i % 3 ==0) and (i!=0)):
            print("-"*21)

        for j in range(9):
                if (j%3 == 0) and (j!=0):
                    print("|", end=" ")

                print (board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()

def run_sudoku():
    print("\nEnter Sudoku puzzle (0 for empty cells):")

    board = []
    for i in range(9):
        row = list(map(int, input(f"Row {i+1}:").split()))
        board.append(row)

    print("\nOriginal Board:")
    print_board(board)

    if solve_sudoku(board):
        print("\nSolved Board:")
        print_board(board)

    
    else:
        print("No solution exists.")

