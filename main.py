import pandas as pd
from CaseOne import CaseOne

global data_frame


def extract():
    return pd.read_csv('resources/airbnb.csv', sep=',')


def solve_case_one():
    case_one = CaseOne(data_frame)
    case_one.order()
    print("Caso 1 realizado con éxito, información desplegada en Resultado.xlsx")


if __name__ == '__main__':
    data_frame = extract()
    solve_case_one()
