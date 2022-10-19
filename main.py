import pandas as pd
from CaseOne import CaseOne
from CaseTwo import CaseTwo
from CaseThree import CaseThree

global data_frame


def extract():
    return pd.read_csv('resources/airbnb.csv', sep=',')


def solve_case_one():
    case_one = CaseOne(data_frame)
    case_one.order()
    print("Caso 1 realizado con éxito, información desplegada en Results.xlsx")


def solve_case_two():
    case_two = CaseTwo(data_frame)
    case_two.start()
    print("Caso 2 realizado con éxito, información desplegada en Roberto.xlsx")


def solve_case_three():
    case_three = CaseThree(data_frame)
    case_three.filter(20, "Shared room")
    case_three.sort(['overall_satisfaction', 'reviews'])
    case_three.first_selected_rows(10)
    case_three.write_excel('Diana.xlsx', 'Diana')
    print("Caso 3 realizado con éxito, información desplegada en Diana.xlsx")


if __name__ == '__main__':
    data_frame = extract()
    solve_case_one()
    solve_case_two()
    solve_case_three()
