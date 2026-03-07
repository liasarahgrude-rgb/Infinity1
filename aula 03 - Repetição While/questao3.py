##Escreva um loop while cuja execução é controlada pelo usuário.
nome = input ("Digite o seu nome: ")
quantidade = int(input ("Quantas vezes você quer exibir seu nome?"))
i = 0
while i < quantidade:
    print(f"{nome}")
    i += 1