import pandas as pd
from CaseTwo import CaseTwo


def extract():
    return pd.read_csv('resources/airbnb.csv', sep=',')


if __name__ == '__main__':
    case_two = CaseTwo(extract())
    case_two.transform()
