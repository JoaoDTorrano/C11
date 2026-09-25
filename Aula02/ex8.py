produtos = []

for cont in range(0, 3):
    produto = {}
    produto["nome"] = input(f"\nNome do produto {cont + 1}: ")
    produto["preco"] = float(input(f"Preco do produto {cont + 1}: "))
    produto["quantidade"] = int(input(f"Quantidade em estoque do produto {cont + 1}: "))
    produtos.append(produto)

print("\n--- Valor total em estoque ---")
for p in produtos:
    total = p["preco"] * p["quantidade"]
    print(f"{p['nome']}: R$ {total}")