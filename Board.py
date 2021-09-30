"""
the board class

makes a game board 
"""
import os
from Buffer import Buffer
from MainScreen import MainScreen
from DialogScreen import Dialog
from OptionsScreen import Options

class Board (Buffer):

    def __init__(self):
        Buffer.__init__(self,1,1)
        self.main_screen = MainScreen()
        self.dialog_screen = Dialog()
        self.options_screen = Options()

    def draw(self):
        os.system(self.clear)
        self.buffer_join(self.main_screen, 0, 0)
        
        self.buffer_join(self.dialog_screen, self.main_screen.buffer_size["lines"], 0)
        self.buffer_join(self.options_screen, self.main_screen.buffer_size["lines"], self.dialog_screen.buffer_size["col"])
        for i in range(0, self.term_size.lines - 1):
            print(''.join(self.Buffer[i]))
