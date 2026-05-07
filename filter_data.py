import pandas as pd
from data_convert import convert_data


# Informacje dotyczące wyświetlania
# Istnieje skrót klawiszowy dotyczący odkomentowania bloków tekstu


# Zamiana jednostek amerykanskich na m. Potrzebne wywolanie jednokrotne.
# convert_data()


# Utworzenie przefiltrowanego pliku z danymi
# df = pd.read_csv('data_750_805.csv', index_col=0)
# df = df[df['Lane_ID'].isin([1, 2])]
# df = df[df['Preceeding'] != 0]
# df = df[df['Following'] != 0]

# df['Vehicle_ID'] = df['Vehicle_ID'].astype(int)
# df['Following'] = df['Following'].astype(int)
# df['Frame_ID'] = df['Frame_ID'].astype(int)

# df = df[
#     (df['Vehicle_ID'] < 100) & 
#     (df['Following'] < 100) &
#     (df["Frame_ID"].isin(range(0, 1000, 10)))
#         ]


# # # Zaladowanie do pliku .csv danych z mniejsza iloscia danych
# df.to_csv('reduced_data.csv', index=False)


# Stworzenie tabel lidera i podazajacego, polaczenie w jedna tabele
new_columns = ['Vehicle_ID', 'Frame_ID', 'Preceeding', 'Global_X', 'Global_Y', 'v_Length', 'Space_Hdwy', 'v_Vel', 'v_Acc']
followers_df = pd.read_csv('reduced_data.csv', usecols=new_columns)

followers_df = followers_df.rename(columns = {
    'Vehicle_ID': 'follower_id',
    'Preceeding': 'leader_id',
    'Global_X': 'follower_x',
    'Global_Y': 'follower_y',
    'v_Vel': 'follower_vel',
    'v_Acc': 'follower_acc',
    'v_Length': 'follower_length',
    'Space_Hdwy': 'follower_hdwy'
}
)


leaders_df = pd.read_csv('reduced_data.csv', usecols=new_columns)
leaders_df = leaders_df.rename(columns = {
    'Vehicle_ID': 'leader_id',
    'Global_X': 'leader_x',
    'Global_Y': 'leader_y',
    'v_Vel': 'leader_vel',
    'v_Acc': 'leader_acc',
    'v_Length': 'leader_length',
    'Space_Hdwy': 'leader_hdwy'
}
)


merged_df = followers_df.merge(
    leaders_df,
    on=['Frame_ID', 'leader_id'],
    how='inner'
)

merged_df['distance'] = merged_df['follower_hdwy'].astype(float) - merged_df['leader_length'].astype(float)

merged_df = merged_df[
    [
        'Frame_ID',
        'leader_id',
        'leader_x',
        'leader_y',
        'leader_vel',
        'leader_acc',
        'follower_id',
        'follower_x',
        'follower_y',
        'follower_vel',
        'follower_acc',
        'distance'
    ]
]


merged_df.to_csv('leader_follower.csv', index=False)