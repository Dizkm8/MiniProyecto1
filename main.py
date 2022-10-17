import pandas as pd
from CaseTwo import CaseTwo

global data_frame


def extract():
    return pd.read_csv('resources/airbnb.csv', sep=',')


def solve_case_two():
    case_two = CaseTwo(data_frame)
    case_two.transform()
    case_two.load()
    print("Caso 2 realizado con éxito, información desplegada en Roberto.xlsx")


if __name__ == '__main__':
    data_frame = extract()
    solve_case_two()
