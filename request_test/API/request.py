import requests
from datetime import datetime


def date_validation(data,data1):
    try:
        datetime.strptime(data,data1 '%d%m%y')
        return True
    except ValueError:
        return False


print("Qual a data inicial e final que você deseja consultar? Ex 01/01/2010 até 31/12/2011")

InitialDate = input("Data inicial: ")
FinalDate = input("Data final: ")
requestUrl = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.20716/dados?formato=csv&dataInicial={InitialDate}&dataFinal={FinalDate}"

<<<<<<< HEAD

r = requests.get(requestUrl)
print(r.content)
=======
if date_validation(InitialDate,FinalDate) == True:
    pf = requests.get(f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.20716/dados?formato=csv&dataInicial={InitialDate}&dataFinal={FinalDate}")
    pj = requests.get(f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.20718/dados?formato=csv&dataInicial={InitialDate}&dataFinal={FinalDate}")
else:
    print("O formato da data é incorreto tente novamente.")



print(pf.content)
print(pj.content)
>>>>>>> 7eafb16 (datetime_validation)
