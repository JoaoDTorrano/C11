preco_original = float(input('Valor original do produto: R$'))
desconto = preco_original*0.05
preco_final = preco_original - desconto

print('O valor depois do desconto é R${:.2f}'.format(preco_final))