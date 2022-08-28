#Read combined_csv.csv

import pandas as pd

df = pd.read_csv('data/ventas_comercial/combined_csv.csv')

filtro_players = df.groupby('Play')['Player'].unique()

#Change column of lists with len of list

#filtro_players = filtro_players.apply(lambda x: len(x))

#loc first value of filtro_players

print(filtro_players.loc[0])



