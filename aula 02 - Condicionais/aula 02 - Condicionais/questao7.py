##Aumento de Salário: Leia o salário de um funcionário. Se for até R$ 1.500,00, ele recebe 15% de aumento. Se for maior, recebe 10%. O programa deve mostrar o salário antigo e o novo.
salario = float (input("Digite o seu salário atual: "))
if salario <= 1500:
    aumento = salario * 0.15
    salario2 = salario + aumento
    print(f"O seu salário antes do aumento era {salario:.2f} e com o aumento ficou {salario2}")
else:
    aumento = salario * 0.10
    salario2 = salario + aumento
    print(f"O seu salário antes do aumento era {salario:.2f} e com o aumento ficou {salario2}")