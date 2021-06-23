import sys

print("""



""")


print("Tic Tac Toe by Roberto")

board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

current_player = "X"
# ..........Functions..........

# function for X to play


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


def player_turn():
    global current_player
    while True:
        try:
            play = int(
                input(f"{current_player}'s turn.....Select a spot to play from 1 to 9: "))
            if board[play] == " ":
                board[play] = current_player
                break

            else:
                print("Please select a correct spot: ")
        except:
            print("Please select a valid spot: ")





# function to check if it is a tie
def checking_if_it_is_tie():
    if " " in board:
        pass
    else:
        show_board()
        print("It is a Tie...")
        input("Press enter to Exit")
        sys.exit()


# function to check if any player won
def check_if_player_won(board, player):
    if (board[1] == player and board[2] == player and board[3] == player) or\
        (board[4] == player and board[5] == player and board[6] == player) or\
        (board[7] == player and board[8] == player and board[9] == player) or\
        (board[1] == player and board[4] == player and board[7] == player) or\
        (board[2] == player and board[5] == player and board[8] == player) or\
        (board[3] == player and board[6] == player and board[9] == player) or\
        (board[3] == player and board[5] == player and board[7] == player) or\
            (board[1] == player and board[5] == player and board[9] == player):
        show_board()
        print(f"{player} Won...Congratulations!!")
        input("Press enter to Exit")
        sys.exit()


# function to print the board
def show_board():
    print("\n")
    print(board[1] + " | " + board[2] + " | " + board[3] + " | "      "1-2-3")
    print(board[4] + " | " + board[5] + " | " + board[6] + " | "      "4-5-6")
    print(board[7] + " | " + board[8] + " | " + board[9] + " | "      "7-8-9")
    print("\n")


# ..........FUNCTIONALITY..........
while True:
    # printing the board
    show_board()

    # Player x turn
    player_turn()

    # checking if X won
    check_if_player_won(board, current_player)

    flip_player()
