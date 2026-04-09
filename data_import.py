import numpy as np
import pandas as pd
from find_v0 import *
from change_of_speed import *
from export_cars_to_csv import *
from car_v_derivative import *

# Informacje dotyczące wyświetlania
# Istnieje skrót klawiszowy dotyczący odkomentowania bloków tekstu
pd.set_option('display.max_rows', 1000)

# Utworzenie przefiltrowanego pliku z danymi
columns = ['Vehicle_ID', 'Frame_ID', 'Preceeding', 'Following', 'v_Vel', "v_Acc"]
IDs = tuple((4, 6, 14, 18, 31, 34, 40, 44))
df = pd.read_csv('data_750_805.csv', usecols=columns)
export_cars(df, columns, IDs)

# Załadowanie przefiltrowanego pliku z danymi
df2 = pd.read_csv('filtered.csv', usecols=columns)


#print(calculte_car_v_derivative(df2, 4))