from Board import Board

if __name__ == '__main__':
    board = Board()
    text = ""
    while True:
        board.add_to_buf(2,2,text)
        board.draw()
        text = input("Give greeting: ")
