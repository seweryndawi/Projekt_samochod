def length_between(df, Id, frame):

    """
    Funkcja wyznacza odleglosc pomiedzy dwoma samochodami w okreslonej klatce.

    Parametry:
        df Tablica danych
        Id1 Id samochodu z przodu
        frame Klatka, czas w ktorym sprawdzamy odleglosc
    
    Wartosc zwracana:
        Odstep pomiedzy poczatkiem samochodu z ID = Id i koncem samochodu z przodu
    """


    car_following = df[(df["Vehicle_ID"] == Id) &
                       (df["Frame_ID"] == frame)]

    if car_following["Preceeding"].iloc[0] == 0:

        return None
    
    else:
        car_preceding = df[(df["Vehicle_ID"].iloc[0] == car_following["Preceeding"].iloc[0]) & 
                           (df["Frame_ID"] == frame)]
        distance = car_following["Space_Hdwy"].iloc[0] - car_preceding["v_Length"].iloc[0]

        return distance