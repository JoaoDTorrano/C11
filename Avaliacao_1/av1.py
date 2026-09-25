import numpy as np

dataset = np.loadtxt('shopping_trends.csv', delimiter= ',', dtype = 'str', encoding = "utf-8")
dados = dataset[1:,]
gender = dados[:,2]
age = dados[:,1].astype(int)

#1)
female = np.char.find(gender,'Female') >= 0
print(round(np.average(sum(age[female])/len(age[female])),2))


#2)
purchases = dados[:,5].astype(int)
media_purchases = int(sum(purchases)/len(purchases))

male = np.char.find(gender,'Male') >= 0

cont = 0

for x in purchases[male]:
    if x > media_purchases:
        cont = cont + 1
print(cont)


#3)
item = dados[:,3]
item_menos_vendido = item.argm
print(len(item_menos_vendido/len(item)))


#4)
desconto = dados[:, 11]
desconto_dado = np.char.find(desconto,'Yes') >= 0
print((len(purchases[desconto_dado])/len(purchases))*100)

#5)
category = dados[:,4]
category_clothing = np.char.find(category,'Clothing') >= 0
color = dados[:,8]
seson = dados[:,9]
summer = np.char.find(seson,'Summer') >= 0
color_clothing_seson = color[category_clothing & summer].argmin()
print(color[color_clothing_seson])




