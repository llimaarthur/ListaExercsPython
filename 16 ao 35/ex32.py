# Exercício 32 - Número dentro do intervalo.

print("--------------------------------------------------")
print("")
print("           INTERVALO ENTRE 10 E 20...")
print("")
print("--------------------------------------------------")
print("")

print("Digite um número e descubra se o mesmo está dentro")
numero = float(input("do intervalo entre 10 e 20: "))
print("")

if numero >= 10 and numero <= 20:
    print("DENTRO.")

else:
    print("FORA.")

# Testes realizados conforme o documento!
# Entradas utilizadas: 10, 15.5, 20 e 20.1