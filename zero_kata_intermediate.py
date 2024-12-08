import os
import random
import time
# ASCII Art
GAME_INTRO = r'''
                                                    .     .d8888b.                                  
    O))))                         O))      O))      .    d88P  Y88b                                 
  O))    O))                       O))   O))        .    888    888                                 
O))        O))                      O)) O))         .    888         8888b.  88888b.d88b.   .d88b.  
O))        O))       O)))))           O))           .    888  88888     "88b 888 "888 "88b d8P  Y8b 
O))        O))                      O)) O))         .    888    888 .d888888 888  888  888 88888888 
  O))     O))                      O))   O))        .    Y88b  d88P 888  888 888  888  888 Y8b.     
    O))))                         O))      O))      .     "Y8888P88 "Y888888 888  888  888  "Y8888  
'''
O_WINS = r'''
Y88b   d88P                       .d88  .d88888b.  88b.        888       888 d8b               888 
 Y88b d88P                       d88P" d88P" "Y88b "Y88b       888   o   888 Y8P               888 
  Y88o88P                       d88P   888     888   Y88b      888  d8b  888                   888 
   Y888P  .d88b.  888  888      888    888     888    888      888 d888b 888 888 88888b.       888 
    888  d88""88b 888  888      888    888     888    888      888d88888b888 888 888 "88b      888 
    888  888  888 888  888      Y88b   888     888   d88P      88888P Y88888 888 888  888      Y8P 
    888  Y88..88P Y88b 888       Y88b. Y88b. .d88P .d88P       8888P   Y8888 888 888  888       "  
    888   "Y88P"   "Y88888        "Y88  "Y88888P"  88P"        888P     Y888 888 888  888      888 
'''
X_WINS = r'''
Y88b   d88P      888       888 d8b                   
 Y88b d88P       888   o   888 Y8P                   
  Y88o88P        888  d8b  888                       
   Y888P         888 d888b 888 888 88888b.  .d8888b  
   d888b         888d88888b888 888 888 "88b 88K      
  d88888b        88888P Y88888 888 888  888 "Y8888b. 
 d88P Y88b       8888P   Y8888 888 888  888      X88 
d88P   Y88b      888P     Y888 888 888  888  88888P' 
'''
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

def check_wins(player_points, win_combinations):
    return any(sum(player_points[i] for i in win) == 3 for win in win_combinations)

def player_turn(available_options):
    while True:
        try:
            choice = int(input(f"{O_TURN}\nChoose your box (1-9): "))
            if choice in available_options:
                return choice - 1
            print("Invalid choice. Try again!")
        except ValueError:
            print("Please enter a number.")

def computer_turn(available_options):
    return random.choice(available_options) - 1

def play_game():
    # Initialize game variables
    box_show_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    available_options = list(range(1, 10))
    O_Points = [0] * 9
    X_Points = [0] * 9
    WIN_COMBINATIONS = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    while available_options:
        print_board(box_show_values)

        # Player's Turn
        o_index = player_turn(available_options)
        available_options.remove(o_index + 1)
        box_show_values[o_index] = 'O'
        O_Points[o_index] = 1

        if check_wins(O_Points, WIN_COMBINATIONS):
            clear_screen()
            print_board(box_show_values)
            print(O_WINS)
            return

        if not available_options:
            break

        # Computer's Turn
        print(X_TURN)
        print(r'''
                                                               (( _______
                                                     _______     /\O    O\
                                                    /O     /\   /  \      \
                                                   /   O  /O \ / O  \O____O\ ))
                                                ((/_____O/    \\    /O     /
                                                  \O    O\    / \  /   O  /
                                                   \O    O\ O/   \/_____O/
                                                    \O____O\/ ))          ))
                                                  ((
        ''')
        time.sleep(1)
        x_index = computer_turn(available_options)
        available_options.remove(x_index + 1)
        box_show_values[x_index] = 'X'
        X_Points[x_index] = 1

        if check_wins(X_Points, WIN_COMBINATIONS):
            clear_screen()
            print_board(box_show_values)
            print(X_WINS)
            return

        clear_screen()

    print_board(box_show_values)
    print(DRAW)

# Main Loop
def main():
    print(GAME_INTRO)
    while True:
        play_game()
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thank you for playing Tic Tac Toe!")
            break
        clear_screen()

if __name__ == "__main__":
    main()
