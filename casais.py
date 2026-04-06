import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('csv/how-couples-met.csv')

#estilizando gráfico 

focus_column = 'online'
focus_color = 'C3'
back_columns = ['college', 'at work','through friends', 'through family', 'restaurant', 'neighbors']
back_colors = ['C0', 'C1', 'C2', 'C4', 'C5', 'C6']

def add_end_labels(df, x , column_names, alpha):
    for column_name in column_names:
        y = df[column_name].iloc[-1]
        label = f'{column_name}'
        plt.text(x, y, label, va='center',alpha=alpha)

def plot_data():
    df.plot(y=back_columns, color = back_colors, alpha=0.5)
    plt.plot(df.index, df[focus_column], color=focus_color, linewidth=5)

def label_lines():
    plt.legend().set_visible(False)
    add_end_labels(df, 2010, back_columns, alpha=0.5)
    add_end_labels(df, 2010, ['online'], alpha=1)

def clean_axes():
    ax = plt.gca()
    ax.spines[['left', 'right', 'top']].set_visible(False)
    ax.tick_params(axis='y', length=0)
    plt.grid(axis='y', alpha=0.5)

def add_axes_labels():
    y_ticks = [0, 10, 20, 30, 40, 50]
    y_tick_labels = ['0', '10', '20', '30', '40', '50%']
    plt.yticks(y_ticks, y_tick_labels)
    plt.xlabel('Decade')


print(df.head())
plot_data()
label_lines()
clean_axes()
add_axes_labels()
plt.title('How Couples Met Over Time')
plt.show()