import pandas as pd
import matplotlib.pyplot as plt


print('----------------------Esqueleto Humano--------------------')
df = pd.read_csv('csv/adult-human-skeleton.csv')
print(df.head())
print('--------------------------------------------------------')
print(df['region'].value_counts())
print('--------------------------------------------------------')
print(df.sort_values(by='fused_from', ascending=False).head())
print('--------------------------------------------------------')
print(df.query('region == "neck"'))

print('----------------------Mamiferos--------------------')

mamifero = pd.read_csv('csv/mammal-neck-bones.csv')
print(mamifero.head())
print('--------------------------------------------------------')
print(mamifero.query('species == "giraffe"'))
print('--------------------------------------------------------')
print(mamifero.query('neck_vertebrae != 7'))
print('--------------------------------------------------------')

print('----------------------Passaros--------------------')

passaro = pd.read_csv('csv/bird-neck-bones.csv')
print(passaro.head())
print('--------------------------------------------------------')
print(passaro.query('neck_vertebrae == neck_vertebrae.max()'))
contar_passaro = passaro['neck_vertebrae'].value_counts()
contar_passaro = contar_passaro.sort_index()
contar_passaro.plot.bar()
plt.show()