##Ano Bissexto: Peça ao usuário para digitar um ano e diga se ele é bissexto ou não. (Dica: Um ano é bissexto se for divisível por 4, mas não por 100, exceto se for divisível por 400).
ano = int (input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano é bissexto!")
else:
    print(f"O ano não é bissexto!")