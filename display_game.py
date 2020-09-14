from check_winner import game_conditions

game = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

player1_turn = True
player2_turn = False


def place_in_position(row, col):
    global player1_turn
    global player2_turn
    try:
        if player1_turn and not player2_turn:
            if game[row-1][col-1] == ' ':
                game[row-1][col-1] = 'X'
                player1_turn = False
                player2_turn = True
            else:
                print("This spot has already been taken")
        elif player2_turn and not player1_turn:
            if game[row-1][col-1] == ' ':
                game[row - 1][col - 1] = 'O'
                player2_turn = False
                player1_turn = True
            else:
                print("This spot has already been taken")
    except IndexError:
        print("There are only 3 rows and 3 columns, please pick numbers between 1-3")


def display(c, s=3):         # to display matrix on square board
    h = ' ---'
    for i in range(0, s):
        print(h*s)
        v = []
        for j in range(0, s):
            v.append('| ' + str(c[i][j]) + ' ')
        for m in v:
            print(m, end='')
        print('|')
    print(h*s)


def main_game():
    display(game)
    while True:
        while player1_turn is True and player2_turn is False:
            try:
                player1 = input("Please pick where you'd like to place your X (row,col): ")
                player1_list = player1.split(",") # separate into two pieces in a list at the comma
                player1_list = list(map(int, player1_list)) # convert strings to int
                player1_list = [abs(x) for x in player1_list]
                place_in_position(player1_list[0], player1_list[1])
                display(game)
                game_conditions(game)
            except (ValueError, IndexError) as error:
                print("\nPlease check your input to make sure that it is in the format of (col,row)\n")
                continue

        while player1_turn is False and player2_turn is True:
            try:
                player2 = input("Please pick where you'd like to place your O (row,col): ")
                player2_list = player2.split(",")
                player2_list = list(map(int, player2_list))
                player2_list = [abs(x) for x in player2_list]
                place_in_position(player2_list[0], player2_list[1])
                display(game)
                game_conditions(game)
            except (ValueError, IndexError) as error:
                print("\nPlease check your input to make sure that it is in the format of (col,row)\n")
                continue


if __name__ == "__main__":
    main_game()

