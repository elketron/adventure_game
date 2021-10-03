from Buffer import Buffer
from Map import *

class MainScreen (Buffer):
    def __init__ (self):
        super().__init__(0.4,1)
        self.Title = " Main "

        self.set_border()
        self.title(self.Title)
        self.map1 = Map()

    def load_map(self):
        ar = Area()
        for i in range(0,2):
            with open(f"Areas/{i}", "r") as area:
                tem = area.readlines()
                
                ar.id = int(tem[0].strip())
                ar.name = tem[1].strip()
                ar.contents = [tem[i].strip() for i in range(2,6)]
                ar.area_str = [tem[i].rstrip() for i in range(6,len(tem))]

                self.map1.set_map(ar)

        
