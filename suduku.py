def is_valid(board, row, col, num):
    # 检查行是否有重复
    for x in range(9):
        if board[row][x] == num:
            return False

    # 检查列是否有重复
    for x in range(9):
        if board[x][col] == num:
            return False

    # 检查3x3小宫格是否有重复
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(board):
    empty = None
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                empty = (i, j)
                break
        if empty is not None:
            break

    if empty is None:
        return True  # 找不到空位，数独已解完

    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # 回溯
    
    return False

def print_board(board):
    for row in board:
        print(' '.join(str(num) for num in row))

# # 示例数独问题
# board = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]

# if solve_sudoku(board):
#     print("Solved Sudoku:")
#     print_board(board)
# else:
#     print("No solution exists")