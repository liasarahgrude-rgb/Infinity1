##Crie um programa que solicite uma senha ao usuário continuamente até que a senha correta (ex: "1234") seja digitada. Utilize um laço while para repetir a entrada. Exiba uma mensagem de erro a cada tentativa incorreta. Ao acertar, exiba "Acesso Liberado" e encerre a execução.
senha = '1102'
senhacliente = ''
i = 0
while senhacliente != senha and i < 3:
    senhacliente = input ("Digite a senha: ")
    if senhacliente != senha:
        print("errou tente novamente")
        print(f'tentativas {i+1}/3')
        i += 1
    else:
        print(f"A senha está correta o acesso tá liberado!")
        break