####Crie um programa que solicite ao usuário: Idade da pessoa Se possui carteira de motorista (True ou False) O programa deve verificar se a pessoa pode dirigir. Para isso, a pessoa precisa ter 18 anos ou mais e ter carteira. Exiba na tela: "Pode dirigir" se a pessoa atender aos critérios "Não pode dirigir" caso contrário Dica: use os operadores >= e and.

idade = int(input("Digite a sua idade: "))
carteira = bool(input ("Você tem carteira de motorista? Digite 0 para sim e 1 para não "))
if idade >= 18 and carteira == 0:
    print(f"Pode dirigir!")
else : 
    print(f"Não pode dirigir!")