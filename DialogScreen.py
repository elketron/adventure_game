"""
the dialog screen class
"""

from Buffer import Buffer

class Dialog(Buffer):
    def __init__(self):
        super().__init__(0.55, 0.6)
        self.Title = " Dialog "
        self.set_border()
        self.title(self.Title)
        self.dialog = []

