import numpy as np

mtz1 = np.zeros((2, 2))
mtz2 = np.random.randint(0, 2, 4)
mtz2 = mtz2.reshape(2, 2)

seguras = 4 - np.sum(mtz2)  # posicoes em que o numero 1 nao se encontra
acertos = 0
jogada = 0
perdeu = False

while acertos < seguras:
    l = int(input("Linha (0 ou 1): "))
    c = int(input("Coluna (0 ou 1): "))
    jogada = jogada + 1

    if mtz2[l][c] == 1:
        if jogada <= 3:
            perdeu = True
            break
    else:
        if mtz1[l][c] == 0:
            mtz1[l][c] = 1  # marca a posicao segura ja jogada
            acertos = acertos + 1

print(mtz1)

if perdeu:
    print("Game Over! :( Try Again!")
else:
    print("Congratulations! You beat the game! :)")