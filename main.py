from Board import Board
from Map import *


if __name__ == '__main__':
    board = Board()
    board.main_screen.load_map()

    board.main_screen.map1.map[1].write_to_buf(board.main_screen)

    board.dialog_screen.load_dialogs()
    while True:
        
        board.draw()
        input()
