from typing import Final
import pandas as pd


class CaseTwo:
    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.room_id_roberto = 97503
        self.room_id_clara = 90387

    def transform(self):
        self.data_frame = self.data_frame[(self.data_frame['room_id'] == self.room_id_roberto) |
                                          (self.data_frame['room_id'] == self.room_id_clara)]

    def load(self):

        pass
