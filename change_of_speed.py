def vel_change(df, veh_ID, frame1, rate_of_change):
    """ Funkcja pozwalająca na wyznaczenie zmiany prędkości pomiędzy dwoma okresami czasu.
    Zmienna 'frame1' przyjmuje jako wartość klatkę z początkiem ruchu.
    Zmienna 'rate_of_change' określa długość ruchu, przy założeniu, że 1 klatka = 100 ms.
    Ta funkcja używa pierwszego wzoru z kartki.
    """
    try:
        frame2 = frame1 + rate_of_change
        row1 = df[(df['Vehicle_ID'] == veh_ID) & (df['Frame_ID'] == frame1)].iloc[0]
        row2 = df[(df['Vehicle_ID'] == veh_ID) & (df['Frame_ID'] == frame2)].iloc[0]
        change_of_velocity = (row2['v_Vel'] - row1['v_Vel']) / rate_of_change
    except:
        change_of_velocity = "Frame 2 out of bounds"
    return change_of_velocity