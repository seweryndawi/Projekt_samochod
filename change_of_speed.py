import numpy as np
import pandas as pd

def change(df, veh_ID, frame1):
    """Ze zdjęcia pierwszy wzór. Przyjęte h = 10. Jako różnica wzięta jedna sekunda."""
    try:
        frame2 = frame1 + 10
        row1 = df[(df['Vehicle_ID'] == veh_ID) & (df['Frame_ID'] == frame1)].iloc[0]
        row2 = df[(df['Vehicle_ID'] == veh_ID) & (df['Frame_ID'] == frame2)].iloc[0]
        change_of_speed = (row2['v_Vel'] - row1['v_Vel']) / 10
    except:
        change_of_speed = "Measurement_out_of_bounds"
    return change_of_speed