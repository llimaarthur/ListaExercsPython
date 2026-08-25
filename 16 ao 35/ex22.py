# Exercício 22 - Situação do aluno por faixa.

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

if media < 5:
    print(f"Média: {media}")
    print("Situação: REPROVADO")

elif media >= 5 and media < 7:
    print(f"Média: {media}")
    print("Situação: RECUPERAÇÃO")

else:
    print(f"Média: {media}")
    print("Situação: APROVADO")

# Testes realizados conforme o documento!
# Entradas utilizadas: 4.0 e 5.0, 5.0 e 5.0, 7.0 e 7.0.