import pandas as pd

datos={'A':[1,2,3],
       'B': [4,5,6]}
df=pd.DataFrame(datos)

#sumar 10 a todas las entradas
df_suma=df+10
print(df_suma)

datos1={'A':[1,2,3],
       'B': [4,5,6]}
df1=pd.DataFrame(datos1)
datos2={'A':[10,20,30],
       'B': [40,50,60]}
df2=pd.DataFrame(datos2)

#Suma entre dataframes
df_suma1=df1+df2
print(df_suma1)

#Añadimos una serie para probar la suma entre serie y datframe. primero creamos a serie
serie= pd.Series([10,20],index=['A','B'])
resultado=df + serie
print(resultado)