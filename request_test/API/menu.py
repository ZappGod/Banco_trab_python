import graphAvg
import MaxMinTot
import request_api

def menu():
    while True:
        print('''
               Menu:
          
        [1] Plotar gráficos
        [2] Documentação
        [3] Requisitos
        [4] Sair             
        ''')

        choice = input("Escolha uma opção: ")

        if choice == '1':
            plotar_graficos_menu()
        elif choice == '2':
            exibir_documentacao()
        elif choice == '3':
            exibir_requisitos()
        elif choice == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def plotar_graficos_menu():
    while True:
        print('''
        [1] Gráfico máximo e mínimo
        [2] Gráfico média
        [3] Voltar
        ''')

        choice = input("Escolha uma opção de gráfico: ")

        if choice == '1':
            plotar_maximo_minimo()
        elif choice == '2':
            plotar_media()
        elif choice == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

def plotar_maximo_minimo():
    pf, pj = request_api.Request_api() 
    MaxMinTot.funcaoMaxMin(pf, pj)

def plotar_media():
    pf, pj = request_api.Request_api()
    graphAvg.GetAverageGraphPjPf(pj,pf)

def exibir_documentacao():

    print("Ainda não escrita")

def exibir_requisitos():
    

    print("Requisitos")

menu()
