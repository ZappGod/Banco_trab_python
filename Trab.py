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

