# Exercício 29 - Tipo de triângulo

print("----------------------------------------------")
print("")
print("FORMANDO UM TRIÂNGULO E DESCOBRINDO SEU TIPO!")
print("")
print("----------------------------------------------")
print("")

lado1 = float(input("Digite a primeira medida: "))
lado2 = float(input("Digite a segunda medida: "))
lado3 = float(input("Digite a terceira medida: "))

if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2):
    print("")
    print("Resultado: FORMAM UM TRIÂNGULO")
    print("")

    if lado1 == lado2 == lado3:
        print("Tipo: EQUILÁTERO")
        print("")

    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Tipo: ISÓSCELES")
        print("")

    else:
        print("Tipo: ESCALENO")
        print("")

else:
    print("")
    print("Resultado: NÃO FORMAM UM TRIÂNGULO")
    print("")

# Testes realizados conforme o documento!
# Entradas utilizadas: 5, 5, 5 | 5, 5, 3 | 3, 4, 5 | 1, 2, 3