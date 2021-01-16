'''
Created on Jan 14, 2021

console based tictactoe game - 2 player

@author: Alec Parfitt
'''

def print_board(current_board):
    ''' Prints board state dict as (ugly) formatted tictactoe board '''
    print()
    count = 0
    ends = (2, 5, 8)
    for location in current_board:
        for status in current_board[location]:
            if count % 3 == 0 and count != 0:
                print()
                print('-----------')
            if count not in ends:
                print(f' {status} |', end = '')
            else:
                print(f' {status} ', end = '')
            count += 1
    print('\n')
    
def game_state_check(current_board, piece = 'x'):
    ''' Compares board to win conditions to see if any are met '''
    win_states = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],
            ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
            ['1', '5', '9'], ['3', '5', '7']]
    
    occupant = ''
    win = piece * 3
    for win_state in win_states:
        for pos in win_state:
            occupant += current_board[pos]
        if occupant == win:
            return True
        occupant = ''
    return False
        
    
if __name__ == '__main__':
    # current board is kept as 3x3 dictionary
    board = {
                '1' : '1', '2' : '2', '3' : '3',
                '4' : '4', '5' : '5', '6' : '6',
                '7' : '7', '8' : '8', '9' : '9'
            }
    play_count = 0
    moves_history = []
    winner = ''
    
    print('Welcome to TicTacToe!')
    print('Take turns picking positions on the board with a number selection')
    print('corresponding to the spot on the board.\n')
    print_board(board)
    
    # Main program loop. Starts by asking the first ('X') user for numeric input,
    # alternates between users to populate board dict with 'X's or 'O's until either
    # user opts to quit, win conditions are met, or stalemate has been reached.
    selection = input('Enter X position to make first move or any other key to quit: ')
    while (selection != 'q') and len(moves_history) < 9 and winner == '':
        if selection in moves_history:
            print('already played! try again')
            selection = input('enter un-played position: ')
            continue
        if selection not in board:
            selection = input('Enter a valid position or q to quit: ')
        # X gets first move. If it wins or the move fills the board, loop will terminate
        if ((play_count == 0) or (play_count % 2 == 0)):
            board[selection] = 'X'
            moves_history.append(selection)
            play_count += 1
            print_board(board)
            if game_state_check(board, 'X'):
                winner = 'X'
            elif len(moves_history) < 9:
                selection = input('Enter next position for O: ')
        # O's turn. moves_history gets appended inside these blocks
        else:
            board[selection] = 'O'
            moves_history.append(selection)
            play_count += 1
            print_board(board)
            if game_state_check(board, 'O'):
                winner = 'O'
            elif len(moves_history) < 9:
                selection = input('Enter next position for X: ')
                
    if winner == '':
        print('no winner!')
    else:
        print(f'{winner} wins!!!!')