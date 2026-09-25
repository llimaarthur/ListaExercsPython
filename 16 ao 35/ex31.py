# Exercício 31 - Divisível por 3 e por 5.

print("-----------------------------------")
print("")
print("     DIVIDINDO POR 3 E POR 5...")
print("")
print("------------------------------------")
print("")


numero = int(input("Digite um número: "))
print("")

if  numero % 3 == 0 and numero % 5 == 0:
    print("DIVISÍVEL POR 3 E POR 5")

elif numero % 3 == 0:
    print("DIVISÍVEL APENAS POR 3 ")

elif numero % 5 == 0: 
    print("DIVISÍVEL APENAS POR 5")

else:
    print("NÃO DIVÍSIVEL POR 3 NEM POR 5")


# Testes realizados conforme o documento!
# Entradas utilizadas: 30, 9 , 20 e 7.