import requests

print("Qual a data inicial e final que você deseja consultar? Ex 01/01/2010 até 31/12/2011")

InitialDate = input("Data inicial: ")
FinalDate = input("Data final: ")


r = requests.get("https://api.bcb.gov.br/dados/serie/bcdata.sgs.20716/dados?formato=csv&dataInicial={InitialDate}&dataFinal={FinalDate} ")
print(r.content)