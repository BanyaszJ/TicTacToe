import numpy as np

class Map:
    def __init__(self, rows, cols):
        self.empty_cell = "*"
        self.rows = rows
        self.cols = cols
        self.map  = self.generate_map(self.rows, self.cols)
        self.show()

    def generate_map(self, n, m):

        self.outer_map = []

        for i in range(n):
            self.inner_map = [self.empty_cell]*m
            self.outer_map.append(self.inner_map)
        return self.outer_map

    def validate_selection(self, player_row, player_col):
    
        is_valid = False

        if self.rows > player_row and self.cols > player_col: # are row/col coordinates within range?
            if self.map[player_row][player_col] == self.empty_cell: # is the selected cell an empty cell?
                is_valid = True

        return is_valid

    def apply_selection(self, player_row, player_col, icon):
        self.map[player_row][player_col] = icon

    def show(self):
        for item in self.map:
            print(" ".join(str(x) for x in item))

    def winner_found(self):

        done = False

        # ROWS AND COLS
        for i in [self.map, np.transpose(self.map)]: # original self.map for rows, andd transposed self.map for cols
            for row in i:
                if self.empty_cell in row: continue
                if all(x == row[0] for x in row): # if all elements of list are equal
                    done = True
        print(done)
        # DIAGONALS (still ugly, and does not work on other than 3x3...)
        if (self.map[0][0]==self.map[1][1]==self.map[2][2] and self.map[0][0] != "*"):
            done = True
        if (self.map[2][0]==self.map[1][1]==self.map[0][2] and self.map[2][0] != "*"):
            done = True

        if done:
            print("A winner has been found!")

        return done

    def is_full(self):

        summarizer = 0

        for i in self.map:
            if self.empty_cell in i:
                summarizer += 1
        if summarizer == 0:
            print("Board is full!")
            return True


class Player:
    def __init__(self, number, icon):
        self.number = number
        self.icon   = icon
        self.selection = None
        
        self.selected_row = None
        self.selected_col = None

    def select(self):
        while True:
            self.selected_row = int(input("Player %s select ROW: " % self.number))
            self.selected_col = int(input("Player %s select COL: " % self.number))

            # if self.selected_row.isdigit() and self.selected_col.isdigit():
            # TODO: IF EXCEPTION: VALUEERROR: RETRY
            return
            # else:
                # print("Invalid row/col, please try again!")
class Main:
    def __init__(self):
        self.p1 = Player(number = 1, icon = "X")
        self.p2 = Player(number = 2, icon = "O")
        self.map = Map(rows = 3, cols = 3) # 3x3... TODO: fix winner_found and is_full

    def start(self):
        while True:
            for curr_player in [self.p1, self.p2]:
                self.next_player_is(curr_player)
                if self.map.winner_found() or self.map.is_full(): return 0 # program stops

    def next_player_is(self, player):
        while True:
            player.select()
            if self.map.validate_selection(player.selected_row, player.selected_col) == True: break

        self.map.apply_selection(player.selected_row, player.selected_col, player.icon)
        self.map.show()


main = Main()
main.start() # program starts
