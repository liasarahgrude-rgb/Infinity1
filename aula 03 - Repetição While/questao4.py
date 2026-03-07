##Crie um programa que solicite ao usuário a entrada de 5 números inteiros. Utilize um contador para controlar quantas vezes o loop foi executado. Utilize um acumulador para somar os números digitados. Ao final, calcule e exiba a média dos números.
i = 0
soma = 0
while i < 5:
    num = int(input("Digite um número inteiro: "))
    soma = soma + num
    i += 1
    media = soma / 5
print(f"A média dos números digitados é {media}")