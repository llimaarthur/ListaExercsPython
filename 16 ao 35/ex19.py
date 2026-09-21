# Exercício 19 - Maior e menor de três números.

n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
n3 = float(input("Digite o terceiro valor: "))

print(f"Valores: {n1}, {n2}, {n3}")

if n1 == n2 == n3:
    print("Todos os valores são iguais, não há um maior e um menor.")

elif n1 >= n2 >= n3:
    print(f"Maior: {n1}")
    print(f"Menor: {n3}")

elif n2>= n1 >= n3:
    print(f"Maior: {n2}")
    print(f"Menor: {n3}")

elif n3 >= n2 >= n1:
    print(f"Maior: {n3}")
    print(f"Menor: {n1}")

elif n2 >= n3 >= n1:
    print(f"Maior: {n2}")
    print(f"Menor: {n1}")

elif n3 >= n1 >= n2:
    print(f"Maior: {n3}")
    print(f"Menor: {n2}")

else:
    print(f"Maior: {n1}")
    print(f"Menor: {n2}")

# Testes realizados conforme o documento!
# Entradas utilizadas: 3, 9 e 5, -4, -1 e -7, 6, 6  e 2.