import pandas as pd
#cargar base de datos csv
movies=pd.read_csv('movie.csv')
print(movies.head())

anime=pd.read_excel('animeflv.xlsx')
print(anime.head())