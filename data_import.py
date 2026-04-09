import numpy as np
import pandas as pd
from export_cars_to_csv import *
from car_v_derivative import *
from find_frame0 import find_frame0
# Informacje dotyczące wyświetlania
# Istnieje skrót klawiszowy dotyczący odkomentowania bloków tekstu
pd.set_option('display.max_rows', 1000)

# Utworzenie przefiltrowanego pliku z danymi
columns = ['Vehicle_ID', 'Frame_ID', 'Preceeding', 'Following', 'v_Vel', "v_Acc"]
# IDs = tuple((4,))
# df = pd.read_csv('data_750_805.csv', usecols=columns)
# export_cars(df, columns, IDs)

# Załadowanie przefiltrowanego pliku z danymi
df2 = pd.read_csv('filtered.csv', usecols=columns)

# Testowanie
frame0 = find_frame0(df2, 4)
print(calculte_car_v_derivative(df2, 4, frame0, 5))
print(vel_change(df2, 4, frame0, 5))