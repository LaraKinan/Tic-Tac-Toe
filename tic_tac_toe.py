players = 'XO'
board = [' ']*9

win_states = [(1,2,3),(4,5,6),(7,8,9), # Horizontal
              (1,4,7), (2,5,8), (3,6,9), # Vertical
              (1,5,9),(3,5,7)] # Diagonal

def print_board():
    print("-------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(board[i*3+j] if board[i*3+j] != ' ' else (i*3+j+1), end="|")
        print("\n-------")

def have_winner():
    for (a,b,c) in win_states:
        if board[a - 1] == board[b - 1] and board[b - 1] == board[c - 1] and not board[a - 1] == ' ':
            return board[a - 1]
    return ' '

def game_still_on():
    if any(board[i] == ' ' for i in range(9)):
        return True
    return False

while True:
    print_board()
    winner = have_winner()
    if winner == 'X':
        print("X won the game! Woho!")
        break
    if winner == 'O':
        print("O won the game! Woho!")
        break
    if not game_still_on() and winner == ' ':
        print("It's a Tie")
        break
    move = input("Choose index for move:")
    if not move.isdigit() or int(move) > 9 or int(move) < 1 or not board[int(move) - 1] == ' ':
        print("Illegal move, try again")
        continue
    board[int(move) - 1] = players[0]
    players = players[::-1]