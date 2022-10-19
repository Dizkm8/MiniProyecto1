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

    def start(self):
        """
        Starts the process to solve case two
        :return: None
        """
        self.transform()
        self.load()

    def get_roberto_and_clara_information(self, roberto_and_clara_data_frame):
        for index in roberto_and_clara_data_frame.index:
            if index == 0:
                self.data_dict['Puntuación general airbnb de Clara: '] = roberto_and_clara_data_frame[
                    'overall_satisfaction'][index]
                self.data_dict['Cantidad reseñas airbnb de Clara: '] = roberto_and_clara_data_frame['reviews'][index]
                self.data_dict['Precio por noche airbnb de Clara: '] = roberto_and_clara_data_frame['price'][index]
            elif index == 1:
                self.data_dict['Puntuación general airbnb de Roberto: '] = roberto_and_clara_data_frame[
                    'overall_satisfaction'][index]
                self.data_dict['Cantidad reseñas airbnb de Roberto: '] = roberto_and_clara_data_frame['reviews'][index]
                self.data_dict['Precio por noche airbnb de Roberto: '] = roberto_and_clara_data_frame['price'][index]

    def transform(self):
        """
        Transform initial data to Dataframe with only Roberto and Clara Dataframe rows
        :return: None
        """
        roberto_and_clara_data_frame = self.initial_data[(self.initial_data['room_id'] == self.room_id_roberto) |
                                                         (self.initial_data['room_id'] == self.room_id_clara)]
        roberto_and_clara_data_frame = roberto_and_clara_data_frame.reset_index(level=None, drop=True)
        self.transform_for_zone(roberto_and_clara_data_frame)
        self.get_roberto_and_clara_information(roberto_and_clara_data_frame)

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
                self.get_price_by_zone([neighbors[0]], ['Roberto y Clara'])
                return
            self.get_opinions_by_zone(neighbors, ['Clara', 'Roberto'])
            self.get_guests_amount_by_zone(neighbors, ['Clara', 'Roberto'])
            self.get_price_by_zone(neighbors, ['Clara', 'Roberto'])
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

    def get_guests_amount_by_zone(self, neighbors, names):
        """
        Gets the average reviews (or guests) by Roberto and clara airbnb zone
        :param neighbors: Neighbors of each airbnb
        :param names: Name of owner of airbnb (Roberto or Clara)
        :return: None
        """
        airbnb_average_overall_satisfaction_by_zone = []
        for neighbor in neighbors:
            airbnb_average_overall_satisfaction_by_zone.append(
                round(self.initial_data[self.initial_data['neighborhood'] == neighbor].iloc[:, 4].mean(skipna=True)))
        for i in range(len(names)):
            self.data_dict['Reseñas promedio de los airbnb de la zona de ' + names[i]] \
                = airbnb_average_overall_satisfaction_by_zone[i]

    def get_price_by_zone(self, neighbors, names):
        """
        Gets the average opinions of airbnb with similar prices
        :return: None
        """
        average_price_by_zone = []
        for neighbor in neighbors:
            average_price_by_zone.append(
                round(self.initial_data[self.initial_data['neighborhood'] == neighbor].iloc[:, 8].mean(skipna=True), 1))
        for i in range(len(names)):
            self.data_dict['Precio promedio de los airbnb de la zona de ' + names[i]] \
                = average_price_by_zone[i]

    def load(self):
        """
        Loads the class data into out excel called Roberto
        :return: None
        """
        pd.DataFrame.from_dict(self.data_dict, orient='index').to_excel('Roberto.xlsx', sheet_name='Roberto',
                                                                        index=True, header=False)
