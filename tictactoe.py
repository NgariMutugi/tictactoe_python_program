# a tic tac toe game in python
import random
from typing import Tuple

board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def display_board():
    #  clear_output()  # Remember, this only works in jupyter!
    print('xxxxxxxxxxxxxxxxxx')
    print(' ', board[0], ' | ', board[1], ' | ', board[2])
    print('-----------------')
    print(' ', board[3], ' | ', board[4], ' | ', board[5])
    print('-----------------')
    print(' ', board[6], ' | ', board[7], ' | ', board[8])
    print('xxxxxxxxxxxxxxxxxx')


display_board()


def check_win():
    count =0

    for a in win_combinations:
        if board[a[0]] == board[a[1]] == board[a[2]] == "X":
            print("You won Against the  Computer!!!\n")
            print("Congratulations!\n")
            return True

        if board[a[0]] == board[a[1]] == board[a[2]] == "O":
            print("The Computer Wins!\n")
            print("!\n")
            return True
    for a in range(9):
        if board[a] == "X" or board[a] == "O":
            count += 1
        if count == 9:
            print("The game ends in a Tie\n")
        return True


while True:
    check_win()
    user_inpu = input('Select a spot: ')
    user_inpu = int(user_inpu)

    if board[user_inpu] != 'X' and board[user_inpu] != 'O':
        board[user_inpu] = 'X'
        # display_board()

        finding = True  # to make sure the opponent chooses a spot not chosen and  plays its part
        while finding:
            opponent = random.randint(0, 8)
            # print(random.randint(0, 8))
            if board[opponent] != 'X' and board[opponent] != 'O':
                board[opponent] = 'O'
            finding = False
            display_board()
    else:
        print('This spot is hot already Taken bro!')
        display_board()

