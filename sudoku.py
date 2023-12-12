
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def solve_sudoku(board):

        row, col = find_empty_cell()

        if row is None:
            return True

        # Try each number from 1 to 9 in the empty cell
        for num in range(1, 10):
            # Check if the number is valid in the current position
            if is_valid(num, row, col):
                # Place the number in the current position
                board[row][col] = num

                # Recursively solve the puzzle
                if solve_sudoku(board):
                    return True

                # If the puzzle cannot be solved with the current number, backtrack
                board[row][col] = 0

        # If no number from 1 to 9 is valid, the puzzle is unsolvable
        return False

def find_empty_cell():

        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return row, col

        # If no empty cell is found, return None
        return None, None

def is_valid( num, row, col):

        # Check if the number already exists in the same row
        for i in range(9):
            if board[row][i] == num:
                return False

        # Check if the number already exists in the same column
        for i in range(9):
            if board[i][col] == num:
                return False

        # Check if the number already exists in the same 3x3 box
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False

        # If the number is valid in all checks, return True
        return True
def print_board():
        """
        Prints the current state of the Sudoku board.
        """

        for row in board:
            print(row)


if solve_sudoku(board):
    print("Sudoku puzzle solved:")
    print_board()
else:
    print("No solution found for the Sudoku puzzle.")
