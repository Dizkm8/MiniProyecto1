import pandas as pd
import openpyxl


class CaseTwo:
    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.room_id_roberto = 97503
        self.room_id_clara = 90387

    def transform(self):
        roberto_clara_data_frame = self.data_frame[(self.data_frame['room_id'] == self.room_id_roberto) |
                                                   (self.data_frame['room_id'] == self.room_id_clara)]
        neighbors = roberto_clara_data_frame['neighborhood'].drop_duplicates().array
        self.get_opinions_by_zone(neighbors)

    def get_opinions_by_zone(self, neighbors):
        airbnb_average_overall_satisfaction_by_zone = []
        for neighbor in neighbors:
            airbnb_average_overall_satisfaction_by_zone.append(
                round(self.data_frame[self.data_frame['neighborhood'] == neighbor].iloc[:, 5].mean(skipna=True), 1))
        self.data_frame.to_excel('Roberto.xlsx', sheet_name='Roberto', index=False, header=True)
        serie = pd.Series
        for neighbor in neighbors:
            serie = pd.Series(data=airbnb_average_overall_satisfaction_by_zone[0],
                              index=[('Promedio Zona: ' + neighbor)])
        serie.to_excel('Roberto.xlsx', sheet_name='Roberto1', index=False, header=True)

    def load(self):
        with pd.ExcelWriter('Roberto.xlsx', mode='a') as writer:
            self.data_frame.to_excel(writer, sheet_name='Roberto', index=False, header=True)
