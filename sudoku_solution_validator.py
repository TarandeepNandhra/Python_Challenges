# Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board,
# and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's,
# which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.
# The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

# Example input

# board = [
# [1, 3, 2, 5, 7, 9, 4, 6, 8],
# [4, 9, 8, 2, 6, 1, 3, 7, 5],
# [7, 5, 6, 3, 8, 4, 2, 1, 9],
# [6, 4, 3, 1, 5, 8, 7, 9, 2],
# [5, 2, 1, 7, 9, 3, 8, 4, 6],
# [9, 8, 7, 4, 2, 6, 5, 3, 1],
# [2, 1, 4, 9, 3, 5, 6, 8, 7],
# [3, 6, 5, 8, 1, 7, 9, 2, 4],
# [8, 7, 9, 6, 4, 2, 1, 3, 5]
# ]

# > False

def check_row_of_squares(arr, start):
  sum = 0
  for j in range(9):
    for i in range(start, start + 3):
      sum += board[i][j]
      if j % 3 == 2 and i == start + 2:
        if sum != 45:
          return False
        else:
          sum = 0
  return True

def check_rows(board):
    for i in range(1, 10):
        for j in range(9):
            if i not in board[j]:
                return False

    return True

def check_columns(board):
    1_to_9 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        numbers = []

        for j in range(9):
            numbers.push(board[i][j])

        if numbers != 1_to_9:
            return False

    return True

def check_board():
  return check_row_of_squares(board, 0) and check_row_of_squares(board, 3) and check_row_of_squares(board, 6) and check_rows(board) and check_columns(board)

# check_board()
