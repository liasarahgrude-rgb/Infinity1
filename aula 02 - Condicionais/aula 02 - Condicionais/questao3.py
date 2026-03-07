###Crie um programa que peça ao usuário um número inteiro e determine: Se o número é positivo, negativo ou zero. Se o número é par ou ímpar (apenas se for diferente de zero).  O programa deve exibir mensagens como: "Número positivo e par" "Número negativo e ímpar" "Número é zero"

inteiro = int (input("Digite um número inteiro: "))
if inteiro > 0:
    if inteiro % 2 == 0:
        print(f"O número é positivo e par!")
    else:
        print(f"O número é positivo ímpar!")
elif inteiro == 0:
    print(f"O número é nulo!")
elif inteiro < 0:
    if inteiro != 0 and inteiro % 2 == 0:
        print(f"O número é negativo e par!")
    else:
        print(f"O número é negativo e ímpar!")