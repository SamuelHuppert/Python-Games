import random

HIT_CHAR = 'x'
MISS_CHAR = 'o'
BLANK_CHAR = '.'
HORIZONTAL = 'h'
VERTICAL = 'v'
MAX_MISSES = 20
SHIP_SIZES = {
    "carrier": 5,
    "battleship": 4,
    "cruiser": 3,
    "submarine": 3,
    "destroyer": 2
}
NUM_ROWS = 10
NUM_COLS = 10
ROW_IDX = 0
COL_IDX = 1
MIN_ROW_LABEL = 'A'
MAX_ROW_LABEL = 'J'


def get_random_position():
    row_choice = chr(
                    random.choice(
                        range(
                            ord(MIN_ROW_LABEL),
                            ord(MIN_ROW_LABEL) + NUM_ROWS
                        )
                    )
    )
    col_choice = random.randint(0, NUM_COLS - 1)
    return (row_choice, col_choice)


def play_battleship():

    while not game_over:
        game = Game()
        game.display_board()
        while not game.is_complete():
            pos = game.get_guess()
            result = game.check_guess(pos)
            game.update_game(result, pos)
            game.display_board()
        game_over = end_program()

    print("Goodbye.")

class Ship:
    def __init__(self, name, start_position, orientation):
        self.name=name
        self.positions={}
        self.sunk=False
        size_of_ship=SHIP_SIZES[name]
        self.positions[(start_position[0],start_position[1])]=False
        rows="ABCDEFGHIJ"
        rows_list=[]
        row_index=[rows.index(start_position[0])]
        if orientation=='h':
            for i in range(0,size_of_ship):
                self.positions[(start_position[0],start_position[1]+i)]=False
        if orientation=='v':
            for i in range(0,size_of_ship):     #Create a list of the cols
                rows_list.append(rows[i+row_index[0]])
            for i in rows_list:     #Go through all the collumns
                self.positions[(i,start_position[1])]=False




class Game:
    def __init__(self, max_misses = MAX_MISSES):
        self.max_misses=max_misses
        self.board={}
        self.guesses=[]
        self.ships=[]
        self.initialize_board()
        self.create_and_place_ships()

    def initialize_board(self):
        temp_dict={}
        rows="ABCDEFGHIJ"
        for i in rows:
            self.board[i]=['.','.','.','.','.','.','.','.','.','.']

    _ship_types = ["carrier", "battleship", "cruiser", "submarine", "destroyer"]
    def update_game(self, guess_status, position):
        row=position[0]
        col=position[1]
        temporary_list=self.board[row]
        if guess_status==True:
            temporary_list[col]=HIT_CHAR
        if guess_status==False:
            if not temporary_list[col]==HIT_CHAR:
                temporary_list[col]=MISS_CHAR
                self.guesses.append(position)
            else:
                self.guesses.append(position)
        self.board[row]=temporary_list
    def is_complete(self):
        x=True
        for ship in self.ships:
            if ship.sunk==False:
                x=False
        if x==True:
            print("YOU WIN!")
            return True
        if len(self.guesses)>=self.max_misses:
            print("SORRY! NO GUESSES LEFT.")
            return True
        return False

    def in_bounds(self, start_position, ship_size, orientation):
        rows="ABCDEFGHIJ"
        if orientation=='h':
            if start_position[1]+ship_size<=NUM_COLS:
                return True
            else:
                return False
        if orientation=='v':
            if rows.index(start_position[0])+ship_size+1<NUM_ROWS:
                return True
            else:
                return False


    def overlaps_ship(self, start_position, ship_size, orientation):
        rows="ABCDEFGHIJ"
        rows_list=[]
        row_index=[rows.index(start_position[0])]
        ship_pos={}
        ship_pos[(start_position[0],start_position[1])]=False
        if orientation=='h':
            for i in range(0,ship_size):
                ship_pos[(start_position[0],start_position[1]+i)]=False
        if orientation=='v':
            for i in range(0,ship_size):     #Create a list of the cols
                rows_list.append(rows[i+row_index[0]])
            for i in rows_list:     #Go through all the collumns
                ship_pos[(i,start_position[1])]=False
        list_of_keys=[]
        keys=ship_pos.keys()
        for key in keys:
            list_of_keys.append(key)
        list_of_other_keys=[]
        for ship in self.ships:
            for position in ship.positions:
                list_of_other_keys.append(position)
        for keys in list_of_keys:
            for forbidden_keys in list_of_other_keys:
                if keys==forbidden_keys:
                    return True
        return False
    def place_ship(self, start_position, ship_size):
        if self.in_bounds(start_position, ship_size, 'h') and not self.overlaps_ship(start_position, ship_size, 'h'):
            return 'h'
        if self.in_bounds(start_position,ship_size,'v') and not self.overlaps_ship(start_position, ship_size,'v'):
            return 'v'
    def create_and_place_ships(self):

        for ship in self._ship_types:
            orientation=''
            while not (orientation=='v'or orientation=='h'):
                random_pos=get_random_position()
                size=SHIP_SIZES[ship]
                orientation=self.place_ship(random_pos, size)
            new_ship=Ship(ship,random_pos,orientation)
            self.ships.append(new_ship)
    def get_guess(self):
        cols='0' \
             '123456789'
        rows='ABCDEFGHIJabcdefghij'
        x=False         #use this 'x' in order to keep the while loop running for collumn
        y=False         #For rows
        while y==False:
            guess= input("Enter a row: ")
            for char in rows:
                if char==guess:
                    y=True
                    row=char.upper()
        while x==False:
            guess= input("Enter a column: ")
            for num in cols:
                if num==guess:
                    x=True
                    collumn=num
        position=(row,int(collumn))
        return (position)

    def check_guess(self, position):
        hit=False
        index_of_hit=0
        j=0
        for ship in self.ships:
            for i in ship.positions.keys():
                if i==position:
                    if ship.positions[position]==False:
                        ship.positions[position]=True
                        hit=True
                        index_of_hit=j
            j+=1
        sunk=False
        if hit==True:
            sunk=True
            for value in self.ships[index_of_hit].positions.values():
                if value==False:
                    sunk=False
        if sunk==True:
            print("You sunk the "+ self.ships[index_of_hit].name+'!')
            self.ships[index_of_hit].sunk=True

        if hit:
            return True
        else:
            return False


    def display_board(self):
        """ Displays the current state of the board."""

        print()
        print("  " + ' '.join('{}'.format(i) for i in range(len(self.board))))
        for row_label in self.board.keys():
            print('{} '.format(row_label) + ' '.join(self.board[row_label]))
        print()

def end_program():
    play=''
    while play!='n' and play!='N' and play!='y' and play!='Y':
        play=input("Play again (Y/N)?\n")
    if play=='n' or play=='N':
        return True
    else:
        return False

def main():
    play_battleship()


if __name__ == "__main__":
    main()
