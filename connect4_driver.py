'''Karan Satwani
   CS 5001
   Project
   Driver file
'''
import turtle
import random
from game import Game
from win import Win
from draw import Turtle_connect

INITIAL_X = -300 
INITIAL_Y = -250
RED_SCORE = "red_scores.txt"
YELLOW_SCORE = "yellow_scores.txt"

def menu(rows,columns):
    '''name: menu
       parameters: rows and columns (integers)
       returns: nothing
    '''
    #calling Turtle_connect class
    turtle_draw = Turtle_connect(rows,columns,INITIAL_X,INITIAL_Y)
    
 
    #calling Game class
    game = Game(rows, columns, INITIAL_X, INITIAL_Y, RED_SCORE, YELLOW_SCORE)
    empty_panel = game.initial_empty_panel(rows, columns)
    positions_y = game.position_slots_y()
    positions_x = game.position_slots_x()

    #calling Win class
    win = Win(rows,columns, INITIAL_X, INITIAL_Y, RED_SCORE, YELLOW_SCORE)
    red_score = win.initialize_red()
    yellow_score = win.initialize_yellow()



    #pre-game setup: drawing board, empty circles, arrows and displaying scores
    turtle_draw.draw_board(rows,columns)
    turtle_draw.circles_and_arrows(rows,columns,\
                                   positions_x,positions_y) 
    turtle_draw.display_scores(red_score,yellow_score) 
    
    #this goes to player turn
    turtle.onscreenclick(game.click_column)


def main():
    
    answer = input("Let's play Connect 4.\n\tEnter 1 for default 6x7 grid:\n"\
                   "\tEnter anything else for manual inputs:\n")
    if answer == "1":
        rows = 6
        columns = 7
        menu(rows,columns)
    
    else:

        rows = input("Please enter the number of ROWS between 4 and 9:\n")
        columns = input("Please enter the number of COLUMNS between 4 and 9:\n")

        while True:
            try:
                rows = int(rows)
                columns = int(columns)
                if rows >= 4 and rows <= 9 and columns >= 4 and columns <= 9:
                    menu(rows,columns)
                    break
                else:
                    print("Not valid numbers")
                    rows = input("Please enter the number of ROWS between 4 and 9:\n")
                    columns = input("Please enter the number of COLUMNS between 4 and 9:\n")
                    
            except:
                print("Not valid inputs")
                rows = input("Please enter the number of ROWS between 4 and 9:\n")
                columns = input("Please enter the number of COLUMNS between 4 and 9:\n")



    



    
    


main()
