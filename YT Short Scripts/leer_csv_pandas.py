import pandas as pd

# leemos nuestro csv directo a un dataframe
df = pd.read_csv("Estudiantes.csv")

df = df.dropna()

print(df)
print()

prom = df["Calificacion"].mean()
print(prom)

print((78 +80 +60 +90 +100 +99 +60) / 7)