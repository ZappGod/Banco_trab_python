import pandas as pd
import matplotlib.pyplot as plt
import request_api

#Função para ver o máximo e o mínimo entre os anos
def funcaoMaxMin():
    
    #Pega os valores de pf e os transforma em números
    data = pf.json()
    df = pd.DataFrame(data)
    df['valor'] = pd.to_numeric(df['valor'], errors='coerce')
    
    #Acha o maior valor entre eles e sua data correspondente 
    fdm_max = df.loc[df["valor"].idxmax()]["data"]
    fvm_max = df["valor"].max()
    
    #Acha o menor valor entre eles e sua data correspondente 
    fdm_min = df.loc[df["valor"].idxmin()]["data"]
    fvm_min = df["valor"].min()
    
    #Pega os valores de pj e os transforma em números
    data2 = pj.json()
    dj = pd.DataFrame(data2)
    dj['valor'] = pd.to_numeric(dj['valor'], errors='coerce')
    
    #Acha o maior valor entre eles e sua data correspondente 
    jdm_max = dj.loc[dj["valor"].idxmax()]["data"]
    jvm_max = dj["valor"].max()
    
    #Acha o menor valor entre eles e sua data correspondente 
    jdm_min = dj.loc[dj["valor"].idxmin()]["data"]
    jvm_min = dj["valor"].min()

    #Cria um gráfico de barras comparando os valores máximos e mínimos de Pessoa Jurídica e Pessoa Física
    bar_width = 0.35
    index = range(2)
    plt.bar(index, [jvm_max, jvm_min], bar_width, label='Pessoa Jurídica', align='center', alpha=0.7)
    plt.bar([i + bar_width for i in index], [fvm_max, fvm_min], bar_width, label='Pessoa Física', align='center', alpha=0.7)
    
    #Exibe na tela o gráfico com as legendas correspondentes
    plt.xlabel('Diferença')
    plt.ylabel('Valores')
    plt.xticks([0.175, 1.175], [f"{jdm_max} | {fdm_max}\nMáximo", f"{jdm_min} | {fdm_min}\nMínimo"])
    plt.title("Máximo e Mínimo valor dos anos")
    plt.legend()
    plt.tight_layout()
    return plt.show()

