from Board import Board
from Map import *

area1 = Area(1, [["Hello this is area 1"],["Hello this is area 1"]])
area2 = Area(2, [["Hello this is area 2"]])

if __name__ == '__main__':
    board = Board()
    map = Map(
        board.main_screen.buffer_size["col"],
        board.main_screen.buffer_size["lines"],
        [area1,area2], "Map 1"
              )
    text = ""
    while True:
        map.map[0].write_to_buf(board.main_screen)
        board.draw()
        text = input("Give greeting: ")
        map.map[1].write_to_buf(board.main_screen)
        board.draw()
        text = input("Give greeting: ")
