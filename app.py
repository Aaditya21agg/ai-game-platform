import streamlit as st
mode = st.selectbox("Choose Game:", ["Tic Tac Toe", "Sudoku"])
if mode == "Tic Tac Toe":
    
    from tictactoe.ai import best_move
    from tictactoe.utils import check_winner

    st.title("Welcome to AI Gaming")
    if "player" not in st.session_state:
        st.session_state.player = "X"
    choice = st.radio("Chosse your symbol:", ["X", "O"])

    st.session_state.player = choice
    ai_player = "O" if choice  == "X" else "X"

    if "board" not in st.session_state:
        st.session_state.board = [[" "]*3 for _ in range(3)]
        st.session_state.current = "X"
    if "game_over" not in st.session_state:
        st.session_state.game_over = False

    board = st.session_state.board
    # AI plays first if user chooses O
    if st.session_state.player == "O" and all(cell ==" " for row in board for cell in row):
        ai_player = "X"
        ai_i, ai_j = best_move(board, ai_player)
        board[ai_i][ai_j]= ai_player

    def make_move(i, j):
        if st.session_state.game_over:
            return
        player = st.session_state.player
        
        
        if board[i][j] == " ":
            board[i][j] = player
            winner = check_winner(board)
            if winner:
                if winner == player:
                    st.success("🎉 You win!")
                else:
                    st.error("🤖 AI wins!")   
                st.session_state.game_over = True
                st.stop()     
            if all(cell != " " for row in board for cell in row):
                st.info("Draw!")
                st.session_state.game_over = True
                st.rerun()
                return
            
            # AI move
            ai_player = "O" if player == "X" else "X"
            ai_i, ai_j = best_move(board, ai_player)
            board[ai_i][ai_j] = ai_player

            winner = check_winner(board)
            if winner:
                st.success(f"{winner} wins!")
                st.session_state.game_over = True
                st.stop()
                
            
            if all(cell!=" " for row in board for cell in row):
                st.info("Draw!")
                st.session_state.game_over = True
                st.rerun()
                return 
        st.rerun()       
    for i in range(3):
            cols = st.columns(3)
            for j in range(3):
                if cols[j].button(board[i][j] or " ", key=f"{i}-{j}"):
                    make_move(i, j)

    if st.button("Reset"):
        st.session_state.board = [[" "]*3 for _ in range(3)]
        st.session_state.game_over = False

elif mode == "Sudoku":
    st.header("Sudoku Solver")

    from sudoku.solver import solve_sudoku, is_valid
    from sudoku.generator import generate_puzzle

    # Initializing board
    if "sudoku_board" not in st.session_state:
        st.session_state.sudoku_board = generate_puzzle()
    board = st.session_state.sudoku_board

        # create grid input
    for i in range(9):
            if i%3 == 0 and i!=0:
                st.markdown("---")
            cols = st.columns([1,1,1,0.3,1,1,1,0.3,1,1,1])
            col_idx=0
            for j in range(9):
                if j%3 == 0 and j!=0:
                    col_idx+=1
                is_fixed = board[i][j] != 0
                value = cols[col_idx].text_input(
                    "",
                    value = str(board[i][j]) if board[i][j]!= 0 else "",
                    key = f"cell-{i}-{j}",
                    max_chars=1,
                    disabled=is_fixed
                )
                if value.isdigit():
                    board[i][j] = int(value)
                else:
                    board[i][j] = 0
                col_idx+=1

    # Buttons
    col1, col2, col3, col4= st.columns(4)

    with col1:
        if st.button("Solve"):
            temp_board = [row[:] for row in board] 
            if solve_sudoku(temp_board):
                st.session_state.sudoku_board = temp_board
                st.success("Solved!")
            else:
                st.error("No solution exists")

    with col2:
        if st.button("clear"):
            st.session_state.sudoku_board = [[0]*9 for _ in range(9)]
    with col3:
        if st.button("Check"):
            temp = [row[:] for row in board]
            solved = [row[:] for row in board] 

            if solve_sudoku(solved) and temp == solved:
                st.success("✅ Correct solution!")   
            else:
                st.error("❌ Incorrect solution")
    with col4:
        if st.button("New Puzzle"):
            st.session_state.sudoku_board = generate_puzzle()