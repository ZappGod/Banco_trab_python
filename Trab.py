import pandas as pd
import matplotlib.pyplot as plt

#Lê arquivo
df = pd.read_csv("dados.csv",encoding="latin-1")

#Os maiores valores e seus respectivos anos
dm_max = df.loc[df["valor"].idxmax()]["data"]
vm_max = df["valor"].max()

#Os menores valores e seus respectivos anos
dm_min = df.loc[df["valor"].idxmin()]["data"]
vm_min = df["valor"].min()

#Grafico do maior e menor de todos os anos
plt.bar(dm_max,vm_max)
plt.bar(dm_min,vm_min)
plt.title("Maior e menor valor dos anos")
plt.xlabel("Ano")
plt.show()