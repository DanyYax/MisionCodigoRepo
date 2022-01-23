import pandas as pd

# leemos nuestro csv directo a un dataframe
df = pd.read_csv("Estudiantes.csv")

print(df)
print()

print(df["Apellido"].value_counts())

print(df["Apellido"].sort())