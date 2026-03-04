#Peça a altura do usuário e verifique se é um valor válido (maior que zero). 
#Caso não seja, informe que a altura é inválida.
altura = int (input ("Digite sua altura: "))
if altura < 0:
    print (f"Sua altura é inválida")