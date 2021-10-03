"""
map class

min width = 50
min height = 50
"""
from __future__ import annotations
from typing import List

from Buffer import Buffer

class Area:
    def __init__(self):
        self.id: int
        self.name: str 
        self.contents: List
        self.area_str: List[str]
        

    def write_to_buf(self, b:Buffer):
        b.clear_buf()
        for i in range(0, len(self.area_str)):
            text = ''.join(self.area_str[i])
            b.add_to_buf(1,i + 1,text)

class Map ():
    def __init__(self):
        self.width:  int
        self.height: int
        self.map:    List[Area] = []
        self.name:   str

    def set_map(self,ar: Area):
        self.map.append(ar)
