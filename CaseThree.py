import pandas as pd
import openpyxl


class CaseThree:
    def __init__(self, data_frame):
        """
        Constructor of the CaseThree class.
        :param data_frame: 2-dimensional labeled data structure to analize.
        """
        self.data_frame = data_frame

    def start(self):
        """
        Starts the process to solve case three
        :return: None
        """
        self.filter(20, "Shared room")
        self.sort(['overall_satisfaction', 'reviews'])
        self.first_selected_rows(10)
        self.write_excel('Diana.xlsx', 'Diana')

    def filter(self, max_price, room_type):
        """
        Filter the data frame based on the maximum price per night and the type of room
        :param max_price: Maximum price per night
        :param room_type: Type of room
        :return: None
        """
        self.data_frame = self.data_frame[(self.data_frame['price'] <= max_price) &
                                          (self.data_frame['room_type'] == room_type)]

    def sort(self, sort_by):
        """
        Sorts the data frame in descending order by columns
        :param sort_by: list of column names to sort
        :return: None
        """
        self.data_frame = self.data_frame.sort_values(by=sort_by, ascending=False)

    def first_selected_rows(self, rows):
        """
        Select the first rows
        :param rows: Number of rows to consider
        :return: None
        """
        self.data_frame = self.data_frame.head(rows)

    def write_excel(self, excel_file, sheet_name):
        """
        Write an Excel file from the dataframe. File does not write row position
        :param excel_file: Excel file name
        :param sheet_name: Sheet name
        :return: None
        """
        self.data_frame.to_excel(excel_file, sheet_name=sheet_name, index=False)