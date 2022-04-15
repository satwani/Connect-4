'''CS5001
   Karan Satwani
   Project
   Win Class
'''

import turtle
from draw import Turtle_connect

class Win:
    '''class: Win
       attributes:
                2 integers -- rows and columns
                2 floats -- initial x and y coordinates
                2 strings -- red_file, yellow_file
       methods: initialize_red, initialize_yellow, check_wins, no_wins,
                hortizontal_win, vertical_win, diagonal_win_right,
                diagonal_win_left, declare_winner, update_score
               
    '''

    def __init__(self, rows, columns, initial_x, initial_y, red_file, yellow_file):
        '''
        Constructor -- creates win instances for connect4
        Parameters:
            self -- the current object
            rows -- number of rows for connect 4 grid, an integer
            columns -- number of columns for connect 4 grid, an integer
            initial_x -- initial x coordinate, float
            initial_y -- initial y coordinate, float
            red_file -- string with the name of file for red player
            yellow_file -- string with the name of file for yellow player
        '''


        self.columns = columns
        self.rows = rows


        self.red_file_name = red_file
        self.yellow_file_name = yellow_file

        self.red_score = 0
        self.yellow_score = 0
        
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.draw = Turtle_connect(self.rows, self.columns,\
                              self.initial_x, self.initial_y)
        


    def initialize_red(self):
        '''
        Method -- initialize red file
        Parameters:
            self -- the current object
        Return -- score for red player, an int
        '''
        self.red_score = 0
        try:
            with open(self.red_file_name, 'r') as infile:
                self.red_score = int(infile.read().strip())
        except OSError:
            with open(self.red_file_name, 'w') as outfile:
                outfile.write("0")
                self.red_score = 0

        return self.red_score

    def initialize_yellow(self):
        '''
        Method -- initialize yellow file
        Parameters:
            self -- the current object
        Return -- score for yellow player, an int
        '''
        self.yellow_score = 0
        try:
            with open(self.yellow_file_name, 'r') as infile:
                self.yellow_score = int(infile.read().strip())
        except OSError:
            with open(self.yellow_file_name, 'w') as outfile:
                outfile.write("0")
                self.yellow_score = 0

        return self.yellow_score

    def check_wins(self, updated_grid, recent_play, player_turn):
        '''
        Method -- calling other methods to check for all types of win and a draw
        Parameters:
            self -- the current object
            updated_grid -- nested list with values of the current grid/panel
            recent_play -- list with row and column number of the last play
            turn -- number indicating who played the current turn, an integer
        Return: nothing
        '''
        self.updated_grid = updated_grid
        self.recent_play = recent_play
        self.player_turn = player_turn

        
        #checking for all wins
        self.horizontal_win(self.updated_grid,self.recent_play,self.player_turn)
        self.vertical_win(self.updated_grid,self.recent_play,self.player_turn)
        self.diagonal_win_right(self.updated_grid,self.rows,self.columns,\
                                self.player_turn)
        self.diagonal_win_left(self.updated_grid,self.rows,self.columns,\
                                self.player_turn)

        
        #checking for a draw
        winner = self.no_win(self.updated_grid)
        if winner == 0:
            self.declare_winner()
        

    def no_win(self, full_grid):
        '''
        Method --  cheking for a no win/draw situation
        Parameters:
            self -- the current object
            full_grid -- a nested list with current situation of the grid
        Return: self.winner, an integer showing if it a draw or not
        '''
        self.winner = 1
        if 0 not in full_grid[0]:
            self.winner = 0
            

        return self.winner

    def horizontal_win(self, updated_grid, recent_play, player_turn):
        '''
        Method -- horizontal win
        Parameters:
            self -- the current object
            updated_grid -- nested list with values of the current grid/panel
            recent_play -- list with row and column number of the last play
            player_turn -- number indicating who played the current turn, an integer
        Return: nothing
        '''
        self.updated_grid = updated_grid
        self.recent_play = recent_play
        self.player_turn = player_turn
        self.winner = 1 #not player or computer
        
        self.check_row = -self.recent_play[0] - 1
        
        for i in range(len(self.updated_grid[self.check_row]) - 3):
            if self.updated_grid[self.check_row][i] == self.player_turn \
               and self.updated_grid[self.check_row][i+1] == self.player_turn\
               and self.updated_grid[self.check_row][i+2] == self.player_turn\
               and self.updated_grid[self.check_row][i+3] == self.player_turn:
               self.winner = self.player_turn
               self.declare_winner()
               break

    def vertical_win(self, updated_grid, recent_play, player_turn):
        '''
        Method -- vertical win
        Parameters:
            self -- the current object
            updated_grid -- nested list with values of the current grid/panel
            recent_play -- list with row and column number of the last play
            player_turn -- number indicating who played the current turn, an integer
        Return: nothing
        '''
        self.updated_grid = updated_grid
        self.recent_play = recent_play
        self.player_turn = player_turn
        self.winner = 1 #not player or computer
        
        self.check_column = self.recent_play[1]

        for i in range(len(self.updated_grid) - 3):
  
            if self.updated_grid[i][self.check_column] == self.player_turn\
               and self.updated_grid[i+1][self.check_column] == self.player_turn\
               and self.updated_grid[i+2][self.check_column] == self.player_turn\
               and self.updated_grid[i+3][self.check_column] == self.player_turn:
               self.winner = self.player_turn
               self.declare_winner()
               break

    def diagonal_win_right(self, updated_grid, rows, columns, player_turn):
        '''
        Method -- diagonal win going right on the grid
        Parameters:
            self -- the current object
            updated_grid -- nested list with values of the current grid/panel
            rows -- number of rows for connect 4 grid, an integer
            columns -- number of columns for connect 4 grid, an integer
            player_turn -- number indicating who played the current turn, an integer
        Return: nothing
        '''
        self.columns = columns
        self.rows = rows
        self.updated_grid = updated_grid
        self.player_turn = player_turn
        self.winner = 1 #not player or computer
        
        
        for i in range(self.columns):
            for j in range(self.rows-1, -1, -1):
                if i + 3 < self.columns and j - 3 > -1:
                    if self.updated_grid[j][i] == self.player_turn\
                       and self.updated_grid[j-1][i+1] == self.player_turn\
                       and self.updated_grid[j-2][i+2] == self.player_turn\
                       and self.updated_grid[j-3][i+3] == self.player_turn:
                           self.winner = self.player_turn
                           self.declare_winner()
                           break



    def diagonal_win_left(self, updated_grid, rows, columns, player_turn):
        '''
        Method -- diagonal win going left on the grid
        Parameters:
            self -- the current object
            updated_grid -- nested list with values of the current grid/panel
            rows -- number of rows for connect 4 grid, an integer
            columns -- number of columns for connect 4 grid, an integer
            player_turn -- number indicating who played the current turn, an integer
        Return: nothing
        '''
        self.columns = columns
        self.rows = rows
        self.updated_grid = updated_grid
        self.player_turn = player_turn
        self.winner = 1 #not player or computer
        
        for m in range(self.columns):
            for n in range(self.rows):
                if m + 3 < self.columns and n + 3 <self.rows:
                    if self.updated_grid[n][m] == self.player_turn\
                       and self.updated_grid[n+1][m+1] == self.player_turn\
                       and self.updated_grid[n+2][m+2] == self.player_turn\
                       and self.updated_grid[n+3][m+3] == self.player_turn:
                           self.winner = self.player_turn
                           self.declare_winner()
                           break



    def declare_winner(self):
        '''
        Method -- declaring winner by checking which player won
        Parameters:
            self -- the current object
        Does -- call other method to update score and calls turtle 
        '''
        original_yellow_score = self.initialize_yellow()
        original_red_score = self.initialize_red()
   
        if self.winner == 2:
            new_red_score = int(original_red_score)
            
            new_red_score += 1
            new_red_score = str(new_red_score)

            #updating score
            self.update_score(new_red_score, self.red_file_name)

            #calling turtle
            self.draw.winner_display(self.winner)
         
        elif self.winner == 5:
            new_yellow_score = int(original_yellow_score)
            new_yellow_score += 1
            new_yellow_score = str(new_yellow_score)
            
            #updating score
            self.update_score(new_yellow_score, self.yellow_file_name)
            
            #calling turtle
            self.draw.winner_display(self.winner)

        elif self.winner == 0:

            #calling turtle
            self.draw.winner_display(self.winner)


    def update_score(self,score,file_name):
        '''
        Method -- initialize yellow file
        Parameters:
            self -- the current object
            score -- updated score of the player who won, an int
            file_name -- name of the file to be updated, a string
        Return -- nothing
        '''
        self.new_score = score
        
        try:
            with open(file_name, 'w') as infile:
                infile.write(self.new_score)
        except OSError:
                print("Could not update score")
            
        
        
