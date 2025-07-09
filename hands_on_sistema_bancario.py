# Fazer um sistema bancario
# Ter opção de deposito onde o valor tem de ser inteiro e posisitivo, o sistema n pode permitir outro valor 
# Ter opção de saque, nessa opção o usuário so pode fazer no maximo 3 saques diarios onde cada um so pode ser de no maximo 500 reais 
# Na opção de saque só pode ser possivel sacar se tiver saldo na conta, caso não tenha deve ser avisado 
# Todas operações devem estar em um extrato
# No extrato decve constar o saldo final


# Aqui usaremos (""") ou (''') para defenir strings multilineas
menu = """ 

[d] Depositar
[s] Sacar
[e] Extrato
[s] Sair

=>"""

saques = []
depositos = []
extrato = {}
LIMITES_SAQUES = 3
total_em_conta = 0


def sacar 
