valCompra = float(input("Digite o valor da compra: "))

if valCompra < 20.00:
    lucro = 0.45
else:
    lucro = 0.30

# Calcula o valor de venda
valVenda = valCompra * (1 + lucro)

print(f"Valor de venda: R${valVenda:.2f}")