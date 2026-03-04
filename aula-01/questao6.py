#Peça o peso e a altura do usuário, calcule o IMC e 
#informe se o IMC é maior ou igual a 18.5 ou se é menor que isso.
peso = float (input ("Digite o seu peso: "))
altura = float (input ("Digite a sua altura: "))
IMC = peso / (altura * altura)
if IMC >= 18.5:
    print (f"O seu IMC é maior ou igual a 18.5")
else:
    print (f"O seu IMC é menor que 18.5")