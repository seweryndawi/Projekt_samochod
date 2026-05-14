def find_frame0(df, ID):
    """Wyszukanie pierwszej klatki samochodu o danym ID.
    
    Parametry
        df Tablica z danymi
        ID ID pojazdu
    
    Zwracana wartosc
        Klatka
    """
    row = df[df['Vehicle_ID'] == ID].iloc[0]
    return row['Frame_ID']