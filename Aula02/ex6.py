ingredientes = ["farinha", "ovos", "leite", "acucar", "manteiga"]
print(f"Receita inicial: {ingredientes}")

ingredientes.append("fermento")
print(f"a) Depois do append: {ingredientes}")

ingredientes.insert(2, "chocolate")
print(f"b) Depois do insert: {ingredientes}")

if "manteiga" in ingredientes:
    ingredientes.remove("manteiga")
print(f"c) Depois do remove: {ingredientes}")