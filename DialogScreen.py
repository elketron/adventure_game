"""
the dialog screen class
"""
import csv

from Buffer import Buffer

class Dialog(Buffer):
    def __init__(self):
        super().__init__(0.55, 0.6)
        self.Title = " Dialog "
        self.seperator = "─" * self.buffer_size["col"]
        self.set_border()
        self.title(self.Title)
        self.files = ["home", "witch"]
        self.dialog = []

    def load_dialogs(self):
        for name in self.files:
            with open(f"Dialogs/{name}.csv", "r") as file:
                csvFile = csv.reader(file)
                self.dialog.append([line for line in csvFile])

        print(self.dialog)

    def set_dialog(self, place:int, id:int):
        self.add_to_buf(1,1,f"{self.dialog[place][id][1]}: {self.dialog[place][id][2]}")


