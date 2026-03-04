#Peça o nome do usuário e verifique se ele digitou algo. 
#Se estiver vazio, mostre que o nome não pode ser vazio, 
#caso contrário confirme que o nome foi registrado.
nome = input ("Digite o seu nome: ")
if nome == "":
    print (f"O nome não pode ser vazio!")
else: 
    print (f"O seu nome foi registrado!")