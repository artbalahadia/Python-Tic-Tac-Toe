# Tic Tac Toe Program in Python
# The game follows a basic Tic Tac Toe game where X and O is used to fill in the board
# Player must follow rules: (1) Avoid out of bounds (2) Avoid filled spaces. Otherwise turn is lost

game_board = [' '] * 10

# Board structure
def display_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])

display_board(game_board)

# Check which player uses 'X' and 'O'
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Please choose marker: (X or O)')

    player1 = marker

    if player1 == 'O':
        player2 = 'X'
    else:
        player2 = 'O'
    print('Player 1 = ' + player1 + ' || Player 2 = ' + player2)
    return player1, player2

# Inputs the move on the board position. Rules above follow.
def place_marker(board, player, position):
    if(1 < position > 9):
        print('Position out of bounds. Please choose from 1 to 9 only. You lost your turn.')
        pass
    elif(board[position] == ' '):
        board[position] = player
        display_board(game_board)
    else:
        print('Invalid input. Place is filled. You lost your turn.')
        pass
    return board

# Winner validations
def winner(board):
    player1 = 'X'
    player2 = 'O'
    if(board[1] == board[2] == board[3] == player1 or
            board[4] == board[5] == board[6] == player1 or
            board[7] == board[8] == board[9] == player1 or
            board[1] == board[4] == board[7] == player1 or
            board[2] == board[5] == board[8] == player1 or
            board[3] == board[6] == board[9] == player1 or
            board[1] == board[5] == board[9] == player1 or
            board[3] == board[5] == board[7] == player1):
        print('Player 1 Wins!')
        return True
    elif(board[1] == board[2] == board[3] == player2 or
            board[4] == board[5] == board[6] == player2 or
            board[7] == board[8] == board[9] == player2 or
            board[1] == board[4] == board[7] == player2 or
            board[2] == board[5] == board[8] == player2 or
            board[3] == board[6] == board[9] == player2 or
            board[1] == board[5] == board[9] == player2 or
            board[3] == board[5] == board[7] == player2):
        print('Player 2 Wins!')
        return True
    else:
        return False

# Interchanges Player 1 and 2
def player_turn(current):
    while(current != 1 and current != 2):
        current = int(input('Who goes first? (Player 1 or 2)'))
    return current

# Initialize Game
def start_game():
    player1, player2 = player_input()
    current =  int(player_turn(' '))

    while(not winner(game_board)):
        if(current == 1):
            position = int(input('Please enter position: (1 to 9)'))
            place_marker(game_board,player1,position)
            current = 2
        elif(current == 2):
            position = int(input('Please enter position: (1 to 9)'))
            place_marker(game_board, player2, position)
            current = 1

#print(game_board)
start_game()