def export_cars(df, cols, *args):
    """Funkcja przyjmuje jako wartości ID samochodów. Na tej podstawie zapisuje dane dotyczące tego samochodu do pliku .csv
    Zmienna 'df' określa tablicę, z której chcemy eksportować dane.
    Zmienna '*args' przyjmuje wartości ID samochodów, których dane chcemy eksportować.
    Zmienna 'cols' przyjmuje kolumny (w formacie 'str'), które chcemy użyć.
    """
    df[df['Vehicle_ID'].isin(*args)].to_csv("filtered.csv", columns = cols, index = False)