from change_of_vel import vel_change

def calculate_v_derivative(df, Id, first_frame, last_frame, rate_of_change) -> list:
    """
    Dla samochodu z wybranym numerem Id wylicza zmienność v' w czasie od frame0 do samego końca.
    Funkcja używa innej funkcji, 'vel_change', do wyliczenia v'

    Parametry:
        df Tablica z wartosciami
        Id Id samochodu
        first_frame Klatka poczatkowa
        last_frame Klatka koncowa
        rate_of_change Krok dyskretny
    
    Wartosc zwracana:
        lista ze zmianami predkosci (float)
    """
    

    v_change_list = []

    for iteration in range(first_frame, last_frame + 1 - rate_of_change, rate_of_change):

        v_change = vel_change(df, Id, iteration, iteration + rate_of_change)
        v_change_list.append(v_change)

    return v_change_list