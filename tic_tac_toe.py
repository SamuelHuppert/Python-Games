
MAX_ROUNDS = 9
NUM_ROWS = 3
NUM_COLS = 3
NUM_POSITIONS = 9
ROW_POS = 0
COL_POS = 1
def reset_board(board):
    for key in board.keys():
        board[key]=' '
def get_current_player(round):
    if round%2==0:
        return 'X'
    else:
        return 'O'
def get_position_choice(board, player_mark):
    print(player_mark+',')
    row=-1
    col=-1
    while  row!=0 and row!=1 and row!=2:
        row=int(input("Choose your row: "))
    while  col!=0 and col!=1 and col!=2:
        col=int(input("Choose your column: "))
    print()
    tuple=(row,col)
    while board[tuple]!=' ':
        row=-1
        col=-1
        while  row!=0 and row!=1 and row!=2:
            row=int(input("Choose your row: "))
        while  col!=0 and col!=1 and col!=2:
            col=int(input("Choose your column: "))
        tuple=(row,col)
        print()
    return tuple
def update_board(board, player_mark, position):
    board[position]=player_mark
def display_outcome(round):
    
    if round==MAX_ROUNDS:
        print("It's a draw!\n")
    elif get_current_player(round)=='X':
        print("X wins!\n")
    elif get_current_player(round)=='O':
        print("O wins!\n")
def check_positions(pos1_value, pos2_value, pos3_value):
    
    if pos1_value=='X'and pos2_value=='X' and pos3_value=='X':
        return True
    elif pos1_value=='O'and pos2_value=='O' and pos3_value=='O':
        return True
    else:
        return False
def is_game_complete(board):
    rows=(0,1,2)
    cols=(0,1,2)
    for col in cols:
        x=0
        o=0
        for row in rows:
            if board[row,col]=='X':
                x+=1
            if board[row,col]=='O':
                o+=1
        if x==3 or o==3:
            return True
    rows=(0,1,2)
    cols=(0,1,2)
    for row in rows:
        x=0
        o=0
        for col in cols:
            if board[row,col]=='X':
                x+=1
            if board[row,col]=='O':
                o+=1
        if x==3 or o==3:
            return True
    if (board[0,0]=='X' and board[1,1]=='X' and board[2,2]=='X') or (board[0,2]=='X' and board[1,1]=='X' and board[2,0]=='X'):
        return True
    if (board[0,0]=='O' and board[1,1]=='O' and board[2,2]=='O') or (board[0,2]=='O' and board[1,1]=='O' and board[2,0]=='O'):
        return True
    return False
def play_tic_tac_toe(board):
    print("Let's Play Tic-tac-toe!\n")
    round=0
    while (not is_game_complete(board)) and round<MAX_ROUNDS:
        print(round)
        display_board(board)
        player_mark=get_current_player(round)
        position=get_position_choice(board,player_mark)
        update_board(board,player_mark,position)
        round+=1

    display_board(board)
    if is_game_complete(board)==True and round==MAX_ROUNDS:
        display_outcome(2) #Just an even number so it'll display X
    elif round==MAX_ROUNDS:
        display_outcome(round)
    else:
        display_outcome(round-1)
    while not is_program_finished():
        round=0
        reset_board(board)
        while (not is_game_complete(board)) and round<MAX_ROUNDS:
            display_board(board)
            player_mark=get_current_player(round)
            position=get_position_choice(board,player_mark)
            update_board(board,player_mark,position)
            round+=1
        display_board(board)
        if is_game_complete(board)==True and round==MAX_ROUNDS:
            print("BUGDETECTED1")
            display_outcome(2) #Just an even number so it'll display X
        elif round==MAX_ROUNDS:
            display_outcome(round)
        else:
            display_outcome(round-1)
    print("Goodbye.")
def is_program_finished():
    play=''
    while play!='n' and play!='N' and play!='y' and play!='Y':
        play=input("Play again (Y/N)?\n")
    if play=='n' or play=='N':
        return True
    else:
        return False
def display_board(board):

    print("     0 1 2 ")

    for row in range(0, NUM_ROWS):
        print("  {}  ".format(row), end="")
        for col in range(0, NUM_COLS):
            if col == 0:
                print(board[(row, col)], end="")
            else:
                print("|{}".format(board[(row, col)]), end="")

        print(" ")

        if row < NUM_ROWS - 1:
            print("    --+-+--")
    print()



def main():

    board = {
        (0,0): ' ', (0,1): ' ', (0,2): ' ',
        (1,0): ' ', (1,1): ' ', (1,2): ' ',
        (2,0): ' ', (2,1): ' ', (2,2): ' '
    }
    play_tic_tac_toe(board)
if __name__ == '__main__':
    main()
