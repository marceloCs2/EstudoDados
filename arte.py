import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def pintar(painting_id):
    rects = features.query('painting_id == @painting_id')
    total_width = rects.eval('x + width').max()
    total_height = rects.eval('y + height').max()
    fig, ax = plt.subplots()
    for(idx,row) in rects.iterrows():
        x,y,w,h,rgb = row[['x','y','width','height','rgb']]
        patch = mpatches.Rectangle((x,y),w,h,facecolor=rgb)
        ax.add_patch(patch)
    ax.axis([0,total_width,0,total_height])
    ax.set_aspect('equal')
    ax.axis('off')
    plt.text(0.5,0.01, painting_id, ha='center', fontsize=14)
    plt.show()




features = pd.read_csv('csv/mondrian-painting-features.csv')
print('----------------------Pinturas--------------------')
print(features.head())
print('----------------------b104--------------------')
print(features.query('painting_id == "b104"').head())
print('----------------------informações--------------------')
informacoes = pd.read_csv('csv/mondrian-painting-info.csv')
print(informacoes.head())
print('----------------------Pintar--------------------')
print(pintar('b104'))
print(pintar('b105'))
print('----------------------tamanho features-------------------- ')
sizes = features.groupby('painting_id').size()
print(sizes)
print('----------------------resetar o index e alterar nome de coluna-------------------- ')
complexity_df = sizes.reset_index(name='complexity')
print(complexity_df)
print('----------------------gráfico scatter-------------------- ')
informacoes = informacoes.merge(complexity_df, on='painting_id', how='left')
plt.scatter(informacoes['year'], informacoes['complexity'])
plt.xlabel('Year')
plt.ylabel('Complexity')
plt.show()