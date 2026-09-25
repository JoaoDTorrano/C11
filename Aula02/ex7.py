ingredientes = ["farinha", "ovos", "leite", "acucar", "manteiga"]
ingredientes.append("fermento")
ingredientes.insert(2, "chocolate")
if "manteiga" in ingredientes:
    ingredientes.remove("manteiga")

print(f"Ingredientes da receita: {ingredientes}")

pessoa1 = {"farinha", "ovos", "sal"}
pessoa2 = {"leite", "ovos", "fermento", "cafe"}

print(f"Pessoa 1 tem em casa: {pessoa1}")
print(f"Pessoa 2 tem em casa: {pessoa2}")

tem_em_casa = pessoa1 | pessoa2

falta_comprar = []
for item in ingredientes:
    falta_comprar.append(item)

for item in tem_em_casa:
    if item in falta_comprar:
        falta_comprar.remove(item)

print(f"\nAinda falta comprar: {falta_comprar}")