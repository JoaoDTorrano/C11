loja_a = {"iPhone 13", "Galaxy S22", "Moto G54", "Xiaomi 13", "Galaxy S22"}
loja_b = {"Galaxy S22", "Xiaomi 13", "Pixel 8", "Moto G54"}

print(f"Loja A vende: {loja_a}")
print(f"Loja B vende: {loja_b}")

todos = loja_a | loja_b
print(f"\nVisitando as duas lojas, posso comprar: {todos}")

ambas = loja_a & loja_b
print(f"Disponiveis em ambas as lojas: {ambas}")