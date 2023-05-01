#Ista 131, by: Daniel Peabody
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.stats import linregress

data = pd.read_csv('AZhousingData.csv')

x = data['sqft']
y = data['Price']

plt.scatter(x,y,marker='^',c='g')
slope, intercept, rvalue, pvalue, stderr = linregress(x, y)
regress_values = slope * x + intercept
plt.plot(x, regress_values, color='red')
plt.gca().set_facecolor('lightgray')
fig = plt.gcf()
fig.patch.set_facecolor('lightgray')

plt.title('Housing Price vs Square Feet',fontsize = 40,family = 'fantasy')
plt.xlabel('Square Feet',fontsize = 25,family = 'fantasy')
plt.ylabel('Price in $',fontsize = 25,family = 'fantasy')
plt.ylim(0, 4000000)
plt.xlim(0,6000)
plt.xticks(fontname = "impact",fontsize = 14)
plt.yticks(fontname = "impact",fontsize = 14)
plt.ticklabel_format(axis='y', style='plain')
plt.show()


