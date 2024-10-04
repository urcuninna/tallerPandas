import pandas as pd
import matplotlib.pyplot as plt

#Creamos una base de datos
data={'Categoria': ['A','B','C','A','B','C','A','B','A'],
      'Valor': [10,20,15,25,30,20,35,40,45]}
df=pd.DataFrame(data)

#Creamos gráfico de barras
df['Categoria'].value_counts().plot(kind='bar')
plt.title('Distribución de la variable categórica')
plt.xlabel('Categoria')
plt.ylabel('Frecuencia')
plt.show()

#Ahora hacemos un gráfico de dispersión
df.plot(kind='scatter', x='Categoria', y='Valor', color='blue')
plt.title('Relación entre dos variable numéricas')
plt.xlabel('Categoria')
plt.ylabel('Valor')
plt.show()

#Ahora creamos un dateframe para visualizar tendencia a lo largo del tiempo con un gráfico de lineas
time_series=pd.date_range('2024-01-01', periods=10)
tendencias={'Fecha': time_series,
      'Valor': [10,25,15,25,30,35,40,50,45,55]}
df1=pd.DataFrame(tendencias)

#Ahora se crea el grafico de lineas
df1.plot(x='Fecha',y='Valor', color='green')
plt.title('Tendencias a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.show()