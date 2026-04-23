import pandas as pd

def data_convert():

    # Ścieżkę do pliku trzeba zmienić, gdy plik znajduje się w innym folderze i zamienić \ na \\
    # Przy kopiowaniu pliku kopiuje się ścieżka do niego
    dataset = pd.read_csv('data_750_805.csv')

    # Testowanie
    # print(list(dataset.columns))
    # print(dataset)

    # 1 stopa - 30,48 cm = 0,3048 m
    dataset['v_Length'] *= 0.3048
    dataset['v_Width'] *= 0.3048
    dataset['v_Vel'] *= 0.3048
    dataset['v_Acc'] *= 0.3048
    dataset['Space_Hdwy'] *= 0.3048

    # Testowanie
    # print(dataset)
    # print(dataset['Vehicle_ID'])

    dataset.to_csv('data_750_805.csv')