def main():
    while True:
        print("\n=== AI GAME PLATFORM===")
        print("1. Tic Tac Toe")
        print("2. Sudoku Solver")
        print("3. Exit")

        choice  = input("Enter choice: ")

        if choice == '1':
            from tictactoe.game import play_game
            play_game()

        #elif choice == '2':
           # from sudoku.board import run_sudoku
           # run_sudoku()

        elif choice == '3':
            print("Exiting..")
            break

        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main()