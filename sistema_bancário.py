# Desafio

# Criação do Menu

menu_banco = '''

Bem-vindo(a) ao Banco!

Digite a opção que você deseja:

deposito = [0]
saque = [1]
extrato = [2]
sair = [3]

'''

# Declaração de variáveis

saldo = 0
limite_saque = 500
numero_de_saques = 0
extrato = ''
TOTAL_DE_SAQUES = 3

# Criando o laço de repetição

while True:
    opcao = int(input(menu_banco))

    # Depósito

    if opcao == 0:
        valor = float(input('Digite o valor que será depositado: R$'))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else:
            print('Valor inválido.')

    # Saque

    elif opcao == 1:
        valor = float(input('Digite o valor que será sacado: R$'))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_saque
        excedeu_saques = numero_de_saques >= TOTAL_DE_SAQUES

        if excedeu_saldo:
            print('Erro. Você não tem saldo suficiente.')

        elif excedeu_limite:
            print('Erro. O valor de saque excede o limite.')

        elif excedeu_saques:
            print('Erro. Você atingiu o limite de saques')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_de_saques += 1

        else:
            print('O valor informado é inválido.')

    # Extrato

    elif opcao == 2:
        print('\n')
        print('='*20,' EXTRATO ','='*20)
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('='*50)
    
    # Sair

    elif opcao == 3:
        break

    else:
        print('Selecione uma operação válida.')