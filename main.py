import random

# Initialize the game board
def initialize_board():
    return [' ' for _ in range(9)]

# Print the game board
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('|'.join(row))
        print('-' * 5)

# Check if a player has won
def check_winner(board, player):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]]
    ]
    return [player, player, player] in win_conditions

# Check if the game is a tie
def check_tie(board):
    return ' ' not in board

# Get the player's move
def get_player_move(board):
    move = int(input("Enter your move (1-9): ")) - 1
    while board[move] != ' ':
        move = int(input("Invalid move. Enter your move (1-9): ")) - 1
    return move

# Get the computer's move
def get_computer_move(board):
    available_moves = [i for i, spot in enumerate(board) if spot == ' ']
    return random.choice(available_moves)

# Main game loop
def play_game():
    board = initialize_board()
    current_player = 'X' # Player starts first

    while True:
        print_board(board)
        
        if current_player == 'X':
            move = get_player_move(board)
        else:
            move = get_computer_move(board)
        
        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

# Call the main game loop
if __name__ == "__main__":
    play_game()
