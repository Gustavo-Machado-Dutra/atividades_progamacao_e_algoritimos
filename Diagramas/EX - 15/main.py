preco_unitario = float(input("Digite o preço unitário do produto: R$ "))
quantidade = int(input("Digite a quantidade comprada: "))
frete = float(input("Digite o valor do frete: R$ "))

subtotal = preco_unitario * quantidade
total = subtotal + frete

print("Subtotal dos produtos: R$", subtotal)
print("Valor total da compra: R$", total)