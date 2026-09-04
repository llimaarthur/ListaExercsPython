# Exercício 35 - Valor do ingresso.

import locale
locale.setLocale(locale.LC_ALL, 'pt_BR.UFT-8')

idade = int(input("Digite a sua idade: "))
estudante = str(input("Você é estudante? (S/N): "))

ingresso = 30
meia = ingresso - (ingresso * 0.50)

if idade <= 12:
    print(f"Valor do ingresso: {locale.currency(meia, grouping=True)}")

elif idade >= 60:
    print(f"Valor do ingresso: {locale.currency(meia, grouping=True)}")

elif idade > 12 and estudante == 'S':
    print(f"Valor do ingresso: {locale.currency(meia, grouping=True)}")

elif estudante == 'N':
    print(f"Valor do ingresso: {locale.currency(ingresso, grouping=True)}")

else:
    print("")



