import pandas as pd

mamifero = pd.read_csv('csv/mammal-neck-bones.csv')
print(mamifero.head())
print('--------------------------------------------------------')
print(mamifero.query('species == "giraffe"'))
print('--------------------------------------------------------')
print(mamifero.query('neck_vertebrae != 7'))
print('--------------------------------------------------------')
