##Crie um programa em Python que: Peça ao usuário duas notas para dois alunos (total de 4 notas). Calcule a média de cada aluno. Exiba para cada aluno a mensagem correspondente: "Aprovado" se a média for maior ou igual a 7; "Recuperação" se a média for maior ou igual a 5 e menor que 7; "Reprovado" se a média for menor que 5.

nota1Aluno1 = float (input("Digite a nota do aluno 1 na primeira avaliação: "))
nota2Aluno1 = float (input("Digite a nota do aluno 1 na segunda avaliação: "))
nota1Aluno2 = float (input("Digite a nota do aluno 2 na primeira avaliação: "))
nota2Aluno2 = float (input("Digite a nota do aluno 2 na segunda avaliação: "))
media = (nota1Aluno1 + nota2Aluno1)/2
media2 = (nota1Aluno2 + nota2Aluno2)/2
if media >= 7:
    print(f"Aprovado!")
elif media >= 5 and media < 7:
    print(f"Recuperação!")
else :
    print(f"Reprovado!")
if media2 >= 7:
    print(f"Aprovado!")
elif media2 >= 5 and media2 < 7:
    print(f"Recuperação!")
else :
    print(f"Reprovado!")