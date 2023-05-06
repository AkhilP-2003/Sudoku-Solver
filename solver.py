from typing import Union

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def solve_board(board: list[list[int]]) -> bool:
    """
    Solves the sudoku board via backtracking
    """

    empty = empty_square(board)

    # Check if 
    if not empty:
        return True
    
    else:
        (row, col) = empty
        num = 1

        while num < 10:
            
            # Check if adding these values into the board is a valid solution
            coordinates = (row, col)
            if is_valid_board(board, num, coordinates):

                # Since it's valid, add into board
                board[row][col] = num

                # Recursively finish the sol'n by calling solve on the 'new' board containing the
                # 'new' value 
                if solve_board(board):
                    return True
                
                # Reset the value to an empty square to try again: backtrack
                board[row][col] = 0
            
            num += 1

    # Since no sol'n could be found, return false
    return False


def empty_square(board: list[list[int]]) -> Union[tuple[int, int], None]:
    """Finds an empty square in the sudoku board. Returns None if there are
    no blank squares.

    Precondition: 0 is an empty square in the board

    """
    not_empty = None

    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if col == 0:
                return (row_index, col_index)
    return not_empty


def is_valid_board(board: list[list[int]], value: int, position: tuple[int, int]) -> bool:
    """
    Checks if board is valid

    Precondition: position is in the form of (row, col)
    """
    # Check if each row is valid
    # for row in board:
    #     if is_unique(row):
    #         validitiy = True
    valid = True

    # Check if each row is valid
    for elm in range(len(board)):
        given_row = position[0]
        given_col = position[1]

        if board[given_row][elm] == value and given_col != elm:
            return not valid
    
    # Check if each col is valid
    for row in range(len(board)):
        given_row = position[0]
        given_col = position[1]

        if board[row][given_col] == value and given_row != given_col:
            return not valid
    
    # Check if each sub-grid is valid
    top_left_row = position[0] - (position[0] % 3)
    top_left_col = position[1] - (position[1] % 3)

    for grid in range(len(board) - 6):
        for i in range(len(board) - 6):
            if board[top_left_row + grid][top_left_col + i] == value:
                return not valid
    
    # Otherwise return that it's valid
    return valid

# def is_unique(board: list[list[int]]) -> bool:
#     """
#     Helper function that checks if each row is unique 
#     """
#     seen_values = []
#     unique = True

#     for row in board:
#         for element in row:
#             if element in seen_values:
#                 return not unique
#             else:
#                 seen_values.append(element)
#         seen_values = [] # reset seen_values for next row

#     return unique

            
def display_sudoku_board(board: list[list[int]]):
    """Function takes in a list of integers and converts it 
    into a board using "-" as seperaters """
    
    for square in range(len(board)):
        
        # For every three rows, print a seperator
        if square % 3 == 0 and square != 0:
            print("-------------")

        len_row = len(board[0])

        # Check if 
        for row in range(len_row):
            if row % 3 == 0:
                print(" | ", end = "")

            if row == 8:
                print(board[square][row])
            
            else:
                print(str(board[square][row]) + " ", end = "")

print(display_sudoku_board(board))

solve_board(board)
print("___________________________________________________________________")
print(display_sudoku_board(board))