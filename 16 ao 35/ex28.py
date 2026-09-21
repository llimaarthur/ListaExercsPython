# Exercício 28 - É possível formar um triângulo?

print("")
print("-------------------------------------------")
print("")
print("         FORMANDO UM TRIÂNGULO!")
print("")
print("-------------------------------------------")
print("")

lado1 = float(input("Digite a primeira medida: "))
lado2 = float(input("Digite a segunda medida: "))
lado3 = float(input("Digite a terceira medida: "))

if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2):
    print("")
    print("Resultado: FORMAM UM TRIÂNGULO")
    print("")

else:
    print("")
    print("Resultado: NÃO FORMAM UM TRIÂNGULO")
    print("")

# Testes realizados conforme o documento!
# Entradas utilizadas: 2, 2, 3 | 1, 2 ,3 | 5, 5, 10