from change_of_speed import vel_change

def calculte_car_v_derivative(df, ID, frame0, rate_of_change):
    """
    Dla samochodu z wybranym numerem ID wylicza zmienność v' na całej odległości.
    Funkcja używa innej funkcji, 'vel_change', do wyliczenia v'
    poczynając od pierwszej klatki samochodu z zadanym ID.
    Zmienna 'frame0' określa klatkę początkową.
    Funkcja pobiera zmienną 'rate_of_change', aby ustalić krok.
    """
    
    vChangeList = [] # Zawiera informacje o początku przedziału, końcu przedziału i v' na tym przedziale.

    for iteration in range(0,100):
        vChange = vel_change(df, ID, frame0 + iteration*rate_of_change, rate_of_change)
        if vChange == "Frame 2 out of bounds":
            break
        vChangeList.append((frame0 + iteration*rate_of_change, frame0+rate_of_change + iteration*rate_of_change, vChange))

    return vChangeList