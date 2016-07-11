

"""Connect4 Module -- Implements a Connect 4 Game with two players.

This module enables two players to play in a game of Connect 4,
with player 1 being "x" and player 2 being "y." Each player
takes turns selecting a column to drop their tile, and the first
to connect 4 in a row, in a column, or in a diagonal, wins.

    Run the program from the command line:
        $ python Connect4.py

Attribute(s):
    None.
"""


def main():
    """main function, creates the game engine and window
    to play the game.

   This function enables creation of the board, printing of
   of the board, and enabling player turns. It also asks
   if the players want to play another game.

   Arguments:
       None.

    Returns:
        None.
    """
    program_over = False
    while not program_over:
        game_over = False
        L = create_board()

        while not game_over:
            print_board(L)
            make_move(L, "x")
            a = check_win(L)
            if a:
                print("Winner!")
                print_board(L)
                game_over = True
                print("Winner is:", "x")
            else:
                game_over = False
            if not game_over:
                print_board(L)
                make_move(L, "y")
                a = check_win(L)
                if a:
                    print("Winner!")
                    print_board(L)
                    game_over = True
                    print("Winner is:", "y")
                else:
                    game_over = False
            else:
                print_board(L)

        if int(input("1. Play Again \n2. Exit\nChoice: ")) == 2:
            program_over = True
        else:
            program_over = False


def print_board(L):
    """print_board function, takes a 2D list and prints into Connect 4 layout.

    This function prints a 2D list to represent the board for Connect 4.
    It also prints the column values to show where each tile
    will get placed depending on the column chosen.

    Arguments:
        L (list): A 2D list of strings.
            This parameter is a list of lists of string representing game
            pieces, "x" for player 1, and "y" for player 2, with "O"
            meaning an open slot.
    Returns:
        None.
    """
    print("\tColumns")
    print("0  1  2  3  4  5  6")
    print("===================")
    for row in L:
        for val in row:
            print(val, end='  ')
        print()
    print("===================")

def check_win(L):
    """check_win function, takes a list of lists of strings and
    checks for a win.

    This function checks for a win from any player.
    It goes through the list by row and column, and
    checks if there are 4 tiles of the same kind
    in any direction: vertically, horizontally,
    or diagonally.

    Arguments:
        L (list): A list of lists of strings.
            This parameter is a list of the rows
            of the game board.
    Returns:
        bool: Returns true if a player has won: false otherwise.
    """
    for i in range(6):
        for j in range(7):
            if L[i][j] == 'x' and i < 3:
                if L[i+1][j] == 'x':
                    if L[i+2][j] == 'x':
                        if L[i+3][j] == 'x':
                            return True
    for i in range(6):
        for j in range(7):
            if L[i][j] == 'x' and j < 4:
                if L[i][j+1] == 'x':
                    if L[i][j+2] == 'x':
                        if L[i][j+3] == 'x':
                            return True
    for i in range(6):
        for j in range(7):
            if L[i][j] == 'x' and j < 4 and i < 3:
                if L[i+1][j+1] == 'x':
                    if L[i+2][j+2] == 'x':
                        if L[i+3][j+3] == 'x':
                            return True
    for i in range(6):
        for j in range(7):
            if L[i][j] == 'x' and i < 3:
                if L[i+1][j-1] == 'x':
                    if L[i+2][j-2] == 'x':
                        if L[i+3][j-3] == 'x':
                            return True

    for i in range(6):
        for j in range(7):
            if L[i][j] == 'y' and i < 3:
                if L[i+1][j] == 'y':
                    if L[i+2][j] == 'y':
                        if L[i+3][j] == 'y':
                            return True
    for i in range(6):
        for j in range(7):
            if L[i][j] == 'y' and j < 4:
                if L[i][j+1] == 'y':
                    if L[i][j+2] == 'y':
                        if L[i][j+3] == 'y':
                            return True
    for i in range(6):
        for j in range(7):
            if L[i][j] == 'y' and j < 4 and i < 3:
                if L[i+1][j+1] == 'y':
                    if L[i+2][j+2] == 'y':
                        if L[i+3][j+3] == 'y':
                            return True
    for i in range(6):
        for j in range(7):
            if L[i][j] == 'y' and i < 3:
                if L[i+1][j-1] == 'y':
                    if L[i+2][j-2] == 'y':
                        if L[i+3][j-3] == 'y':
                            return True
    return False


def make_move(L, x):
    """make_move function, makes a move dependent on the indicated column.

    This function take the game board as a list of lists of strings
    and a user-chosen column index to place their tile.

    Arguments:
        L (list): A list of lists of strings.
            This parameter is a list of the rows of the board.
        x (Int): A column index.
            This parameter is the chosen column index by the
            user.
    Returns:
        None.
    """
    a = int(input("Enter a column: "))
    if a > 6 or a < 0:
        print("Out of bounds. Try again")
        make_move(L, x)
    else:
        if L[5][a] != 'O':
            if L[4][a] != 'O':
                if L[3][a] != 'O':
                    if L[2][a] != 'O':
                        if L[1][a] != 'O':
                            if L[0][a] != 'O':
                                print("Column not available. Try again.")
                                make_move(L, x)
                            else:
                                L[0][a] = x
                        else:
                            L[1][a] = x
                    else:
                        L[2][a] = x
                else:
                    L[3][a] = x
            else:
                L[4][a] = x
        else:
            L[5][a] = x


def create_board():
    """create_board function, creates the game board at the
    start of every game.

    This function creates a list of lists of "O" strings,
    indicating empty tiles on the board.

    Arguments:
        None.
    Returns:
        list: Returns a list of lists of strings.
    """
    L = [["O", "O", "O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O", "O", "O"]]
    return L

if __name__ == '__main__':
    main()
