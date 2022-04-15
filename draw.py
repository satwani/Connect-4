'''CS5001
   Karan Satwani
   Project
   Turtle class
'''

import turtle
import sys


BOARD_COLOR = "blue"
BOARD_SHAPE = "square"
BOARD_CIRCLE_COLOR = "White"
PLAYER_1_COLOR = "Red"
COMPUTER_COLOR = "Yellow"

class Turtle_connect:
    '''class: Turtle_drawings
       Attributes: 2 integers -- rows and columns
                   2 floats -- initial x and y coordinates
       Methods: draw_board, circles_and_arrows, color_turns,
                display_scores, whose_turn, winner_display, text_A

    '''

    def __init__(self,rows,columns,initial_x,initial_y):
        '''
        Constructor -- creates the game connect 4 using turtle
        Parameters:
            self -- the current object
            rows -- number of rows for connect 4 grid, an integer
            columns -- number of columns for connect 4 grid, an integer
            initial_x -- initial x coordinate, float
            initial_y -- initial y coordinate, float
        '''

        self.rows =rows
        self.columns = columns
        self.initial_x = initial_x
        self.initial_y = initial_y
      

    def draw_board(self,rows,columns):
        '''
        Method --  drawing only the board(without circles)
        Parameters:
            self -- the current object
            rows -- number of rows for connect 4 grid, an integer
            columns -- number of columns for connect 4 grid, an integer
        Return: nothing
        '''


        turtle.hideturtle()
        turtle.screensize(rows*250, columns*250)
        turtle.speed(0)
        turtle.penup()
        turtle.goto(self.initial_x,self.initial_y)
        turtle.color(BOARD_COLOR)
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(77*columns)
            #turtle.left(90)
            turtle.circle(20,90)
            turtle.forward(70*rows)
            turtle.circle(20,90)
            #turtle.left(90)
        turtle.end_fill()
        

        return 

    def circles_and_arrows(self,rows,columns,positions_x,positions_y):
        '''
        Method --  drawing circles and arrows
        Parameters:
            self -- the current object
            rows -- number of rows for connect 4 grid, an integer
            columns -- number of columns for connect 4 grid, an integer
            positions_x -- list of positions for x coordinates
            positions_y -- list of positions for y coordinates
        Return: nothing
        '''
        self.positions_x = positions_x
        self.positions_y = positions_y
        #drawing white circles
        turtle.goto(self.initial_x+50,self.initial_y+10)
        for i in range(0,rows+1):
            for j in range(0,columns):

                turtle.color(BOARD_CIRCLE_COLOR)
                turtle.begin_fill()
                turtle.hideturtle()
                turtle.circle(33)
                turtle.end_fill()
                turtle.forward(75)
            
            turtle.goto(self.initial_x+50,self.positions_y[i])

        #drawing arrows
        turtle.goto(self.initial_x+30,self.positions_y[-1])
        for j in range(0,columns):
            turtle.color("black")
            turtle.begin_fill()
            turtle.forward(30)
            turtle.right(120)
            turtle.forward(30)
            turtle.right(120)
            turtle.forward(30)
            turtle.end_fill()
            turtle.right(120)
            turtle.forward(76)

            

        return


    def color_turns(self,turn,recent_fill,positions_x,positions_y):
        '''
        Method --  coloring turn
        Parameters:
            self -- the current object
            turn -- number indicating who played the current turn, an integer
            recent_fill -- list with row and column number for circle to fill
            positions_x -- list of positions for x coordinates
            positions_y -- list of positions for y coordinates
        Return: nothing
        '''
        self.positions_x = positions_x
        self.positions_y = positions_y

        if turn == 2:
            color = PLAYER_1_COLOR
            turtle.speed(0)
        elif turn == 5:
            turtle.speed(10)
            color = COMPUTER_COLOR
            
        x_coor = recent_fill[1]

        y_coor = recent_fill[0]

        turtle.goto(positions_x[x_coor]+50-18,positions_y[y_coor])
        turtle.color(color)
        turtle.begin_fill()
        turtle.hideturtle()
        turtle.circle(33)
        turtle.end_fill()
        turtle.penup()


    def display_scores(self,red_score,yellow_score):
        '''
        Method --  displaying scores
        Parameters:
            self -- the current object
            red_score -- current score of red player, an integer
            yellow_score -- current score of yellow player, an integer
        Return: nothing
        '''
        red_score = str(red_score)
        yellow_score = str(yellow_score)
        
        turtle.penup()
        turtle.goto(self.positions_x[1] - 15,self.positions_y[self.rows + 1] + 30)
        turtle.color("black")
        turtle.write("Red/Player Score: \n\t"+red_score, \
                     align="left", font = ("Arial",10,"bold"))
        turtle.goto(self.positions_x[3] - 20,self.positions_y[self.rows+1]+30)
        turtle.write("Yellow/Comp. Score:\n\t "+yellow_score,\
                     align="left", font = ("Arial",10,"bold"))
        
        self.whose_turn(2)        



    def whose_turn(self,turn):
        '''
        Method --  whose turn
        Parameters:
            self -- the current object
            turn -- number indicating who is supposed to play next, an integer
        Return: nothing
        '''
        #clearing text before changing turns
        turtle.penup()
        turtle.goto(self.positions_x[0]-150,self.positions_y[-4])
        turtle.color("white")
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(110)
            turtle.left(90)
            turtle.forward(25)
            turtle.left(90)
        turtle.end_fill()
        
        if turn == 2:
            turn_color = PLAYER_1_COLOR
            turn_text = "Player's Turn"
            turtle.speed(0)
        elif turn == 5:
            turn_color = COMPUTER_COLOR
            turn_text = "Computer's Turn"
            turtle.speed(0)

        #drawing circle indicating player or computer
        turtle.penup()
        turtle.goto(self.positions_x[0] - 100,self.positions_y[-5])
        turtle.color(turn_color)
        turtle.pendown()
        turtle.begin_fill()
        turtle.hideturtle()
        turtle.circle(33)
        turtle.end_fill()
        turtle.penup()

        #written text part
        turtle.goto(self.positions_x[0] - 150,self.positions_y[-4])
        turtle.pendown()
        turtle.color("black")
        turtle.write(turn_text,align="left",font = ("Arial",10,"bold"))
        turtle.penup()


    def winner_display(self,winner):
        '''
        Method --  winner display
        Parameters:
            self -- the current object
            winner -- an integer indicating who won the game
        Return: nothing
        '''
        turtle.speed(2)
        turtle.penup()
        turtle.goto(0,0)
        turtle.bgcolor("black")
        turtle.screensize(300,300)
        turtle.clear()
        turtle.penup()
        turtle.goto(-70,0)
        turtle.color("white")
        turtle.speed(6)
        
        if winner == 2:
            written = "Player Won!!!"

        elif winner == 5:
            written = "Computer Won!!!"
            
        else:
            written = "It's a Draw!!!"

        turtle.write(written,font=("Arial",20,"bold"))
        
        #slowing down before quitting
        turtle.speed(1)
        turtle.penup()
        turtle.goto(200,200)
        sys.exit()
        turtle.bye()

    #function for A+
    def text_A(self,x_coor,y_coor,again):
        '''
        Method --  text for A+ attempt
        Parameters:
            self -- the current object
            x_coor -- x coordinate, an integer
            y_coor -- y coordinate, an integer
            again -- which player will play again, an integer
        Return: nothing
        '''
        turtle.speed(10)
        
        turtle.goto(x_coor,y_coor)
        
        if again == 2:
            again_text = "You are lucky! Play again!"
        elif again == 5:
            again_text = "Computer is lucky! It goes again!"

        if again == 0:
            #clearing again text
            turtle.penup()
            turtle.goto(x_coor,y_coor-40)
            turtle.color("white")
            turtle.begin_fill()
            for i in range(2):
                turtle.forward(300)
                turtle.left(90)
                turtle.forward(25)
                turtle.left(90)
            turtle.end_fill()
        else:
            turtle.goto(x_coor,y_coor-30)
            turtle.pendown()
            turtle.color("black")
            turtle.write(again_text,align="left",font = ("Arial",11,"bold"))
            turtle.penup()
            
        
        
    
                
            

     
