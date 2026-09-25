salario_atual = float(input('Salária atual é de R$'))
aumento = salario_atual*0.15
salario_novo = salario_atual + aumento

print('O salário novo apos o aumento de 15% é de R${:.2f}'.format(salario_novo))