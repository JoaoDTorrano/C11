n = int(input("Quantas pessoas serao cadastradas? "))

pessoas = []

for cont in range(0, n):
    pessoa = {}
    pessoa["nome"] = input(f"\nNome da pessoa {cont + 1}: ")
    pessoa["idade"] = int(input(f"Idade da pessoa {cont + 1}: "))
    pessoa["sexo"] = input(f"Sexo da pessoa {cont + 1} (digite M ou F): ")
    pessoas.append(pessoa)

soma_idades = 0
mulheres_jovens = 0

for p in pessoas:
    soma_idades = soma_idades + p["idade"]
    if p["sexo"] == "F" and p["idade"] < 20:
        mulheres_jovens = mulheres_jovens + 1

media = soma_idades / len(pessoas)

print(f"\nA media de idade do grupo e {media} anos")
print(f"Existem {mulheres_jovens} mulher(es) com menos de 20 anos")