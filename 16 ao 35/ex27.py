# Exercício 27 - Classificação de IMC.

print("------------------------------------------------")
print("")
print("             CÁLCULO DE IMC!")
print("")
print("------------------------------------------------")

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
print("")

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Peso: {peso: .2f} kg")
    print(f"Altura: {altura: .2f} m")
    print("")
    print(f"IMC: {imc: .2f}")
    print("Classificação: ABAIXO DA FAIXA")

elif imc >= 18.5 and imc <= 25:
    print(f"Peso: {peso: .2f} kg")
    print(f"Altura: {altura: .2f} m")
    print("")
    print(f"IMC: {imc: .2f}")
    print("Classificação: FAIXA NORMAL")

elif imc >= 25 and imc <= 30:

    print(f"Peso: {peso: .2f} kg")
    print(f"Altura: {altura: .2f} m")
    print("")
    print(f"IMC: {imc: .2f}")
    print("Classificação: ACIMA DA FAIXA")

else:
    print(f"Peso: {peso: .2f} kg")
    print(f"Altura: {altura: .2f}")
    print("")
    print(f"IMC: {imc: .2f}")
    print("Classificação: FAIXA ELEVADA")
    
# Testes realizados conforme o documento!
# Entradas utilizadas: 50kg, 1.70m | 80kg, 1.80m | 90kg, 1.70m
