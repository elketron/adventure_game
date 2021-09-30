"""
the buffer class makes a buffer and has its functions
"""
from __future__ import annotations
import os

class Buffer ():
    clear = 'cls' if os.name == 'nt' else 'clear'
    
    def __init__(self, height: float, width: float):
        self.border_chars = ["┌", "─", "┐", "└", "┘", "│"]
        self.term_size = os.get_terminal_size()
        self.buffer_size = {"col": int(round(self.term_size.columns * width,0)), 
                            "lines": int(round(self.term_size.lines * height,0)) }
        self.Buffer = [ [" "] * self.buffer_size["col"] for _ in range(self.buffer_size["lines"])]

    def clear_buf(self):
        self.Buffer = [ [" "] * self.buffer_size["col"] for _ in range(self.buffer_size["lines"])]
        self.set_border()

    def set_border(self):
        # top border
        self.Buffer[0][0] = self.border_chars[0]
        for i in range(1, self.buffer_size["col"] - 1):
            self.Buffer[0][i] = self.border_chars[1]
        self.Buffer[0][self.buffer_size["col"] - 1] = self.border_chars[2]
    
        # side borders 
        for i in range(1, self.buffer_size["lines"] - 1):
            self.Buffer[i][0] = self.border_chars[5]
    
        for i in range(1,self.buffer_size["lines"] - 1):
            self.Buffer[i][self.buffer_size["col"] - 1] = self.border_chars[5]

        # bottom border
        self.Buffer[self.buffer_size["lines"] - 1][0] = self.border_chars[3]
        for i in range(1, self.buffer_size["col"] - 1):
            self.Buffer[self.buffer_size["lines"] - 1][i] = self.border_chars[1]
        self.Buffer[self.buffer_size["lines"] - 1][self.buffer_size["col"] - 1] = self.border_chars[4]

    def title(self, title:str):
        self.add_to_buf(1, 0, title)

    def add_to_buf(self, x:int, y:int, text:str ):
        offsety = 0
        j = x
        for i in range(0, len(text)):
            if j >= self.buffer_size["col"] - x:
                offsety += 1
                j = x
            self.Buffer[y + offsety][x + j] = text[i]
            j += 1

    def buffer_join (self, b:Buffer, offsety:int, offsetx:int):
        for i in range(0, b.buffer_size["lines"]):
            for j in range(0, b.buffer_size["col"]):
                self.Buffer[i + offsety][j + offsetx] = b.Buffer[i][j]
