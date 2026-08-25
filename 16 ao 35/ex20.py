# Exercício 20 - Três números em ordem crescente.

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))

print(f"Valores: {n1}, {n2}, {n3}")

if n1 == n2 == n3:
    print("Valores iguais, não existe uma ordem.")

elif n1 >= n2 >= n3:
    print(f"Ordem crescente: {n3}, {n2}, {n1}")

elif n2 >= n1 >= n3:
    print(f"Ordem crescente: {n3}, {n1}, {n2}")

elif n3 >= n1 >= n2:
    print(f"Ordem crescente: {n2}, {n1}, {n3}")

elif n1 >= n3 >= n2:
    print(f"Ordem crescente: {n2}, {n3}, {n1}")

elif n2 >= n3 >= n1:
    print(f"Ordem crescente: {n1}, {n3}, {n2}")

else:
    print(f"Ordem crescente: {n1}, {n2}, {n3}")


# Testes realizados conforme o documento!
# Entradas utilizadas: 3, 1 e 2, 7, 7 e 4, -1, -5 e 0.