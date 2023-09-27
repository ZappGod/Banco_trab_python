import pandas as pd
import matplotlib.pyplot as plt

def GetAverageGraphPjPf(pj, pf):
    # Transforma os dados JSON em DataFrames do pandas
    pjData = pd.DataFrame(pj.json())
    pfData = pd.DataFrame(pf.json())

    # Converte a coluna 'valor' para um numero
    pjData['valor'] = pd.to_numeric(pjData['valor'], errors='coerce')
    pfData['valor'] = pd.to_numeric(pfData['valor'], errors='coerce')

    # Pega o ano da coluna 'data' e cria uma nova coluna 'ano' em ambos os DataFrames
    pjData['ano'] = pd.to_datetime(pjData['data']).dt.year
    pfData['ano'] = pd.to_datetime(pfData['data']).dt.year

    # Calcula a média de cotação para cada ano em ambos os DataFrames
    media_pj = pjData.groupby('ano')['valor'].mean()
    media_pf = pfData.groupby('ano')['valor'].mean()

    # Plota o gráfico de linhas para mostrar a cotação geral do ano para ambos os tipos
    plt.figure(figsize=(10, 6))
    plt.plot(media_pj.index, media_pj.values, label='Cotação PJ', marker='o', linestyle='-')
    plt.plot(media_pf.index, media_pf.values, label='Cotação PF', marker='o', linestyle='-')
    
    plt.xlabel('Ano')
    plt.ylabel('Média de Cotação')
    plt.title('Cotação Geral do Ano (PJ vs PF)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Exemplo de utilização:
# Substitua pj e pf pelo response da api do gov. Ex: (https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=01/01/2010&dataFinal=31/12/2016)
# GetAverageGraphPjPf(pj, pf)
