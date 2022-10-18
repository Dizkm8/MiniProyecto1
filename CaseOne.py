class CaseOne:

    def __init__(self, data_frame):
        """
        Class CaseOne constructor.
        :param data_frame: Data from airbnb.csv.
        """
        self.data_frame = data_frame

    def filter(self):
        """
        Method that filters the data table as required.
        :return: Filtered data table.
        """
        # Only reviews greater than 10.
        critics = self.data_frame[self.data_frame['reviews'] > 10]

        # Rating greater than four stars.
        four_stars = critics[critics['overall_satisfaction'] >= 4]

        # Only 2 rooms.
        final_table = four_stars[four_stars['bedrooms'] == 2]

        return final_table

    def order(self):
        """
        Method that sorts the table data in descending order based on reviews and rating.
        :return: Table with sorted data.
        """
        # It is ordered in descending order taking into account the reviews and criticisms.
        sorted_table = self.filter().sort_values(['overall_satisfaction', 'reviews'], ascending=False)
        new_table = sorted_table.reset_index(level=None, drop=True)
        new_table.to_excel('Result.xlsx', index=True, header=True)
