import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# formatação dos eixos
def format_axes():
    plt.xlabel('Speed (km/h)')
    plt.ylabel('Stopping distance (m)')
    plt.axhline(color='black', alpha=0.5, linestyle='--')
    plt.axvline(color='black', alpha=0.5, linestyle='--')

# modelo quadrático
class QuadraticModel:
    def fit(self, x, y):
        x = pd.DataFrame(x)
        quadratic = PolynomialFeatures(degree=2)
        quad_features = quadratic.fit_transform(x)
        quad_model = LinearRegression().fit(quad_features, y)
        y_pred = quad_model.predict(quad_features)
        self.a = quad_model.coef_[2]
        self.b = quad_model.coef_[1]
        self.c = quad_model.intercept_
        self.rsquared = r2_score(y, y_pred)
        
    def predict(self, x):
        return self.a*x**2 + self.b*x + self.c
       
    def plot_model(self, xmin, xmax):
        xvals = range(xmin, xmax+1)
        yvals = [self.predict(x) for x in xvals]
        plt.plot(xvals, yvals, color='black')
        
    def print_model_info(self):
        a = self.a
        b = self.b
        c = self.c
        rsquared = self.rsquared
        print('QuadraticModel')
        print(f'Parameters: a = {a:.2f}, b = {b:.2f}, c = {c:.2f}')
        print(f'Equation: y = {self.a:.2f}x² + {self.b:.2f}x + {self.c:.2f}')
        print(f'Goodness of Fit (R²): {rsquared:.3f}')

df = pd.read_csv('csv/ebike-stopping-distances.csv')
df_low = pd.read_csv('csv/ebike-data-low-speed.csv')
df_high = pd.read_csv('csv/ebike-data-high-speed.csv')

df_all = pd.concat([df, df_low, df_high])
quadratic = QuadraticModel()
quadratic.fit(df_all['speed'], df_all['distance'])
quadratic.print_model_info()
plt.scatter(df['speed'], df['distance'], color = 'C0', alpha=0.5)
plt.scatter(df_low['speed'], df_low['distance'], color = 'C1', alpha=0.5)
plt.scatter(df_high['speed'], df_high['distance'], color = 'C2', alpha=0.5)
quadratic.plot_model(xmin=0, xmax=61)
format_axes()
plt.show()
