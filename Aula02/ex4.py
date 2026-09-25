pessoas = []

for cont in range(0, 3):
    pessoa = {}
    pessoa["nome"] = input(f"Nome da pessoa {cont + 1}: ")
    pessoa["peso"] = float(input(f"Peso da pessoa {cont + 1}: "))
    pessoas.append(pessoa)

maior_nome = pessoas[0]["nome"]
maior_peso = pessoas[0]["peso"]
menor_nome = pessoas[0]["nome"]
menor_peso = pessoas[0]["peso"]

for p in pessoas:
    if p["peso"] > maior_peso:
        maior_peso = p["peso"]
        maior_nome = p["nome"]
    if p["peso"] < menor_peso:
        menor_peso = p["peso"]
        menor_nome = p["nome"]

print(f"\nA pessoa mais pesada e {maior_nome} com {maior_peso}kg")
print(f"A pessoa mais leve e {menor_nome} com {menor_peso}kg")