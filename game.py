'''CS5001
   Karan Satwani
   Project
   Game Class
'''

from draw import Turtle_connect
from win import Win
import random
import turtle

class Game:
    '''class: Game
       Attributes:
                2 integers -- rows and columns
                2 floats -- initial x and y coordinates
                2 strings -- red_file, yellow_file
       Methods: position_slots_y, position_slots_x, initial_empty_panel,
                click_column, column_count, computer_turn, player_turn
    '''

    def __init__(self, rows, columns, initial_x, initial_y, red_file, yellow_file):
        '''
         Constructor -- creates Game to play connect4
         Parameters:
            self -- the current object
            rows -- number of rows for connect 4 grid, an integer
            columns -- number of columns for connect 4 grid, an integer
            initial_x -- initial x coordinate, float
            initial_y -- initial y coordinate, float
            red_file -- string with the name of file for red player
            yellow_file -- string with the name of file for yellow player
         '''
        self.rows = rows
        self.columns = columns
        self.initial_x = initial_x
        self.initial_y = initial_y

        #additional
        self.dict = {}
        self.y_positions = []
        self.x_positions = []


        self.player_value = 2
        self.computer_value = 5

        self.turtle_draw = Turtle_connect(rows, columns, self.initial_x, self.initial_y)
        self.column_count(self.columns)
        self.win = Win(self.rows, self.columns, self.initial_x,\
                       self.initial_y, red_file, yellow_file)
       

    def position_slots_y(self):
        '''
        Method -- positions for y axis
        Parameters:
            self -- the current object
        Return -- list with positions where circles are drawn on the y axis
        '''        
        
        self.y_positions = [0] * (self.rows+2)
        self.y_positions[0] = self.initial_y + 10
        for i in range(1, self.rows +  2):
            self.y_positions[i] = self.y_positions[i - 1] + 70


        return self.y_positions

    def position_slots_x(self):
        '''
        Method -- positions for x axis
        Parameters:
            self -- the current object
        Return -- list with positions where circles are drawn on the x axis
        '''
        self.x_positions = [0]*(self.columns + 1)
        self.x_positions[0] = self.initial_x + 18
        for i in range(1, self.columns + 1):
            self.x_positions[i] = self.x_positions[i - 1] + 75


        return self.x_positions
    
    def initial_empty_panel(self, rows, columns):
        '''
        Method -- creating initial empty panel/grid
        Parameters:
            self -- the current object
            rows -- number of rows for connect 4 grid, an integer
            columns -- number of columns for connect 4 grid, an integer
        Return -- nestedlist with all 0's
        '''

        self.empty_panel = [[0] * columns for i in range(rows)]
        self.updated_panel = self.empty_panel
        
    
        return self.empty_panel
    
    
    def click_column(self, x, y):
        '''
        Method -- click column
        Parameters:
            self -- the current object
            x -- x coordinate where the player clicked
            y -- y coordinate where the player clicked
        Return -- column number where the player clicked, an int
        Does -- converts the coordinates (if valid) to a column number,
                also calls the player_turn method
        '''
        
        self.drop_in_column = -1

        if y <= self.y_positions[-1] and y >= self.y_positions[-2]+40:
            if x >= self.x_positions[0] and x <= self.x_positions[-1]:
                for i in range(self.columns):
                    if x >= self.x_positions[i] and x <= self.x_positions[i + 1] - 20:
                        self.drop_in_column = i
                        self.play_column = self.drop_in_column
                        self.dict[self.play_column] += 1

                        while True:
                            if self.dict[self.play_column] >= self.rows+1:
                                self.dict[self.play_column] -= 1
                                turtle.onscreenclick(self.click_column)
                            else:   
                                break
                      
                        self.player_turn(self.updated_panel)  
        else:
            self.drop_in_column = 0

        return self.drop_in_column


    def column_count(self, columns):
        '''
        Method -- column count 
        Parameters:
            self -- the current object
            columns -- number of columns for connect 4 grid, an integer
        Does -- makes a dictionary wtith every column number as key
                and 0's values which get updated later when player/computer selects the column.
                This is used to check if the column is full and  it cannot take in more pieces
        '''
        self.dict = {}
        self.keys = range(columns + 1)
        values = [0]*(columns + 1)
        for i in self.keys:
            self.dict[i] = values[i]
            
        return
        
    def computer_turn(self, updated_panel):
        '''
        Method -- computer_turn 
        Parameters:
            self -- the current object
            updated_panel -- nested list with values of the current grid/panel
        Does -- computer pick a random valid column, updates the gird, calls turtle,
                check for win/draw and calls onscreenclick fucntion to switch to player
        '''
        self.updated_panel = updated_panel
        self.computer_play = random.randint(0,self.columns - 1)

        while True:
            if self.updated_panel[0][self.computer_play] != 0:
                self.computer_play = random.randint(0,self.columns - 1)
            else:
                break
        
        if updated_panel[-1][self.computer_play] == 0:
            updated_panel[-1][self.computer_play] = self.computer_value
            
            self.updated_panel = updated_panel
            self.dict[self.computer_play] += 1
            recent_fill = [0,self.computer_play]
            
            #filling circle
            self.turtle_draw.color_turns(self.computer_value, recent_fill,\
                                         self.x_positions, self.y_positions)

            #checking wins
            self.win.check_wins(updated_panel,recent_fill,self.computer_value)

            #for A+
            again = random.randint(0,3)
            
            if again % 2 == 1:
                self.turtle_draw.text_A(self.x_positions[2],self.y_positions[0],\
                                                self.computer_value)
                self.computer_turn(updated_panel)
                
            else:
                #clearing again text
                self.turtle_draw.text_A(self.x_positions[2],self.y_positions[0],0)
                
                #player value because comp played its turn
                self.turtle_draw.whose_turn(self.player_value)   
                turtle.onscreenclick(self.click_column)

        else:
            self.dict[self.computer_play] += 1
      
            self.temp_col = -self.dict[self.computer_play]

            if updated_panel[self.temp_col][self.computer_play] == 0:
                
                updated_panel[self.temp_col][self.computer_play] = self.computer_value
                row = -self.temp_col - 1
                
                if row < 0:
                    row *= -1

                recent_fill = [row,self.computer_play]
                
                #filling circle
                self.turtle_draw.color_turns(self.computer_value, recent_fill,\
                                             self.x_positions, self.y_positions)

                #checking wins
                self.win.check_wins(updated_panel, recent_fill, self.computer_value)

                #for A+
                again = random.randint(0,3)
                
                if again % 2 == 1:
                    self.turtle_draw.text_A(self.x_positions[2], self.y_positions[0],\
                                                self.computer_value)
                    self.computer_turn(updated_panel)
                else:
                    #clearing again text
                    self.turtle_draw.text_A(self.x_positions[2], self.y_positions[0], 0)
                    
                    #player value because comp played its turn
                    self.turtle_draw.whose_turn(self.player_value)
                    turtle.onscreenclick(self.click_column)
    
        return self.updated_panel
        
    def player_turn(self, updated_panel):
        '''
        Method -- player_turn 
        Parameters:
            self -- the current object
            updated_panel -- nested list with values of the current grid/panel
        Does --  updates the gird with already selected column in the click_column method,
                 calls turtle, check for win/draw and calls computer_turn method
        '''
        
        updated_panel = self.updated_panel
            
        if updated_panel[-1][self.play_column] == 0:

            updated_panel[-1][self.play_column] = self.player_value
            recent_fill = [0,self.play_column]

            #filling circle
            self.turtle_draw.color_turns(self.player_value, recent_fill,\
                                         self.x_positions, self.y_positions)

            #checking wins
            self.win.check_wins(updated_panel, recent_fill, self.player_value)
            
            #for A+
            again = random.randint(0,3)

            if again % 2 == 1:
                self.turtle_draw.text_A(self.x_positions[2], self.y_positions[0],\
                                                self.player_value)
                turtle.onscreenclick(self.click_column)
                
            else:
                #clearing again text
                self.turtle_draw.text_A(self.x_positions[2], self.y_positions[0], 0)
                
                #computer value because player played its turn
                self.turtle_draw.whose_turn(self.computer_value)
                self.computer_turn(updated_panel)
    
        else:

                self.temp_col = -self.dict[self.play_column]

                if updated_panel[self.temp_col][self.play_column] == 0:
                    
                    updated_panel[self.temp_col][self.play_column] = self.player_value
                    row = -self.temp_col - 1
                    
                    if row < 0:
                        row *= -1
                        
                    recent_fill = [row,self.play_column]

                    #filling circle
                    self.turtle_draw.color_turns(self.player_value, recent_fill,\
                                                 self.x_positions, self.y_positions)

                    #checking wins
                    self.win.check_wins(updated_panel,recent_fill,self.player_value)
                    
                    #for A+
                    again = random.randint(0,3)
 
                    if again % 2 == 1:
                        self.turtle_draw.text_A(self.x_positions[2], self.y_positions[0],\
                                                self.player_value)
                        turtle.onscreenclick(self.click_column)
                        
                    else:
                        #clearing again text
                        self.turtle_draw.text_A(self.x_positions[2], self.y_positions[0], 0)
                        
                        #computer value because player played its turn
                        self.turtle_draw.whose_turn(self.computer_value)
                        self.computer_turn(updated_panel)

                    
                    


    
                
                





