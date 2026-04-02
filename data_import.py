import numpy as np
import pandas as pd
from find_v0 import *
from change_of_speed import *
from export_cars_to_csv import *
from car_v_derivative import *

pd.set_option('display.max_rows', 1000)
chosen_columns = ['Vehicle_ID', 'Frame_ID', 'Preceeding', 'Following', 'v_Vel', "v_Acc"]
#df = pd.read_csv('data_750_805.csv', usecols=chosen_columns)
df2 = pd.read_csv('test.csv', usecols=chosen_columns)

#export_cars(df, (4, 6, 14, 18, 31, 34, 40, 44))
print(calculte_car_v_derivative(df2, 4))