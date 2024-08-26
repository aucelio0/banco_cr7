# biblioteca
from datetime import date

# função menu do banco
def menu_principal():
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year
    
    print(f'\n{'=' * 20} BANCO CR7 / {dia}/{mes}/{ano} {'=' * 20}\n')
    print('1- Criar uma conta.')
    print('2- Entrar na conta.')
    print('3- Exibir correntistas.')
    print('4- Excluir conta.')
    print('5- Encerrar programa.')
    
# função lista de operações
def exibir_operacoes():
    print(f'\n{'-' * 10} OPERAÇÕES {'-' * 10}\n')
    print('1- Consultar saldo.')
    print('2- Depositar valor.') 
    print('3- Sacar valor.')
    print('4- Voltar')
    
# função exibir dados do correntista
def exibir_dados(nome, i, saldo): 
    print(f'ID: {i}')
    print(f'Nome: {nome}')
    print(f'Agência: 1001')
    print(f'Conta: 1001{i}')
    print(f'Saldo: R$ {saldo}')
    
#função de depósito
def depositar_valor(saldo, valor): 
    saldo += valor
    return saldo

# função saque
def sacar_valor(saldo, valor):
    saldo -= valor
    return saldo     