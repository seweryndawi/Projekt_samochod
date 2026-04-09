def export_cars(df, cols, IDs):
    """Funkcja przyjmuje jako wartości ID samochodów. Na tej podstawie zapisuje dane dotyczące tego samochodu do pliku .csv
    Zmienna 'df' określa tablicę, z której chcemy eksportować dane.
    Zmienna 'IDs' przyjmuje wartości ID samochodów, których dane chcemy eksportować.
    Zmienna 'cols' przyjmuje kolumny (w formacie 'str'), które chcemy użyć.
    """
    df[df['Vehicle_ID'].isin(IDs)].to_csv("filtered.csv", columns = cols, index = False)