import numpy as np
import constants_fleet as ct
import random

class Board:

    def __init__(self, player):

        self.player = player
        self.board_dim = ct.BOARD_SIZE
        self.ships = ct.SHIP_SIZES_TO_DEPLOY
        self.my_board = np.full([ct.BOARD_SIZE, ct.BOARD_SIZE], ' ')
        self.enemys_track_board = np.full([ct.BOARD_SIZE, ct.BOARD_SIZE], ' ')

    def ship_fits_within_board(self, size, row, column, orientation):

        # This is to verify whether the ship falls within the board based on
        # its size, orientation, and the random board coordinates

        fits = False

        if orientation == 'N':
            if (row - size + 1) >= 0:
                fits = True

        elif orientation == 'S':
            if (row + size - 1) <= self.board_dim - 1:
                fits = True

        elif orientation == 'E':
            if (column + size - 1) <= self.board_dim - 1:
                fits = True

        elif orientation == 'O':
            if (column - size + 1) >= 0:
                fits = True

        else:
            fits = False

        return fits

    def ship_has_space(self, size, row, column, orientation):

        # This is to determine whether the ship has space to be deployed as randomly
        # selected: no ship already in any of the positions to be used for this ship
        # or in the water surrounding it

        start_row = 0
        end_row = 0
        start_column = 0
        end_column = 0

        if orientation == 'N':
            if (row - size + 1) > 0:
                start_row = row - size
            else:
                start_row = 0

            if row < 9:
                end_row = row + 2
            else:
                end_row = row + 1

            if column > 0:
                start_column = column - 1
            else:
                start_column = 0

            if column < 9:
                end_column = column + 2
            else:
                end_column = column + 1

        elif orientation == 'S':
            if row > 0:
                start_row = row - 1
            else:
                start_row = 0

            if (row + size - 1) < 9:
                end_row = row + size + 1
            else:
                end_row = row + size

            if column > 0:
                start_column = column - 1
            else:
                start_column = 0

            if column < 9:
                end_column = column + 2
            else:
                end_column = column + 1

        elif orientation == 'E':
            if row > 0:
                start_row = row - 1
            else:
                start_row = 0

            if row < 9:
                end_row = row + 2
            else:
                end_row = row + 1

            if column > 0:
                start_column = column - 1
            else:
                start_column = 0

            if (column + size - 1) < 9:
                end_column = column + size + 1
            else:
                end_column = column + size

        elif orientation == 'O':
            if row > 0:
                start_row = row - 1
            else:
                start_row = 0

            if row < 9:
                end_row = row + 2
            else:
                end_row = row + 1

            if (column - size + 1) > 0:
                start_column = column - size
            else:
                start_column = column - size + 1

            if column < 9:
                end_column = column + 2
            else:
                end_column = column + 1

        space_required = self.my_board[start_row:end_row + 1, start_column:end_column]
        has_space = 'O' not in space_required

        return has_space

    def deploy_ship(self, size, row, column, orientation):

        # This is to deploy the ship in the location randomly selected

        if orientation == 'N':
            self.my_board[row - size + 1:row + 1, column] = 'O'

        elif orientation == 'S':
            self.my_board[row:row + size, column] = 'O'

        elif orientation == 'E':
            self.my_board[row, column: column + size] = 'O'

        elif orientation == 'O':
            self.my_board[row, column - size + 1: column + 1] = 'O'

    def deploy_fleet(self):

        # This is to deploy the fleet of ships

        for i in self.ships:
            while True:
                orientation = random.choices('NSEO')
                rand_row = random.randint(0, self.board_dim - 1)
                rand_col = random.randint(0, self.board_dim - 1)
                if (
                        self.ship_fits_within_board(i, rand_row, rand_col, orientation[0])
                        and self.ship_has_space(i, rand_row, rand_col, orientation[0])
                ):
                    self.deploy_ship(i, rand_row, rand_col, orientation[0])
                    break
