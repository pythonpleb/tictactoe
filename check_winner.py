
'''
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
'''

winner = False
empty_tiles = True


def check_rows(game):
    global winner
    row = 0
    while row != 3:
        for x in game[row]:
            if 'X' in game[row][1:] == game[row][:-1]:
                print("Player 1 wins the game")
                winner = True
                break
            elif 'O' in game[row][1:] == game[row][:-1]:
                print("Player 2 wins the game")
                winner = True
                break
        row += 1


def check_columns(game):
    global winner
    col = 0
    while col != 3:
        if 'X' == game[0][col] == game[1][col] == game[2][col]:
            print("Player 1 wins the game")
            winner = True
            break
        elif 'O' == game[0][col] == game[1][col] == game[2][col]:
            print("Player 2 wins the game")
            winner = True
            break
        col += 1


def check_diagonals(game):
    global winner
    if 'X' == game[0][0] == game[1][1] == game[2][2]:
        print("Player 1 wins the game")
        winner = True
    elif 'O' == game[0][0] == game[1][1] == game[2][2]:
        print("Player 2 wins the game")
        winner = True
    elif 'X' == game[0][2] == game[1][1] == game[2][0]:
        print("Player 1 wins the game")
        winner = True
    elif 'O' == game[0][2] == game[1][1] == game[2][0]:
        print("Player 2 wins the game")
        winner = True


def check_tie(game, string):
    global empty_tiles
    for row in game:
        for element in row:
            if element == string:
                return True


def game_over():
    if winner is True:
        exit()


def game_conditions(game):
    check_rows(game)
    check_columns(game)
    check_diagonals(game)
    if not check_tie(game, ' ') and winner is False:
        print("Tie")
        exit()
    game_over()
