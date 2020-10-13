# These are the functions to be imported into main_fleet
import random
import constants_fleet as ct

def shoot_to_sink(row, column, enemys_board, my_tracking_board):
    # This function:
    # - Checks whether there is a ship in the coordinates provided (row, column).
    # - Updates the player's tracking board and the enemy's board
    # - Returns a boolean variable: whether a ship has been found and hit

    ship_hit = False

    if enemys_board[row, column] == 'O':
        ship_hit = True
        enemys_board[row, column] = 'X'
        my_tracking_board[row, column] = 'X'
    elif enemys_board[row, column] == ' ':
        ship_hit = False
        enemys_board[row, column] = '-'
        my_tracking_board[row, column] = '-'
    else:
        pass  # This should only occur when shooting twice to the same position. Shot wasted - Do nothing.

    return ship_hit


def find_coord_to_shoot(my_tracking_board):

    # This function returns the coordinates - random - to shoot to sink for Player 2 - the machine

    while True:
        shoot_row = random.randint(0, ct.BOARD_SIZE - 1)
        shoot_column = random.randint(0, ct.BOARD_SIZE - 1)
        if my_tracking_board[shoot_row, shoot_column] == ' ':
            break

    return shoot_row, shoot_column
