def find_frame0(df, ID):
    row = df[df['Vehicle_ID'] == ID].iloc[0]
    return row['Frame_ID']