##O Triângulo: Escreva um programa que leia três números (lados de um triângulo). O programa deve informar se os lados formam um triângulo e, se sim, dizer se ele é Equilátero (3 lados iguais), Isósceles (2 lados iguais) ou Escaleno (todos diferentes).
lado1 = float(input("Digite o valor do lado A: "))
lado2 = float(input("Digite o valor do lado B: "))
lado3 = float(input("Digite o valor do lado C: "))
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print(f"Os três lados formam um triângulo do tipo equilátero!")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print(f"Os três lados formam um triângulo do tipo isósceles!")
    else:
        print(f"Os três lados formam um triângulo do tipo escaleno!")
else:
    print (f"Os três lados não formam um triângulo!")
