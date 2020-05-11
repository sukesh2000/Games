#!/usr/bin/env python
# coding: utf-8

# In[3]:


from IPython.display import clear_output
def display_board(board, e):
    clear_output()
    d = {'1': board[1], '2': board[2], '3': board[3], '4': board[4], '5': board[5], '6': board[6], '7': board[7], '8': board[8], '9': board[9]}
    print('Available moves       Tic - Tac - Toe\n')
    print('   |   |                   |   |')
    print(f' {e[7]} | {e[8]} | {e[9]}               {d["7"]} | {d["8"]} | {d["9"]}')
    print('   |   |                   |   |')
    print('---+---+---             ---+---+---')
    print('   |   |                   |   |')
    print(f' {e[4]} | {e[5]} | {e[6]}               {d["4"]} | {d["5"]} | {d["6"]}')
    print('   |   |                   |   |')
    print('---+---+---             ---+---+---')
    print('   |   |                   |   |')
    print(f' {e[1]} | {e[2]} | {e[3]}               {d["1"]} | {d["2"]} | {d["3"]}')
    print('   |   |                   |   |')


# In[4]:


#Player Input
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O', 'X')


# In[5]:


#Place Marker
def place_marker(board, e, marker, position):
    board[position] = marker
    e[position] = ' '


# In[6]:


#Winner Check
def win_check(board, mark):
    return ((board[7] == mark and board [8] == mark and board [9] == mark) or
    (board[4] == mark and board [5] == mark and board [6] == mark) or
    (board[1] == mark and board [2] == mark and board [3] == mark) or
    (board[7] == mark and board [5] == mark and board [3] == mark) or
    (board[9] == mark and board [5] == mark and board [1] == mark) or
    (board[7] == mark and board [4] == mark and board [1] == mark) or
    (board[8] == mark and board [5] == mark and board [2] == mark) or
    (board[9] == mark and board [6] == mark and board [3] == mark))


# In[7]:


#First Player to play
import random
def choose_first():
    n = random.randint(1, 2)
    if n == 1:
        return 'Player 1', n
    elif n == 2:
        return 'Player 2', n


# In[8]:


#Free space to be checked
def space_check(board, position):
    return board[position] == ' '


# In[9]:


#Full board check
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# In[10]:


def player_choice(board):
    position = 0
    while position not in list(range(1,10)) or not space_check(board, position):
        position = int(input('Choose your next position: (1-9)'))
    return position


# In[11]:


def replay():
    rep = ''
    while not (rep == 'Y' or rep == 'N'):
        rep = input('Do you want to play again? Enter Yes or No: ')[0].upper()
    return rep.startswith('Y')


# In[12]:


#Main
while True:
    print('Welcome to Tic Tac Toe!')
    test_board = [' ']*10
    ava = [f for f in list(range(0, 10))]
    p1, p2 = player_input()
    t = choose_first()
    #print(t[0] + ' will go first.')
    turn = t[1]
    game = input('Do you want to start? (Yes or No)')
    if game.lower()[0] == 'y':
        g = True
    else:
        g = False
    
    while g:
        #Player 1
        if turn == 1:
            display_board(test_board, ava)
            print(f'Player 1: {p1}, Player 2: {p2}')
            print('Player 1 turn')
            position = player_choice(test_board)
            place_marker(test_board, ava, p1, position)
            if win_check(test_board, p1):
                display_board(test_board, ava)
                print('Player 1 has won the game')
                g = False
            else:
                if full_board_check(test_board):
                    display_board(test_board, ava)
                    print('The game is tied.')
                    break
                else:
                    turn = 2
        #Player 2
        elif turn == 2:
            display_board(test_board, ava)
            print(f'Player 1: {p1}, Player 2: {p2}')
            print('Player 2 turn')
            position = player_choice(test_board)
            place_marker(test_board, ava, p2, position)
            if win_check(test_board, p2):
                display_board(test_board, ava)
                print('Player 2 has won the game')
                g = False
            else:
                if full_board_check(test_board):
                    display_board(test_board, ava)
                    print('The game is tied.')
                    break
                else:
                    turn = 1
    if not replay():
        break

