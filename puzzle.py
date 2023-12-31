'''
The logic puzzle game board has a square shape with 9×9 cells.
The board contains cells of different colors that are used in
the game and white areas that are not used for the game. 
The validate_board function is used to determine
if the logic puzzle board is ready to start the game.
The cells of the board must be filled in according to the
following rules before the game starts:

1) The colored cells of each row must contain
numbers from 1 to 9 without repetition.

2) The colored cells of each column must contain
digits from 1 to 9 without repetition.

3) Each block of cells of the same color must contain
digits from 1 to 9 without repetition.
'''
def validate_board(board: list) -> bool:
    '''
    The validate_board(board) function returns a Boolean value.
    For example, for a game board, in the doctype, the function
    returns False, since the fifth column contains two digits 1.
    >>> validate_board(["**** ****", "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"\
])
    False
    '''
    def check_for_dups(field: list) -> bool:
        for line in field:
            line_of_nums = line.strip('*')
            line_of_nums = line_of_nums.replace(' ', '')
            if any(line_of_nums.count(x) > 1 for x in line_of_nums):
                return False
            if '0' in line_of_nums:
                return False
        return True

    if not check_for_dups(board):
        return False

    column = []
    list_of_columns = []
    for num_column in range(9):
        for line in board:
            column += [line[num_column]]
        list_of_columns += [''.join(column)]
        column = []

    if not check_for_dups(list_of_columns):
        return False

    board_list =[]
    for line in board:
        board_list += [list(line)]

    angle = []
    colors = []
    line = 4
    for col in range(4, -1, -1):
        for row in range(5):
            angle += board_list[line - row][col]
        for column in range(1, 5):
            angle += board_list[line][col + column]
        colors += [''.join(angle)]
        angle = []
        line += 1

    if not check_for_dups(colors):
        return False
    return True
