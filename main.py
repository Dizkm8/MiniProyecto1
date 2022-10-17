import pandas as pd
from CaseTwo import CaseTwo

global data_frame


def extract():
    return pd.read_csv('resources/airbnb.csv', sep=',')


def init_case_two():
    case_two = CaseTwo(data_frame)
    case_two.transform()


if __name__ == '__main__':
    data_frame = extract()
    init_case_two()
