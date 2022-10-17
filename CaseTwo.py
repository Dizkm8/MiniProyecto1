from typing import Final
import pandas as pd
import openpyxl


# to_excel() function working https://datatofish.com/export-dataframe-to-excel/
# the rest of methods: https://aprendeconalf.es/docencia/python/manual/pandas/#eliminar-columnas-de-un-dataframe
# insert Columns function https://www.geeksforgeeks.org/python-pandas-dataframe-insert/

class CaseTwo:
    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.room_id_roberto = 97503
        self.room_id_clara = 90387

    def transform(self):
        self.data_frame = self.data_frame[(self.data_frame['room_id'] == self.room_id_roberto) |
                                          (self.data_frame['room_id'] == self.room_id_clara)]
        for i in ['host_id', 'room_type', 'neighborhood', 'accommodates', 'bedrooms', 'price']:
            del self.data_frame[i]
        self.data_frame.insert(0, 'Dueño', ['Clara', 'Roberto'], allow_duplicates=False)
        self.data_frame = self.data_frame.rename(columns={'room_id': 'ID habitación', 'reviews': 'Cantidad reseñas',
                                                          'overall_satisfaction': 'Puntuación (0 a 5)'})

    def load(self):
        self.data_frame.to_excel('Roberto.xlsx', sheet_name='Roberto', index=False, header=True)
