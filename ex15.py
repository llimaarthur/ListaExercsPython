# Exercício 15 - Custo final da compra.

preco_unitario = float(input("Preço unitário: R$ "))
quantidade = int(input("Quantidade: "))
frete = float(input("Frete: R$ "))

subtotal = preco_unitario * quantidade
total = subtotal + frete

print(f"Subtotal: R$ {subtotal}")
print(f"Total: R$ {total}")

# Testes realizados conforme o documento
# Valores utilizados: R$ 10.00, com quantidade 3 e R$ 5.00 de frete,
# ------------------  R$ 49.90, com quantidade 2 e R$ 0.00 de frete e
# ------------------  R$ 7.50, com quantidade 10 e R$ 12.00 de frete.
