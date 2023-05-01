#Ista 131, by: Daniel Peabody
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset and extract the relevant columns
data = pd.read_csv('AZhousingData.csv')
df = data[['baths', 'sqft']]

# Group the data by number of bathrooms and calculate the mean square footage
grouped = df.groupby('baths')['sqft'].mean()

# Create the bar chart
fig, ax = plt.subplots()
bars = ax.bar(grouped.index.astype(str), grouped.values)
bars[1].set_hatch('//')
bars[3].set_hatch('//')
bars[5].set_hatch('//')
bars[7].set_hatch('//')
bars[9].set_hatch('//')

plt.xlabel('Number of Bathrooms',fontsize = 25,family = 'fantasy')
plt.ylabel('Square Footage',fontsize = 25,family = 'fantasy')
plt.title('Average Square Footage by Number of Bathrooms',fontsize = 40,family = 'fantasy')
plt.xticks(fontname = "impact",fontsize = 14)
plt.yticks(fontname = "impact",fontsize = 14)
plt.gca().set_facecolor('lightgray')
fig = plt.gcf()
fig.patch.set_facecolor('lightgray')
plt.show()
