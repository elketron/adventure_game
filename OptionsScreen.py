"""
options screen class
"""
from Buffer import Buffer

class Options(Buffer):
    def __init__(self):
        super().__init__(0.55, 0.4)
        self.Title = " Options "

        self.set_border()
        self.title(self.Title)

