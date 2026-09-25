# Exercício 34 - Quantidade de dias do mês.

print("--------------------------------------")
print("")
print("     QUANTIDADE DE DIAS DO MÊS!")
print("")
print("-------------------------------------")
print("")

mes = int(input("Digite um mês (1 a 12): "))
print("")

ano = int(input("Digite um ano: "))
print("")

if mes in [1, 3, 5, 7, 9, 10, 12]:
    print("POSSUI 31 DIAS.")

elif mes in [4,6, 9, 11]:
    print("POSSUI 30 DIAS.")

elif mes == 2 and (ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)):
    print("POSSUI 29 DIAS.")

elif mes == 2:
    print("POSSUI 28 DIAS.")

else:
    print("MÊS INVÁLIDO.")

# Testes realizados conforme o documento!
# Entradas utilizadas: Mês: 2, Ano: 2024 | Mês: 2, Ano: 2023 |
# Mês: 4, Ano: 2026 | Mês: 12, Ano: 2026 | Mês: 13, Ano: 2026