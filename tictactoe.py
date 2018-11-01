
board = [" " for i in range(9)]


def print_table():
    row1 = "| {} | {} | {} |".format(board[0],board[1],board[2])
    row2 = "| {} | {} | {} |".format(board[3],board[4],board[5])
    row3 = "| {} | {} | {} |".format(board[6],board[7],board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2

    print("Your turn player {}".format(number))

    choice =int(input("Enter your move  [1-9]: ").strip())

    if board[choice -1] == " ":
        board[choice-1] = icon
    else:
        print()
        print("That space is not empty!")

def is_victory(icon):
    i = 0
    while i<=8 :
        if board[i] == icon and board[i] == board[i+1] and board[i] == board[i+2]:
            return True
        else:
            i = i+3

        return False


while True:

    print_table()
    player_move("X")
    print_table()
    if is_victory("X"):
        print("X Wins!")
        break
    player_move("O")
    if is_victory("O"):
        print_table()
        print("O is win!")
        break





