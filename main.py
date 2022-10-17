import pandas as pd
from CaseTwo import CaseTwo

data_frame = pd.read_csv('resources/airbnb.csv', sep=',')
case_two = CaseTwo(data_frame)

