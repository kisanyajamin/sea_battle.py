import random

def create_board(size):
    board = []
    for i in range(size):
        board.append(["O"] * size)
    return board

def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row(board):
    return random.randint(0, len(board) - 1)

def random_col(board):
    return random.randint(0, len(board[0]) - 1)

def main():
    print("Let's play Battleship!")
    board_size = int(input("Enter the size of the board: "))
    board = create_board(board_size)
    print_board(board)
    ship_row = random_row(board)
    ship_col = random_col(board)

    for turn in range(4):
        print("Turn", turn+1)
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))

        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sank my battleship!")
            break
        else:
            if (guess_row < 0 or guess_row > board_size-1) or (guess_col < 0 or guess_col > board_size-1):
                print("Oops, that's not even in the ocean.")
            elif(board[guess_row][guess_col] == "X"):
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
            if (turn == 3):
                print("Game Over")
        print_board(board)

if __name__ == "__main__":
    main()
