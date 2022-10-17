import pandas as pd
from CaseTwo import CaseTwo
from CaseThree import CaseThree

global data_frame


def extract():
    return pd.read_csv('resources/airbnb.csv', sep=',')


def solve_case_two():
    case_two = CaseTwo(data_frame)
    case_two.transform()
    case_two.load()
    print("Caso 2 realizado con éxito, información desplegada en Roberto.xlsx")


def solve_case_three():
    case_three = CaseThree(data_frame)
    case_three.transform()
    case_three.load()
    print("Caso 3 realizado con éxito, información desplegada en Diana.xlsx")


if __name__ == '__main__':
    data_frame = extract()
    solve_case_two()
    solve_case_three()
