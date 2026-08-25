# Exercício 23 - Categoria de votação.

print("Olá, para consultar sobre o seu voto precisaremos apenas que você nos informe a sua idade!")
idade = int(input("Digite sua idade: "))

if idade < 16:
    print("NÃO PODE VOTAR")

elif idade == 16 or idade == 17:
    print("VOTO OPCIONAL")

elif idade >= 18 and idade <= 69:
    print("VOTO OBRIGATÓRIO")

else:
    print("VOTO OPCIONAL")

# Testes realizados conforme o documento!
# Entradas utilizadas: 15, 16, 18, 70.