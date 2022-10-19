import pandas as pd
import openpyxl


class CaseTwo:
    def __init__(self, data_frame):
        """
        Constructor of the CaseTwo class
        :param data_frame: Dataframe with initial data to analyze.
        """
        self.data_dict = dict()
        self.initial_data = data_frame
        self.room_id_clara = 90387
        self.room_id_roberto = 97503

    def transform(self):
        """
        Transform initial data to Dataframe with only Roberto and Clara Dataframe rows
        :return: None
        """
        roberto_and_clara_data_frame = self.initial_data[(self.initial_data['room_id'] == self.room_id_roberto) |
                                                         (self.initial_data['room_id'] == self.room_id_clara)]
        roberto_and_clara_data_frame = roberto_and_clara_data_frame.set_index("room_id").reset_index(
            level=None, drop=True)
        self.transform_for_zone(roberto_and_clara_data_frame)
        self.get_opinions_by_price()
        print(self.data_dict)

    def transform_for_zone(self, roberto_and_clara_data_frame):
        """
        Transforms Roberto and Clara dataframe to get information by airbnb zone
        :param roberto_and_clara_data_frame: Roberto and Clara only Dataframe
        :return: None
        """
        neighbors = []
        for index in roberto_and_clara_data_frame.index:
            neighbors.append(roberto_and_clara_data_frame['neighborhood'][index])
        if len(neighbors) == 2:
            if neighbors[0] == neighbors[1]:
                self.get_opinions_by_zone([neighbors[0]], ['Roberto y Clara'])
                self.get_guests_amount_by_zone([neighbors[0]], ['Roberto y Clara'])
                return
            self.get_opinions_by_zone(neighbors, ['Clara', 'Roberto'])
            self.get_guests_amount_by_zone(neighbors, ['Clara', 'Roberto'])
            return

    def get_opinions_by_zone(self, neighbors, names):
        """
        Gets the average opinions by Roberto and clara airbnb zone
        :param neighbors: Neighbors of each airbnb
        :param names: Name of owner of airbnb (Roberto or Clara)
        :return: None
        """
        airbnb_average_overall_satisfaction_by_zone = []
        for neighbor in neighbors:
            airbnb_average_overall_satisfaction_by_zone.append(
                round(self.initial_data[self.initial_data['neighborhood'] == neighbor].iloc[:, 5].mean(skipna=True), 1))
        for i in range(len(names)):
            self.data_dict['Puntuación promedio de los airbnb de la zona de ' + names[i]] \
                = airbnb_average_overall_satisfaction_by_zone[i]

    def get_opinions_by_price(self):
        """
        Gets the average price of all airbnb
        :return: None
        """
        prices_sum = 0
        rows_amount = 0
        for index in self.initial_data.index:
            price = self.initial_data['price'][index]
            if price > 1000 and index < 2500:
                price /= 30
            rows_amount += 1
            prices_sum += price
        if rows_amount == 0:
            return
        self.data_dict['Promedio de precio todos los airbnb'] = round(prices_sum / rows_amount, 1)

    def get_guests_amount_by_zone(self, neighbors, names):
        airbnb_average_overall_satisfaction_by_zone = []
        for neighbor in neighbors:
            airbnb_average_overall_satisfaction_by_zone.append(
                round(self.initial_data[self.initial_data['neighborhood'] == neighbor].iloc[:, 4].mean(skipna=True)))
        for i in range(len(names)):
            self.data_dict['Reseñas promedio de los airbnb de la zona de ' + names[i]] \
                = airbnb_average_overall_satisfaction_by_zone[i]

    def load(self):
        """
        with pd.ExcelWriter('Roberto.xlsx', mode='a') as writer:
            self.data_frame.to_excel(writer, sheet_name='Roberto', index=False, header=True)
        """
        pass
