# Desafio

# Criação do Menu

menu_banco = '''

Bem-vindo(a) ao Banco!

Digite a opção que você deseja:

deposito = [0]
saque = [1]
extrato = [2]
sair = [3]
novo usuário = [4]
nova conta = [5]
listagem de contas = [6]

'''

# Criando funções

# Função de saque

def saque(*, saldo, valor, extrato, numero_de_saques, limite_saque):
        
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

    return saldo, extrato

# Função de depósito

def deposito(saldo, valor, extrato, /):

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else:
            print('Valor inválido.')

        print('\n','='*10,'DEPÓSITO REALIZADO COM SUCESSO','='*10)
        return saldo, extrato

# Função de extrato

def extrato(saldo, /, *, extrato):
    print('\n')
    print('='*20,' EXTRATO ','='*20)
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('='*50)

# Função de Novo Usuário

def novo_usuario(usuarios):
    cpf = input('Digite seu CPF [Apenas os números]: ')
    usuario = filtragem_de_usuarios(cpf, usuarios)

    if usuario:
        print('Este CPF já está cadastrado com outro usuário!')
        return
    
    nome = input('Nome completo: ')
    data_de_nascimento = input('Data de nascimento [dd-mm-aa]: ')
    endereco = input('Endereço [logradouro, nº - bairro - cidade/uf]: ')

    usuarios.append({'nome': nome, 'data_de_nascimento': data_de_nascimento, 'cpf': cpf, 'endereco': endereco})
    print('='*10,f'USUÁRIO CRIADO COM SUCESSO!','='*10)

# Função de Filtragem de Usuários

def filtragem_de_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# Função de Criar uma Nova Conta

def criar_nova_conta(agencia, numero_conta, usuarios):

    cpf = input('Digite o CPF do usuário: ')
    usuario = filtragem_de_usuarios(cpf, usuarios)

    if usuario:
        print('='*10,'CONTA CRIADA COM SUCESSO','='*10)
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('Usuário não encontrado!')

def listagem_de_contas(contas):
    for conta in contas:
        linha = f'''
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}

        '''
        print('='*20)
        print(linha)
        print('='*20)

# Declaração de variáveis

saldo = 0
limite_saque = 500
numero_de_saques = 0
extrato = ''
TOTAL_DE_SAQUES = 3
usuarios = []
contas = []
AGENCIA = '0001'

# Criando o laço de repetição

while True:
    opcao = int(input(menu_banco))

    # Depósito

    if opcao == 0:
        
          valor = float(input('Digite o valor que será depositado: R$'))

          saldo, extrato = deposito(saldo, valor, extrato)

    # Saque

    elif opcao == 1:
        valor = float(input('Digite o valor que será sacado: R$'))

        saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, numero_de_saques=numero_de_saques, limite_saque=limite_saque,)

    # Extrato

    elif opcao == 2:
        
        saldo, extrato = extrato(saldo, extrato=extrato)
    
    # Criar novo usuário

    elif opcao == 4:
        novo_usuario(usuarios)
    
    # Criar nova conta

    elif opcao == 5:
        numero_conta = len(contas) + 1
        conta = criar_nova_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    # Listagem de contas
    
    elif opcao == 6:
        listagem_de_contas(contas)

    # Sair

    elif opcao == 3:
        break

    else:
        print('Selecione uma operação válida.')