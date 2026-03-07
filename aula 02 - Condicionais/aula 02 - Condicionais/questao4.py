##Crie um programa que: Solicite ao usuário três notas (use input() e converta para float). Calcule a média aritmética dessas três notas. Exiba a situação acadêmica do aluno seguindo as regras: "Aprovado" → média maior ou igual a 7.0 "Recuperação" → média maior ou igual a 5.0 e menor que 7.0 "Reprovado" → média menor que 5.0

n1Aluno1 = float (input("Digite a nota do aluno na primeira avaliação: "))
n2Aluno1 = float (input("Digite a nota do aluno na segunda avaliação: "))
n3Aluno1 = float (input("Digite a nota do aluno na segunda avaliação: "))
media = (n1Aluno1 + n2Aluno1 + n2Aluno1)/3
if media >= 7.0:
    print(f"Aprovado!")
elif media >= 5:
    print(f"Recuperação!")
else :
    print(f"Reprovado!")