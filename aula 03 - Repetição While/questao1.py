##Menu com Loop Infinito
while True:
    print(f"-Digite 1 para ver")
    print(f"-Digite 2 para atualizar")
    print(f"-Digite 3 para cadastrar ")
    print(f"-Digite 4 para remover ")
    print(f"-Digite 5 para sair ")
    opcao = input("Digite a opção que você deseja visualizar: ")
    if opcao == '1':
        print(f"Vamos vizualizar!")
    elif opcao == '2':
        print(f"Vamos atualizar!")
    elif opcao == '3':
        print(f"Vamos iniciar o seu cadastro!")
    elif opcao == '4':
        print(f"Vamos remover suas informações!")
    elif opcao == '5':
        break 
    else :
        print(f"Digite 1,2,3,4 ou 5, não aceito outros números!")