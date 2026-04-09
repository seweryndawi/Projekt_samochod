import find_v0
import change_of_speed

def calculte_car_v_derivative(df, Id):
    """
    Dla samochodu z wybranym numerem ID wylicza zmienność v' na całej odległości.
    Funkcja używa innej funkcji, 'change_of_speed', do wyliczenia v'
    poczynając od pierwszej klatki.
    """
    v0 = find_v0.find_v0(df, Id)
    frameInterval_vDerivative = [] # Zawiera informacje o początku przedziału, końcu przedziału i v' na tym przedziale.
    for iteration in range(0,100):
        vDerivative = change_of_speed.change(df, Id, 128, iteration*10)
        if vDerivative == "Measurement_out_of_bounds":
            break
        frameInterval_vDerivative.append((128+iteration*10, 128+10+iteration*10, vDerivative))
    return frameInterval_vDerivative