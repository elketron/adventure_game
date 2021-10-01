"""
map class

min width = 50
min height = 50
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import List

from Buffer import Buffer

@dataclass
class Area:
    id: int
    area_str: List[List[str]]

    def write_to_buf(self, b:Buffer):
        b.clear_buf()
        for i in range(0, len(self.area_str)):
            text = ''.join(self.area_str[i])
            b.add_to_buf(1,i + 1,text)

@dataclass
class Map ():
    width:  int
    height: int
    map:    List[Area]
    name:   str
