# Fazer um sistema bancario
# Ter opção de deposito onde o valor tem de ser inteiro e posisitivo, o sistema n pode permitir outro valor 
# Ter opção de saque, nessa opção o usuário so pode fazer no maximo 3 saques diarios onde cada um so pode ser de no maximo 500 reais 
# Na opção de saque só pode ser possivel sacar se tiver saldo na conta, caso não tenha deve ser avisado 
# Todas operações devem estar em um extrato
# No extrato decve constar o saldo final


saques = []
depositos = []
limites_de_saque = 3
total_em_conta = sum(depositos) - sum(saques)

def main():

# Aqui usaremos (""") ou (''') para defenir strings multilineas
    print( """ 
    [s] Sacar
    [d] Depositar
    [e] Extrato
    [q] Sair

    => """)

def sacar():
    global limites_de_saque, saques
    if limites_de_saque <= 0:
        print("Limite de saques diários atingido.")
        return
    total_em_conta = sum(depositos) - sum(saques)
    valor_saque = float(input('Qual valor deseja sacar? '))
    if valor_saque > total_em_conta:
        print(f'Saldo insuficiente, você possui R$ {total_em_conta}')
        return
    elif valor_saque <= 500:
        saques.append(valor_saque)
        print(f'Saque de R$ {valor_saque:.2f} realizado com sucesso!')
        limites_de_saque -= 1
        print(f'Limite de saques diários: {limites_de_saque}')
    else:
        print('O valor do saque deve ser no máximo R$ 500.')

def depositar():
    global depositos
    valor_deposito = float(input('Qual valor deseja depositar? '))
    if valor_deposito > 0:
        depositos.append(valor_deposito)
        print(f'Depósito de R$ {valor_deposito:.2f} realizado com sucesso!')
    else:
        print('O valor do depósito deve ser positivo.')

def ver_extrato():
    total_em_conta = sum(depositos) - sum(saques)
    print("\nExtrato:")
    print("Saques:")
    for saque in saques:
        print(f'R$ {saque:.2f}')
    print("Depósitos:")
    for deposito in depositos:
        print(f'R$ {deposito:.2f}')
    print(f'Saldo final: R$ {total_em_conta:.2f}')
    print("\n")

while True:
    main()
    opcao = input("Escolha uma opção: ").lower()
    if opcao == "s":
        sacar()
    elif opcao == "d":
        depositar()
    elif opcao == "e":
        ver_extrato()
    elif opcao == "q":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")