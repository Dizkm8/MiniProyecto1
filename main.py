import pandas as pd
from CaseOne import CaseOne
from CaseTwo import CaseTwo
from CaseThree import CaseThree

global data_frame


def extract():
    """
    Reads the data file
    :return: File procesed into DataFrame or None if IOError is caught
    """
    try:
        return pd.read_csv('resources/airbnb.csv', sep=',')
    except IOError as e:
        print("Corrupted!", e)
        return None


def solve_cases():
    """
    Call all the cases solve methods
    :return: None
    """
    solve_case_one()
    solve_case_two()
    solve_case_three()


def solve_case_one():
    """
    Initialize and start case one to solver
    :return: None
    """
    case_one = CaseOne(data_frame)
    case_one.start()
    print("Case 1 completed successfully, result on Results.xlsx")


def solve_case_two():
    """
    Initialize and start case two solver
    :return: None
    """
    case_two = CaseTwo(data_frame)
    case_two.start()
    print("Case 2 completed successfully, result on en Roberto.xlsx")


def solve_case_three():
    """
    Initialize and start case three to solver
    :return: None
    """
    case_three = CaseThree(data_frame)
    case_three.start()
    print("Case 3 completed successfully, result on Diana.xlsx")


if __name__ == '__main__':
    data_frame = extract()
    if data_frame is not None:
        solve_cases()
