import numpy as np
import constants_fleet as ct
import classess_fleet as cl
import functions_fleet as func

# Player 1 is the human, Player 2 the machine
player_1 = 'P1'
player_2 = 'P2'
board_1 = cl.Board(player_1)
board_2 = cl.Board(player_2)

# Deploy ships to the boards
board_1.deploy_fleet()
board_2.deploy_fleet()

# Initialize variables
turn_player1 = ct.ITS_P1_TURN
turn_player2 = ct.ITS_P2_TURN
player_1_lives_left = np.sum(board_1.my_board == 'O')
player_2_lives_left = np.sum(board_2.my_board == 'O')

while True and player_1_lives_left > 0 and player_2_lives_left > 0:
    choice = 1

    if turn_player1:
        # Display options available for Player 1
        print('\nYour turn. Your options are:')
        print('1 - Attack your enemy')
        print('2 - Display your board')
        print("3 - Display your tracking of your enemy's board")
        print('4 - Quit the game\n')
        option = input('Enter your choice -> ')
        while option not in ['1', '2', '3', '4']:
            print('Wrong choice. Try again.')
            option = input('Enter your choice -> ')
        else:
            choice = int(option)

    if choice == 1:
        if turn_player1:
            print('\nEnter the position of your shot (row and column): ')
            shoot_row = int(input('\tRow - 0 to 9 -> '))
            shoot_column = int(input('\tColumn - 0 to 9 -> '))
            hit = True
            while hit:
                hit = func.shoot_to_sink(shoot_row, shoot_column, board_2.my_board, board_1.enemys_track_board)
                if hit:
                    print(f'PLAYER 1 ({shoot_row}, {shoot_column}) -- That was a HIT!')
                    player_2_lives_left -= 1
                    if player_2_lives_left > 0:
                        print(f'Keep playing!')
                    break
                else:
                    print(f'PLAYER 1 ({shoot_row}, {shoot_column}) -- That was a MISS...')
                    turn_player1 = False
                    turn_player2 = True

        elif turn_player2:
            print('\nTurn for Player 2')
            hit = True
            while hit:
                shoot_row, shoot_column = func.find_coord_to_shoot(board_2.enemys_track_board)
                hit = func.shoot_to_sink(shoot_row, shoot_column, board_1.my_board, board_2.enemys_track_board)
                if hit:
                    print(f'PLAYER 2 ({shoot_row}, {shoot_column}) -- That was a HIT!')
                    player_1_lives_left -= 1
                    if player_1_lives_left > 0:
                        print(f'PLAYER 2 keeps playing!')
                else:
                    print(f'PLAYER 2 ({shoot_row}, {shoot_column}) -- That was a MISS...')
                    turn_player1 = True
                    turn_player2 = False

    elif choice == 2:
        # Option 2 - Display P1's board and lives left for both contenders
        print('\nThis is your board - as it currently is: \n')
        print(board_1.my_board)
        print(f'\nLives left for you:  {player_1_lives_left}')
        print(f'Lives left for your enemy: {player_2_lives_left}')

    elif choice == 3:
        # Option 3 - Display P1's enemy tracking board and lives left for both contenders
        print("\nThis is your tracking of your enemy's board: \n")
        print(board_1.enemys_track_board)
        print(f'\nLives left for you:  {player_1_lives_left}')
        print(f'Lives left for your enemy: {player_2_lives_left}')

    elif choice == 4:
        really = input('Are you sure you want to quit the game (Y/N)?')
        if really.lower() == 'y':
            print('Game over!\n')
            break
        else:
            continue

    else:
        print('Wrong choice. Try again.')


