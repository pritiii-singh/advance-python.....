"""
Project 129: Classic Tic-Tac-Toe Game
Concepts: 2D grid/list modeling, game-loop states, win-condition evaluation.
"""
def print_board(board):
    print("\n")
    for row in range(3):
        print(f" {board[row*3]} | {board[row*3+1]} | {board[row*3+2]} ")
        if row < 2:
            print("---|---|---")
    print("\n")

def check_winner(board, player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8), # rows
        (0,3,6), (1,4,7), (2,5,8), # cols
        (0,4,8), (2,4,6)           # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in wins)

def main():
    board = [str(i) for i in range(1, 10)]
    current_player = "X"
    moves = 0

    print("=== TIC TAC TOE ===")
    print("Choose numbers 1-9 to place your mark:")

    while moves < 9:
        print_board(board)
        move_str = input(f"Player {current_player}'s turn (1-9): ").strip()
        if not (move_str.isdigit() and 1 <= int(move_str) <= 9):
            print("Invalid input. Pick 1 to 9.")
            continue
        idx = int(move_str) - 1
        if board[idx] in ["X", "O"]:
            print("Cell already occupied. Choose another!")
            continue

        board[idx] = current_player
        moves += 1

        if check_winner(board, current_player):
            print_board(board)
            print(f"[WINNER] Player {current_player} WINS!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("[DRAW] Game ended in a DRAW!")

if __name__ == "__main__":
    main()
