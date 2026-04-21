import math

# Initialize board
board = [' ' for _ in range(9)]

# Print board
def print_board():
    print()
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("---|---|---")
    print()

# Check winner
def check_winner(bd, player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    for pos in win_positions:
        if bd[pos[0]] == bd[pos[1]] == bd[pos[2]] == player:
            return True
    return False

# Check draw
def is_draw(bd):
    return ' ' not in bd

# Minimax Algorithm
def minimax(bd, depth, is_max):
    if check_winner(bd, 'O'):
        return 1
    if check_winner(bd, 'X'):
        return -1
    if is_draw(bd):
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if bd[i] == ' ':
                bd[i] = 'O'
                score = minimax(bd, depth+1, False)
                bd[i] = ' '
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if bd[i] == ' ':
                bd[i] = 'X'
                score = minimax(bd, depth+1, True)
                bd[i] = ' '
                best = min(best, score)
        return best

# Best move for AI
def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Game loop
def play_game():
    print("Positions are numbered 1 to 9:")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")

    while True:
        print_board()

        # Player move
        try:
            pos = int(input("Enter your move (1-9): ")) - 1
            if board[pos] != ' ':
                print("Position already taken!")
                continue
        except:
            print("Invalid input!")
            continue

        board[pos] = 'X'

        if check_winner(board, 'X'):
            print_board()
            print("You win!")
            break
        if is_draw(board):
            print_board()
            print("Draw!")
            break

        # AI move
        ai_move = best_move()
        board[ai_move] = 'O'

        if check_winner(board, 'O'):
            print_board()
            print("AI wins!")
            break
        if is_draw(board):
            print_board()
            print("Draw!")
            break

# Run game
play_game()