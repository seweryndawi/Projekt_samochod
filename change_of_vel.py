def vel_change(df, Id, frame1, frame2):
    """ 
    Funkcja pozwalająca na wyznaczenie zmiany prędkości pomiędzy dwoma okresami czasu.
    
    Parametry:
        df Tablica z danymi
        Id Id samochodu
        frame1 Pierwsza klatka (mniejsza / wczesniejsza)
        frame2 Druga klatka (większa / pozniejsza)
    
    Zwracana wartosc:
        Zmiana w predkosci (float)
    """


    row1 = df[(df['Vehicle_ID'] == Id) & (df['Frame_ID'] == frame1)].iloc[0]
    row2 = df[(df['Vehicle_ID'] == Id) & (df['Frame_ID'] == frame2)].iloc[0]
    change_of_velocity = row2['v_Vel'] - row1['v_Vel']

    return change_of_velocity