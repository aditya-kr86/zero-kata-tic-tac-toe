import os
import time

# ASCII Art
GAME_INTRO = r'''
Welcome to Advanced Tic Tac Toe!
'''

O_WINS = "O Wins! Better luck next time!"
X_WINS = "Computer Wins! You cannot defeat me!"
DRAW = "It's a draw!"
O_TURN = "Your Turn (O)."
X_TURN = "Computer's Turn (X)."

# Helper Functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(box_values):
    print(f" {box_values[0]} | {box_values[1]} | {box_values[2]}")
    print(f"---|---|---")
    print(f" {box_values[3]} | {box_values[4]} | {box_values[5]}")
    print(f"---|---|---")
    print(f" {box_values[6]} | {box_values[7]} | {box_values[8]}")

def check_winner(board, marker):
    WIN_COMBINATIONS = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(all(board[i] == marker for i in combo) for combo in WIN_COMBINATIONS)

def is_draw(board):
    return all(isinstance(cell, str) for cell in board)

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return 10 - depth
    if check_winner(board, 'O'):
        return depth - 10
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if isinstance(board[i], int):  # Check if the cell is empty
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = i + 1  # Undo move
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if isinstance(board[i], int):
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = i + 1  # Undo move
                best_score = min(score, best_score)
        return best_score

def computer_turn(board):
    best_score = float('-inf')
    best_move = None
    for i in range(9):
        if isinstance(board[i], int):  # Check if the cell is empty
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = i + 1  # Undo move
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def player_turn(board):
    while True:
        try:
            choice = int(input(f"{O_TURN}\nChoose your box (1-9): "))
            if 1 <= choice <= 9 and isinstance(board[choice - 1], int):
                return choice - 1
            print("Invalid choice. Try again!")
        except ValueError:
            print("Please enter a number.")

def play_game():
    # Initialize game board
    board = [i + 1 for i in range(9)]
    clear_screen()
    print(GAME_INTRO)

    while True:
        print_board(board)

        # Player's Turn
        player_move = player_turn(board)
        board[player_move] = 'O'
        clear_screen()
        if check_winner(board, 'O'):
            print_board(board)
            print(O_WINS)
            return
        if is_draw(board):
            print_board(board)
            print(DRAW)
            return

        # Computer's Turn
        print(X_TURN)
        time.sleep(1)
        computer_move = computer_turn(board)
        board[computer_move] = 'X'
        clear_screen()
        if check_winner(board, 'X'):
            print_board(board)
            print(X_WINS)
            return
        if is_draw(board):
            print_board(board)
            print(DRAW)
            return

# Main Loop
def main():
    while True:
        play_game()
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thank you for playing Tic Tac Toe!")
            break
        clear_screen()

if __name__ == "__main__":
    main()
