import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo 
df = pd.read_csv("dados.csv", encoding="latin-1", parse_dates=["data"])

# Extrai o ano da coluna 'data' e cria uma nova coluna 'ano'
df['ano'] = df['data'].dt.year

# Calcula a média de cotação para cada ano
media_por_ano = df.groupby('ano')['valor'].mean()

# Plota o gráfico de barras da média de cotação por ano
plt.figure(figsize=(10, 6))
media_por_ano.plot(kind='bar', color='blue', alpha=0.7)
plt.xlabel('Ano')
plt.ylabel('Média de Cotação')
plt.title('Média de Cotação por Ano')
plt.xticks(rotation=0)
plt.show()
