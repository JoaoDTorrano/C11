aluno = {}
aluno["nome"] = input("Nome do aluno: ")
aluno["media"] = float(input("Media do aluno: "))

aluno["situacao"] = "RP"
if aluno["media"] >= 50:
    aluno["situacao"] = "AP"

print("\n--- Dados do aluno ---")
for k, v in aluno.items():
    print(f"{k} - {v}")