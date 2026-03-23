import random
from sudoku.solver import solve_sudoku

def generate_full_board():
    board = [[0]*9 for _ in range(9)]
    solve_sudoku(board) # fills it 
    return board

def remove_numbers(board, difficulty=40): # difficulty - number of cells to remove
    removed = 0
    while removed < difficulty:
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        if board[row][col]!=0:
            board[row][col]=0
            removed+=1
    return board

def generate_puzzle():
    board = generate_full_board()
    puzzle = remove_numbers(board, difficulty=40)
    return puzzle

