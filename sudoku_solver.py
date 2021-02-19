puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

# sudoku(puzzle)
# # Should return
#  [[5,3,4,6,7,8,9,1,2],
#   [6,7,2,1,9,5,3,4,8],
#   [1,9,8,3,4,2,5,6,7],
#   [8,5,9,7,6,1,4,2,3],
#   [4,2,6,8,5,3,7,9,1],
#   [7,1,3,9,2,4,8,5,6],
#   [9,6,1,5,3,7,2,8,4],
#   [2,8,7,4,1,9,6,3,5],
#   [3,4,5,2,8,6,1,7,9]]

def solver():
    global puzzle
    for y in range(9):
        for x in range(9):
            if puzzle[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        puzzle[y][x] = n
                        solver()
                        # if possible returns false (dead end) will return here
                        puzzle[y][x] = 0
                # if this return is reached, algorithm has tried 1-9 for [y][x],
                # but has backtracked or possible returned False.
                return


def possible(y, x, n):
    # check the row
    for i in range(9):
        if puzzle[y][i] == n:
            return False

    # check the column
    for i in range(9):
        if puzzle[i][x] == n:
            return False

    # check 3x3 square containing [y][x]
    # coords of top left ele in 3x3 square using floor div
    y0 = (y // 3) * 3
    x0 = (x // 3) * 3
    for i in range(3):
        for j in range(3):
            if puzzle[y0 + i][x0 + j] == n:
                return False
    # puzzle[y][x] could be n as n is not in row, col or square.
    return True

solver()
print(puzzle)
