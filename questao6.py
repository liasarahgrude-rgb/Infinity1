##Calculadora de IMC: Crie um programa que receba o peso e a altura de uma pessoa. Calcule o IMC ($IMC = peso / altura^2$) e classifique:Abaixo de 18.5: "Abaixo do peso"Entre 18.5 e 24.9: "Peso normal"Entre 25 e 29.9: "Sobrepeso"30 ou mais: "Obesidade"
peso = float (input("Digite o seu peso: "))
altura = float (input("Digite a sua altura: "))
IMC = peso / (altura*altura)
if IMC < 18.5:
    print(f"Abaixo do peso!")
elif 18.5 < IMC < 24.9:
    print(f"Peso normal!")
elif 25 < IMC < 29.9:
    print(f"Sobrepeso!")
else:
    print(f"Obesidade!")