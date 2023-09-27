import requests
from datetime import datetime

def date_validation(initial,final):
    try:
        datetime.strptime(initial,'%d/%m/%Y')
        datetime.strptime(final, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def Request_api():
    print("Qual a data inicial e final que você deseja consultar? Ex 01/01/2010 até 31/12/2011")

    InitialDate = input("Data inicial: ")
    FinalDate = input("Data final: ")

    if date_validation(InitialDate,FinalDate):
        pf = requests.get(f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.20716/dados?formato=json&dataInicial={InitialDate}&dataFinal={FinalDate}")
        pj = requests.get(f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.20718/dados?formato=json&dataInicial={InitialDate}&dataFinal={FinalDate}")
        return pf,pj
    else:
        print("O padrão da data inserido é inválido.")

