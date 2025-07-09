descontos = {
    "DESCONTO10": 0.90,
    "DESCONTO20": 0.80,
    "SEM_DESCONTO": 1.00
}   
while True:
    preco = float(input('Qual o valor da compra? '))
    cupom = input('Qual o cupom de desconto? ')

    if cupom in descontos:
        preco *= descontos[cupom]

    print(f'Preço final: R$ {preco:.2f}')
    continuar = input('Deseja realizar outra compra? (s/n) ')
    if continuar.lower() != 's':
        print('Obrigado por comprar conosco!')
        break