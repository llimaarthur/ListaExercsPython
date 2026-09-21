# Exercício 26 - Reajuste por faixa salarial.

print("-------------------------------------------------------------------")
print("")
print("         ATENÇÃO! ESTAMOS PASSANDO POR REAJUSTES SALARIAIS.")
print("")
print("     Informe-nos abaixo seu salário para que possamos calculá-lo")
print("         conforme os reajustes e mostrarmos os novos valores!")
print("")
print("-------------------------------------------------------------------")
print("")
print("-------------------------------------------------------------------")
print("")
print("                         FAIXAS SALARIAIS!")
print("")
print("         Até R$ 1500.00 - 15 por cento de aplicação.")
print("         De R$ 1500.01 até R$ 3000.00 - 10 por cento de aplicação.")
print("         Acima de R$ 3000.00 - 5 por cento de aplicação.")
print("")
print("-------------------------------------------------------------------")

salario = float(input("Digite o seu salário: R$ "))

if salario <= 1500:
    aumento1 = salario * 0.15
    salario_novo1 = salario + aumento1

    print("Percentual aplicado: 15%")
    print(f"Valor do aumento: R$ {aumento1}")
    print(f"Novo salário: R$ {salario_novo1}")

elif 1500.01 <= salario <= 3000:
    aumento2 = salario * 0.10
    salario_novo2 = salario + aumento2

    print("Percentual aplicado: 10%")
    print(f"Valor do aumento: R$ {aumento2}")
    print(f"Novo salário: R$ {salario_novo2}")

else:
    aumento3 = salario * 0.05
    salario_novo3 = salario + aumento3

    print("Percentual aplicado: 5%")
    print(f"Valor do aumento: R$ {aumento3}")
    print(f"Novo salário: R$ {salario_novo3}")

# Testes realizados conforme o documento!
# Entradas utilizadas: R$ 1500.00, R$ 3000.00 e R$ 4000.00.