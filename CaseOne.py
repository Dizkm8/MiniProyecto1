class CaseOne:

    def __init__(self, data_frame):
        """
        Class CaseOne constructor.
        :param data_frame: Data from airbnb.csv.
        """
        self.data_frame = data_frame

    def filter(self):
        """
        Filters the data table as required.
        :return: Filtered data frame.
        """
        # Only reviews greater than 10.
        critics = self.data_frame[self.data_frame['reviews'] > 10]

        # Rating greater than four stars.
        four_stars = critics[critics['overall_satisfaction'] >= 4]

        # Only 2 rooms.
        only_two_rooms = four_stars[four_stars['bedrooms'] == 2]

        # More than 4 people.
        more_four_people = only_two_rooms[only_two_rooms['accommodates'] >= 4]

        # Only apartments.
        final_table = more_four_people[more_four_people['room_type'] == "Entire home/apt"]

        return final_table

    def order(self):
        """
        Sorts the table data in descending order based on reviews and rating.
        :return: Table with sorted data.
        """
        # It is ordered in descending order taking into account the reviews and criticisms.
        sorted_table = self.filter().sort_values(['overall_satisfaction', 'reviews'], ascending=False)
        new_table = sorted_table.reset_index(level=None, drop=True)
        new_table.to_excel('Results.xlsx', index=True, header=True)
