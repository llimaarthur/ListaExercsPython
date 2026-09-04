# Exercício 35 - Valor do ingresso.

import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

print("-------------------------------------------")
print("")
print("         APLICAÇÃO MEIA ENTRADA!")
print("")
print("-------------------------------------------")
print("")

idade = int(input("Digite a sua idade: "))
print("")
estudante = input("Você é estudante? (S/N): ").upper()
print("")

ingresso = 30
meia = ingresso - (ingresso * 0.50)

if estudante != 'S' and estudante != 'N':
    print("Por favor, digite apenas Sim ou Não (S/N).")

elif idade > 12 and idade < 60 and estudante == 'S':
    print(f"Idade: {idade} anos")
    print("")
    print("Estudante: Sim")
    print("")
    print(f"Valor do ingresso: {locale.currency(meia, grouping=True)}")

elif idade <= 12:
    print(f"Idade: {idade} anos")
    print("")

    if estudante == 'S':
        print("Estudante: Sim")
        print("")

    elif estudante == 'N':
        print("Estudante: Não")
        print("")

    print(f"Valor do ingresso: {locale.currency(meia, grouping=True)}")
    

elif idade >= 60:
    print(f"Idade: {idade} anos")
    print("")

    if estudante == 'S':
            print("Estudante: Sim")
            print("")
    
    elif estudante == 'N':
        print("Estudante: Não")
        print("")

    print(f"Valor do ingresso: {locale.currency(meia, grouping=True)}")

elif estudante == 'N':
    print(f"Idade: {idade} anos")
    print("")
    print("Estudante: Não")
    print("")
    print(f"Valor do ingresso: {locale.currency(ingresso, grouping=True)}")

# Testes realizados conforme o documento!
# Entradas utilizadas: 10, NÃO | 25, SIM | 65, NÃO | 30, NÃO
