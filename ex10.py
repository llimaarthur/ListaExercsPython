# Exercício 10 - Salário com comissão.

salario_fixo = float(input("Salário fixo: R$ "))
total_vendido = float(input("Total vendido: R$ "))

comissao = total_vendido * 0.04
salario_total = salario_fixo + comissao

print(f"Comissão: R$ {comissao}")
print(f"Salário total: R$ {salario_total}")

# Testes realizados conforme o documento
# Valores utilizados: R$1.500,00, R$ 2.000,00 E R$ 2.500,00.