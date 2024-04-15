"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name:       Anas Monjib
Email:      amonjib@gmail.com
Student Id: H291936

"""
# define the initial state of the board
board = [
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["r", "n", "b", "q", "k", "b", "n", "r"]
]


# define a function to print the board
def print_board():
    for row in board:
        print(" ".join(row))


# define a function to move a piece
def move_piece(start, end, player):
    # get the piece at the starting position
    piece = board[start[0]][start[1]]
    # check if the starting position is empty
    if piece == " ":
        print("There is no piece at the starting position.")
        return
    # check if the piece belongs to the current player
    if player == "white" and piece.islower():
        print("You cannot move a black piece.")
        return
    if player == "black" and piece.isupper():
        print("You cannot move a white piece.")
        return
    # check if the ending position is occupied by a friendly piece
    if piece.islower() and board[end[0]][end[1]].islower():
        print("You cannot move to a position occupied by a friendly piece.")
        return
    if piece.isupper() and board[end[0]][end[1]].isupper():
        print("You cannot move to a position occupied by a friendly piece.")
        return
    # move the piece to the ending position
    board[end[0]][end[1]] = piece
    board[start[0]][start[1]] = " "


# main game loop
while True:
    # print the current state of the board
    print_board()

    # prompt player 1 to make a move
    start = tuple(int(x.strip()) for x in input(
        "Player 1, enter the starting position (row, col): ").split(","))
    end = tuple(int(x.strip()) for x in input(
        "Player 1, enter the ending position (row, col): ").split(","))
    move_piece(start, end, "white")

    # check if player 1 has won
    if board[end[0]][end[1]] == "k":
        print("Player 1 wins!")
        break

    # prompt player 2 to make a move
    start = tuple(int(x.strip()) for x in input(
        "Player 2, enter the starting position (row, col): ").split(","))
    end = tuple(int(x.strip()) for x in input("Player 2, enter the ending position (row, col): ").split(","))
    move_piece(start, end, "black")

    # check if player 2 has won
    if board[end[0]][end[1]] == "K":
        print("Player 2 wins!")
        break