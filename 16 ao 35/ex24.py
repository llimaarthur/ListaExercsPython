# Exercício 24 - Ano bissexto.

ano = int(input("Ano: "))

if ano % 400 == 0:
    print("Resultado: ANO BISSEXTO")

else:
    print("Resultado: NÃO BISSEXTO")


# Testes realizados conforme o documento!
# Entradas utilizadas: 2024, 1900, 2000 e 2023.