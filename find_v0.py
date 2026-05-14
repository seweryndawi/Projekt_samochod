def find_v0(df, veh_ID):
    """Wyszukanie pierwszej predkosci samochodu o ID veh_ID"""

    
    row = df[df['Vehicle_ID'] == veh_ID].iloc[0]
    return row["v_Vel"]