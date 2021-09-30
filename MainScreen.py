from Buffer import Buffer

class MainScreen (Buffer):
    def __init__ (self):
        super().__init__(0.4,1)
        self.Title = " Main "

        self.set_border()
        self.title(self.Title)
