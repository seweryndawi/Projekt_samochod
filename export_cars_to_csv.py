def export_cars(df, *args):
    """Funkcja przyjmuje jako wartości ID samochodów. Na tej podstawie zapisuje dane dotyczące tego samochodu do pliku .csv"""
    df[df['Vehicle_ID'].isin(*args)].to_csv("test.csv", columns = ['Vehicle_ID', 'Frame_ID', 'Preceeding', 'Following', 'v_Vel', "v_Acc"], index = False)