import random

# Initialize the board
board = [' '] * 10  # Index 0 is ignored for easier indexing (1-9)

# Function to print the board
def print_board():
    print(f"""
     {board[1]} | {board[2]} | {board[3]}
    ---+---+---
     {board[4]} | {board[5]} | {board[6]}
    ---+---+---
     {board[7]} | {board[8]} | {board[9]}
    """)

# Function to check for a win
def check_win(player):
    win_combinations = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # columns
        (1, 5, 9), (3, 5, 7)              # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_combinations)

# Function to check for a tie
def is_tie():
    return all(space != ' ' for space in board[1:])

# Function for computer move
def computer_move():
    free_fields = [i for i in range(1, 10) if board[i] == ' ']
    return random.choice(free_fields)

# Start game
board[5] = 'X'  # Computer starts at center
print("Welcome to Tic-Tac-Toe!")
print_board()

while True:
    # Player move
    while True:
        try:
            user = int(input("Enter your move (1-9): "))
            if user < 1 or user > 9 or board[user] != ' ':
                print("Invalid move. Try again.")
            else:
                board[user] = 'O'
                break
        except ValueError:
            print("Please enter a valid number.")

    print_board()

    # Check if player wins
    if check_win('O'):
        print("You win!")
        break
    if is_tie():
        print("It's a tie!")
        break

    # Computer move
    comp = computer_move()
    board[comp] = 'X'
    print(f"Computer chose: {comp}")
    print_board()

    # Check if computer wins
    if check_win('X'):
        print("Computer wins!")
        break
    if is_tie():
        print("It's a tie!")
        break
