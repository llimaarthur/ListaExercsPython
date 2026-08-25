# Exercício 21 - Aprovado ou reprovado.

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"Média: {media}")
    print("Situação: APROVADO")

else:
     print(f"Média: {media}")
     print("Situação: REPROVADO")


# Testes realizados conforme o documento!
# Entradas utilizadas: 5.0 e 8.0, 7.0 e 7.0, 10.0 e 9.0.