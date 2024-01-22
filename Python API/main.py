import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC24d087c9c86275dd0c99cc9413b9c4e8"
# Your Auth Token from twilio.com/console
auth_token  = "59a56186e0d257415b0314c3e9c661d2"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5511985735869",
            from_="+12017293106",
            body=f'Olá, SR.Diego! No mês de {mes} alguém bateu a meta. Foi Vendedor: {vendedor},com o toatal de: {vendas}. Ele ganhou a viagem com a Família.')
        print(message.sid)

# Para cada arquivo:

# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55.000 não quero fazer nada
