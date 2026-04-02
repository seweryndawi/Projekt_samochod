import numpy as np
import pandas as pd
"""Ze zdjęcia pierwszy wzór. Przyjęte h = 10. Wzięta tutaj jako różnica jedna sekunda."""
def slowing_down(df, veh_ID, frame1):
    frame2 = frame1 + 10
    row1 = df[(df['Vehicle_ID'] == veh_ID) & (df['Frame_ID'] == frame1)].iloc[0]
    row2 = df[(df['Vehicle_ID'] == veh_ID) & (df['Frame_ID'] == frame2)].iloc[0]
    change_of_speed = (row2['v_Vel'] - row1['v_Vel']) / 10
    return change_of_speed