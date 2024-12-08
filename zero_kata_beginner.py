import os
import random
import time
game_intro = r'''

                                                    .     .d8888b.                                  
    O))))                         O))      O))      .    d88P  Y88b                                 
  O))    O))                       O))   O))        .    888    888                                 
O))        O))                      O)) O))         .    888         8888b.  88888b.d88b.   .d88b.  
O))        O))       O)))))           O))           .    888  88888     "88b 888 "888 "88b d8P  Y8b 
O))        O))                      O)) O))         .    888    888 .d888888 888  888  888 88888888 
  O))     O))                      O))   O))        .    Y88b  d88P 888  888 888  888  888 Y8b.     
    O))))                         O))      O))      .     "Y8888P88 "Y888888 888  888  888  "Y8888  
'''
o_turns = r'''
 .d88888b.       88888888888                                 
d88P" "Y88b          888                                     
888     888          888                                     
888     888          888  888  888 888d888 88888b.  .d8888b  
888     888          888  888  888 888P"   888 "88b 88K      
888     888          888  888  888 888     888  888 "Y8888b. 
Y88b. .d88P          888  Y88b 888 888     888  888      X88 
 "Y88888P"           888   "Y88888 888     888  888  88888P' 
'''
x_wins = r'''
Y88b   d88P      888       888 d8b                   
 Y88b d88P       888   o   888 Y8P                   
  Y88o88P        888  d8b  888                       
   Y888P         888 d888b 888 888 88888b.  .d8888b  
   d888b         888d88888b888 888 888 "88b 88K      
  d88888b        88888P Y88888 888 888  888 "Y8888b. 
 d88P Y88b       8888P   Y8888 888 888  888      X88 
d88P   Y88b      888P     Y888 888 888  888  88888P' 
'''
o_wins = r'''
 .d88888b.       888       888 d8b                   
d88P" "Y88b      888   o   888 Y8P                   
888     888      888  d8b  888                       
888     888      888 d888b 888 888 88888b.  .d8888b  
888     888      888d88888b888 888 888 "88b 88K      
888     888      88888P Y88888 888 888  888 "Y8888b. 
Y88b. .d88P      8888P   Y8888 888 888  888      X88 
 "Y88888P"       888P     Y888 888 888  888  88888P' 
'''
O_Points = [0,0,0,0,0,0,0,0,0]
X_Points = [0,0,0,0,0,0,0,0,0]
box_show_values = [1,2,3,4,5,6,7,8,9]
available_options = [1,2,3,4,5,6,7,8,9]
is_game_on = True
def print_board():
    print(f" {box_show_values[0]} | {box_show_values[1]} | {box_show_values[2]}")
    print(f'___|___|___')
    print(f" {box_show_values[3]} | {box_show_values[4]} | {box_show_values[5]}")
    print(f'___|___|___')
    print(f" {box_show_values[6]} | {box_show_values[7]} | {box_show_values[8]}")

wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def check_wins(player_points):
    for win in wins:
        # Calculate the sum for the current winning combination
        sum_points = player_points[win[0]] + player_points[win[1]] + player_points[win[2]]
        # print(f"Checking win combination {win}: Sum = {sum_points}")
        if sum_points == 3:  # Check if the sum equals 3
            return True
    return False  # Return False if no winning combination is found

print(game_intro)

while len(available_options):
    
    print_board()
    o_choosed = int(input(f"{o_turns}\nChoose Your Box :"))
    available_options.remove(o_choosed)
    O_index = o_choosed-1
    box_show_values[O_index] = 'O'
    O_Points[O_index] = 1
    if check_wins(O_Points) :
        os.system('cls')
        print_board()
        print(o_wins)
        break
    os.system('cls')

    print("Computer Turns")
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
    print_board()
    X_choosed = random.choice(available_options)
    available_options.remove(X_choosed)
    X_index = X_choosed-1
    box_show_values[X_index] = 'X'
    X_Points[X_index] = 1
    if check_wins(X_Points) :
        os.system('cls')
        print_board()
        print(x_wins)
        break
    os.system('cls')

else:
    print("Match Draw")

