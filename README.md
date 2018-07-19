# tic-tac-toe_python_program
# I am applying some coding stuff check tictactoe.py for simplicity
a tic tac toe in python

# tic tac toe game tutorial:
- please follow version `tictactoev2.py`
- Introducing the player for 2 players
*Tic-tac-toe* (also known as *noughts* and *crosses* or *Xs* and *Os*) is a paper-and-pencil game for two players, X
and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a
horizontal, vertical, or diagonal row wins the game.

## steps we are going to take
- introduction: what it is tic-tac-toe game
1. lets begin by designing the board
- we need to create a 3 by 3 board:
- we assign each position to a number
our board will be a list then we reformat it into a 3 by 3 board.
- lets do it!
2. let create a board as a list:
`board = [n, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
3. let format it for display in 3 by 3 board
- just a bit of salt grain creativity;
```
def display_board(board):
    print('xxxxxxxxxxx')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('xxxxxxxxxxx')

```
- you can test the display using (optional)
- its always to taste the waters before .... drinking??? :smile:
`test_display = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']`
`display_board(test_display)`
4. lets write a function that ask the user if she/he want to be'X' or "O"
- consider use a <code>while loop<\code>
```
def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
```
5. Write a function that takes in a board and checks to see if someone has won.
```
def win_check(board,mark):

    return (
    (board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

```
6. Write a function that uses the random module to randomly decide which player goes first.
You may want to lookup random.randint() Return a string of which player went first.
```
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
```
7.Write a function that returns a boolean indicating whether a space on the board is freely available.
```
def space_check(board, position):

    return board[position] == ' '

```
8.  Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
```
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

```
9.  Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 8 to
 check if its a free position. If it is, then return the position for later use.
 ```
 def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position

 ```
 10. replay function
 ```
 def replay():

    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
 ```

# Finally lets combine stuff to create the running game:
- lets get some logic first
1. we need a while loop to keep the game running
- inside the while loop
-- actual game play
-- set everything up (BOARD, WHOS FIRST, CHOOSE MARKERS X, 0)
- game play
- player one turn
- player two turn

2. break out of the while loop on the <code>replay()</code> function
