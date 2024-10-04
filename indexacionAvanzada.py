import pandas as pd

datos={'Nombre ':['Alice','Bob','Charlie'],
       'Edad ': [25,30,35],
       'Ciudad ': ['A','B','C']}
df=pd.DataFrame(datos)
print(df)

#Seleccionar datos con iloc[]
sel_iloc=df.iloc[1,1]
print(sel_iloc)

#Seleccionar datos con iat[]
sel_iat=[1,1]
print(sel_iat)