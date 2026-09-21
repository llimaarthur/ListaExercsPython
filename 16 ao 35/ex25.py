# Exercício 25 - Preço conforme a forma de pagamento.

preco_produto = float(input("Preço: R$ "))

print("------------------------------------------------------")
print("                     OPÇÕES")
print("")
print("     1 - DINHEIRO OU PIX (10 por cento de desconto)")
print("     2 - DÉBITO (5 por cento de desconto)")
print("     3 - CRÉDITO A VISTA (Sem alteração)")
print("     4 - CRÉDITO PARCELADO (8 por cento de acréscimo)")
print("")
print("------------------------------------------------------")

opcao = int(input("Opção: "))

if opcao == 1:
    desconto1 = preco_produto - (preco_produto * 0.10)
    print(f"Valor final: R$ {desconto1}")

elif opcao == 2:
    desconto2 = preco_produto - (preco_produto * 0.05)
    print(f"Valor final: R$ {desconto2}")

elif opcao == 3:
    print(f"Valor final: R$ {preco_produto}")

elif opcao == 4:
    acrescimo = preco_produto + (preco_produto * 0.08)
    print(f"Valor final: R$ {acrescimo}")

else:
    print("OPÇÃO NÃO EXISTENTE.")

# Testes realizados conforme o documento!
# Entradas utilizadas: R$ 100.00 | Opção 2, R$ 100.00 | Opção 3 e R$ 100.00 | Opção 4.