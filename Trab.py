import pandas as pd
import matplotlib.pyplot as plt

#lê arquivo
df = pd.read_csv("dados.csv",encoding="latin-1")

#Os maiores valores e seus respectivos anos
dm_max = df.loc[df["valor"].idxmax()]["data"]
vm_max = df["valor"].max()

#Os menores valores e seus respectivos anos
dm_min = df.loc[df["valor"].idxmin()]["data"]
vm_min = df["valor"].min()

plt.bar(dm_max,vm_max)
plt.bar(dm_min,vm_min)
plt.show()
"""
Tentativa falha de achar o maximo e o minimo por ano
df_dataaux = pd.to_datetime(df['data'], format='%d/%m/%Y')
dm_max11 = df[df_dataaux.dt.year == 2011]
vm_max11 = df[df_dataaux.dt.year == 2011]['valor'].max()

plt.bar(dm_max11,dm_max11)
plt.show()
"""