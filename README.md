# Banco_trab_python

Trabalho de requisição de API e geração de gráficos em Python

Alunos: Anthonny Camargo, Gabriell Zappelini, Otávio Moraes, William Coscodai

## Requisitos

Instalação de dependências:

`pip install -r ./src/requirements.txt ou pip install -r ./requirements.txt`

## Execução

`python ./src/main.py ou python ./main.py`

Após a execução, o sistema abrirá um menu de opções para o usuário, onde ele poderá escolher entre as opções:

1. Mostrar gráficos
2. Requisitos
3. Sair

Basta digitar o número da opção desejada e apertar enter.
Após isso o sistema irá mostrar os dados correspondentes a opção escolhida.

## API

O arquivo `request_api.py` é responsável pela requisição da API do banco central e retornar os dados.

O arquivo `menu.py` é responsável por gerar o menu de opções para o usuário, e direciona-lo para a opção escolhida.

O arquivo `main.py` é o arquivo principal da execução do sistema.

O arquivo `requirements.txt` é responsável por conter as dependências do projeto.

O arquivo `MaxMinTot.py` é responsável por gerar o gráfico dos valores mínimos e máximos taxa de juros de todos os anos para pessoas físicas e jurídicas.

O arquivo `graphAvg.py` é responsável por gerar o gráfico de média da taxa de juros anual para pessoas físicas e jurídicas, em determinado ano escolhido pelo usuário
