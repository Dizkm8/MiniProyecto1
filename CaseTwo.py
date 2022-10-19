import pandas as pd
import openpyxl


class CaseTwo:
    def __init__(self, data_frame):
        self.data_frame = None
        self.initial_data = data_frame
        self.room_id_roberto = 97503
        self.room_id_clara = 90387

    def transform(self):
        neighbors = []
        names = []
        roberto_data_frame = self.initial_data[(self.initial_data['room_id'] == self.room_id_roberto)]
        clara_data_frame = self.initial_data[(self.initial_data['room_id'] == self.room_id_clara)]
        roberto_data_frame = roberto_data_frame.set_index("room_id")
        clara_data_frame = clara_data_frame.set_index("room_id")
        if roberto_data_frame.shape[0] > 0:
            neighbors.append(roberto_data_frame.iloc[0, 2])
            names.append('Roberto')
        if clara_data_frame.shape[0] > 0:
            neighbors.append(clara_data_frame.iloc[0, 2])
            names.append('Clara')
        if len(neighbors) == 2:
            if neighbors[0] == neighbors[1]:
                self.get_opinions_by_zone([neighbors[0]], names)
                return
        self.get_opinions_by_zone(neighbors, names)

    def get_opinions_by_zone(self, neighbors, names):
        airbnb_average_overall_satisfaction_by_zone = []
        for neighbor in neighbors:
            airbnb_average_overall_satisfaction_by_zone.append(
                round(self.initial_data[self.initial_data['neighborhood'] == neighbor].iloc[:, 5].mean(skipna=True), 1))
        self.initial_data.to_excel('Roberto.xlsx', sheet_name='Roberto', index=False, header=True)
        # df = pd.DataFrame([['María', 18], ['Luis', 22], ['Carmen', 20]], columns=['Nombre', 'Edad'])
        print(airbnb_average_overall_satisfaction_by_zone)
        self.data_frame = pd.DataFrame(columns=['Dueño', 'Puntuación general airbnb de la zona'])
        # for i in range(len(neighbors)):
        # new_row = {'name': 'Geo', 'physics': 87, 'chemistry': 92, 'algebra': 97}
        # append row to the dataframe
        # df_marks = df_marks.append(new_row, ignore_index=True)
        # new_row = {''}
        """        for i in range(len(neighbors)):
            serie = pd.Series(data=airbnb_average_overall_satisfaction_by_zone[i],
                              index=[('Promedio Zona: ' + neighbors[i])])
        serie.to_excel('Roberto.xlsx', sheet_name='Roberto1', index=False, header=True)"""

    def load(self):
        """
        with pd.ExcelWriter('Roberto.xlsx', mode='a') as writer:
            self.data_frame.to_excel(writer, sheet_name='Roberto', index=False, header=True)
        """
        pass
