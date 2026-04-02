import numpy as np
import pandas as pd
from find_v0 import *
from change_of_speed import *
from export_cars_to_csv import *

pd.set_option('display.max_rows', 1000)
chosen_columns = ['Vehicle_ID', 'Frame_ID', 'Preceeding', 'Following', 'v_Vel', "v_Acc"]
df = pd.read_csv('data_750_805.csv', usecols=chosen_columns)

df_filtered = df[df['Vehicle_ID'] == 4].drop_duplicates()
print(df_filtered.iloc[:1000])
print(find_v0(df, 4))
print(slowing_down(df, 4, 128))
export_cars(df, (4, 6, 14, 18, 31, 34, 40, 44))
#print(df.iloc[:100]) 4, 6, 14, 18, 31, 34, 40, 44 Wartości ID samochodów poczynając od lidera, który nie ma nikogo przed nim
# prędkość v_0, czas t, minimalna odległość, przyspieszenie, zwalnianie, prędkość, droga