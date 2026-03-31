import pandas as pd
import matplotlib.pyplot as plt

passaro = pd.read_csv('csv/bird-neck-bones.csv')
print(passaro.head())
print('--------------------------------------------------------')
print(passaro.query('neck_vertebrae == neck_vertebrae.max()'))
contar_passaro = passaro['neck_vertebrae'].value_counts()
contar_passaro = contar_passaro.sort_index()
contar_passaro.plot.bar()
plt.show()