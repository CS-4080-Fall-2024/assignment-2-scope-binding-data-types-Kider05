sudoku_board = [
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

def print_board(board):
    for row in board:
            print(" ".join(str(num) for num in row))


def solve_sudoku(board):
    #double nested loop to check each individual cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0: #if cell is 0/empty, try placing 1-10 and test with placeable()
                for num in range(1, 10):
                    if placeable(board, row, col, num):
                        board[row][col] = num #if placeable, set cell to num and check if board is solved
                        if solve_sudoku(board): #recalls solve_sudoku and reruns the double nested loop
                            #if all cells are filled then it will return True and exit out which will return true again
                            return True
                        board[row][col] = 0 #resets cell to 0 to try next number in 1-10
                return False
    return True


def placeable(board, row, col, num):
    if num in board[row]: #if num is in the current row, it can't be placeable so return False
        return False

    for r in range(9): #look through each row in the current column to check for num, if its there, return False
        if board[r][col] == num:
            return False

    start_row = (row // 3) * 3 #split the board into 3x3 squares, (row // 3) to find which 3x3 num is in, left middle right
    start_col = (col // 3) * 3 #then multiply (row // 3) by 3 to get the index of the top-left cell in num's 3x3 grid
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            #double nested loop through the 3x3 grid to check if num is inside, False if it is inside
            if board[r][c] == num:
                return False
    return True

if solve_sudoku(sudoku_board):
    print("Solved Sudoku board:")
    print_board(sudoku_board)
else:
    print_board(sudoku_board)
    print("No solution")