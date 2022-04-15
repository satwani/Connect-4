'''testing'''

import unittest
import os
from game import Game
from win import Win



class GameTest(unittest.TestCase):
    def test_init(self):
        game = Game(4, 8, 100, 50,"red.txt","yellow.txt")
        self.assertEqual(game.rows, 4)
        self.assertEqual(game.columns, 8)
        self.assertEqual(game.initial_x, 100)
        self.assertEqual(game.initial_y, 50)
        self.assertEqual(game.y_positions,[])
        self.assertEqual(game.x_positions,[])
        self.assertEqual(game.player_value,2)
        self.assertEqual(game.computer_value,5)

    def test_column_count(self):
        game = Game(2, 3, 100, 50,"red.txt","yellow.txt")
        game.column_count(3)
        self.assertEqual(game.dict,{0:0, 1:0, 2:0, 3:0})

    def test_position_slots_x(self):
        game = Game(2, 3, 10, 20,"blue.txt","white.txt")
        game.position_slots_x()
        self.assertEqual(game.x_positions,[28, 103, 178, 253])

    def test_position_slots_y(self):
        game = Game(1, 5, 60, 40,"pink.txt","orange.txt")
        game.position_slots_y()
        self.assertEqual(game.y_positions,[50, 120, 190])

    def test_initial_empty_panel(self):
        game = Game(2, 3, 460, 430,"pink.txt","orange.txt")
        game.initial_empty_panel(2, 3)
        self.assertEqual(game.updated_panel,[[0, 0, 0], [0, 0, 0]])
        
        

class WinTest(unittest.TestCase):
    def test_init(self):
        win = Win(15, 47, -400, -150,"purple.txt","grey.txt")
        self.assertEqual(win.rows, 15)
        self.assertEqual(win.columns, 47)
        self.assertEqual(win.initial_x, -400)
        self.assertEqual(win.initial_y, -150)
        self.assertEqual(win.red_score, 0)
        self.assertEqual(win.yellow_score, 0)
        self.assertEqual(win.red_file_name, "purple.txt")
        self.assertEqual(win.yellow_file_name, "grey.txt")

    def test_initialize_red(self):
        win = Win(4, 5, 30, 50,"nofile.txt","HDMI.txt")
        
        if os.path.exists('nofile.txt'):
            os.remove('nofile.txt')
        win.initialize_red()
        self.assertEqual(win.red_score,0)

    def test_initialize_yellow(self):
        win = Win(67, 87, 17, 42,"nofile.txt","deep.txt")
        
        if os.path.exists('deep.txt'):
            os.remove('deep.txt')
            
        win.initialize_yellow()
        self.assertEqual(win.yellow_score,0)

    def test_update_score(self):
        win = Win(67, 87, 17, 202,"rubric.txt","document.txt")

        if os.path.exists('rubric.txt'):
            os.remove('rubric.txt')
        
        win.update_score("32","rubric.txt")

        with open("rubric.txt", "r") as infile:
            test_score = int(infile.read().strip())
            
        self.assertEqual(test_score,32)
            
    def test_no_win(self):
        win = Win(300, 2, 518, 387,"color.txt","line.txt")

        win.no_win([[43, 89, 42],[54, 67]])
        self.assertEqual(win.winner,0)

        win.no_win([[43, 0, 42],[54, 67]])
        self.assertEqual(win.winner, 1)

    def test_horizontal_win(self):
        win = Win(200, 29, 8, 7,"lor.txt","display.txt")
        four_by_four = [[0] * 4 for i in range(4)]
        four_by_four[0] = [6]*4
        win.horizontal_win(four_by_four,[-1, 4],6)
        self.assertEqual(win.winner, 6)

    def test_vertical_win(self):
        win = Win(1, 2, 85, 43,"pirates.txt","explain.txt")
        four_by_four = [[0] * 4 for i in range(4)]
        for i in range(len(four_by_four)):
            four_by_four[i][0] = 18
        win.vertical_win(four_by_four, [0, 0], 18)
        self.assertEqual(win.winner, 18)

    def test_diagonal_win_right(self):
        win = Win(13, 61, 185, 403,"pirates.txt","explain.txt")
        four_by_four = [[0] * 4 for i in range(4)]
        for i in range(len(four_by_four)):
                four_by_four[i][3 - i] = 7
        win.diagonal_win_right(four_by_four, 4, 4, 7)
        self.assertEqual(win.winner, 7)

    def test_diagonal_win_left(self):
        win = Win(13, 61, 185, 403,"pirates.txt","explain.txt")
        four_by_four = [[0] * 4 for i in range(4)]
        for i in range(len(four_by_four)):
                four_by_four[i][i] = 7
        win.diagonal_win_left(four_by_four, 4, 4, 7)
        self.assertEqual(win.winner, 7)
        
    

def main():

    unittest.main(verbosity = 3)
    
main()
    
