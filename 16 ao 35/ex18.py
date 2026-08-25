# Exercício 18 - Maior de dois números.

n1 = float(input("Primeiro valor: "))
n2 = float(input("Segundo valor: "))

if n1 > n2:
    print(f"Maior valor: {n1}")

elif n2 > n1:
    print(f"Maior valor: {n2}")

else:
    print("VALORES IGUAIS")

# Testes realizados conforme o documento!
# Entradas utilizadas: 4 e 9, -2 e -8, 5 e 5.