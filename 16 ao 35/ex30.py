# Exercício 30 - Aprovação de empréstimo.

import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UFT-8')

print("")
print("-----------------------------------")
print("")
print("     APROVAÇÃO DE EMPRÉSTIMO!")
print("")
print("-----------------------------------")
print("")

valor_imovel = float(input("Por favor digite o valor do ímovel: R$ "))
salario_mensal = float(input("Por favor digite seu salário mensal: R$ "))
prazo = int(input("Por favor digite o prazo de pagamento em anos: "))

prestacao = valor_imovel / (prazo * 12)
limite = salario_mensal * 0.30

if prestacao <= limite:
    print("")
    print(f"Valor do imóvel: {locale.currency(valor_imovel, grouping=True)}")
    print(f"Salário: {locale.currency(salario_mensal, grouping=True)}")
    print(f"Prazo: {prazo} anos")
    print("")
    print(f"Prestação: {locale.currency(prestacao, grouping=True)}")
    print(f"Limite: {locale.currency(limite, grouping=True)}")
    print("Resultado: APROVADO")
    print("")

else:
    print("")
    print(f"Valor do imóvel: {locale.currency(valor_imovel, grouping=True)}")
    print(f"Salário: {locale.currency(salario_mensal, grouping=True)}")
    print(f"Prazo: {prazo} anos")
    print("")
    print(f"Prestação: {locale.currency(prestacao, grouping=True)}")
    print(f"Limite: {locale.currency(limite, grouping=True)}")
    print("Resultado: NEGADO")
    print("")
    
# Testes realizados conforme o documento!
# Entradas utilizadas (imóvel, salário, anos): R$ 120.000, R$ 2.000, 20 | R$ 300.000, R$ 3.000, 15 | R$ 216.000, R$ 2.000, 30
    