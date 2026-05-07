class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = len(board)
        for i in range(n):
            if not check_line(board[i]):
                return False
            
            column = []
            for j in range(n):
                if board[j][i] == ".":
                    continue
                column.append(board[j][i])
                
            if not check_line(column):
                return False
            
        return check_square(board)
    

def check_line(line):
    nums = []
    for value in line:
        if value == ".":
            continue
        nums.append(value)
    return True if len(nums) == len(set(nums)) else False


def check_square(board: list[list[str]]) -> bool:
    # create the 9 bucket squares for 3x3 squares numbers
    squares = [[] for _ in range(9)]

    for row_index, row in enumerate(board):
        # diving by 3 a 9 grid makes sure each row belongs to the associated square (0//3=0, 1//3=0, 4//3=1, etc...)
        row_group = row_index // 3

        # navigate through the row to get all columns
        for col_index, cell_value in enumerate(row):
            # immediate check to avoid wasting time
            if cell_value == ".":
                continue

            col_group = col_index // 3
            # 012, 345, 678 are the indices for each line. row_group*3 aligns with the first square in each line (0,3,6). col_group does the same with columns.
            square_index = row_group * 3 + col_group
            squares[square_index].append(cell_value)

    # duplicate check
    for square in squares:
        if len(square) != len(set(square)):
            return False

    return True