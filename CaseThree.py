import pandas as pd
import openpyxl


class CaseThree:
    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.price = 50
        self.room_type = "Shared room"
        self.first_rows = 10
        self.sortby = ['overall_satisfaction', 'reviews']

    def transform(self):
        self.data_frame = self.data_frame[
            (self.data_frame['price'] <= self.price) & (self.data_frame['room_type'] == self.room_type)].sort_values(
            by=self.sortby, ascending=False).head(self.first_rows)

    def load(self):
        self.data_frame.to_excel('Diana.xlsx', sheet_name='Diana', index=False, header=True)