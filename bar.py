#Ista 131, by: Daniel Peabody
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset and extract the bedroom column
data = pd.read_csv('AZhousingData.csv')
bedrooms = data['beds']

# Count the number of entries for each bedroom count
bedroom_counts = bedrooms.value_counts()

# Create the bar chart
fig, ax = plt.subplots()
ax.bar(bedroom_counts.index, bedroom_counts.values,color='r')
plt.xlabel('Number of Bedrooms',fontsize = 25,family = 'fantasy',c='w')
plt.ylabel('Frequency',fontsize = 25,family = 'fantasy',c='w')
plt.title('Frequency of Bedrooms in Housing Market',fontsize = 40,family = 'fantasy',c='w')
plt.xticks(fontname = "impact",fontsize = 14,c='w')
plt.yticks(fontname = "impact",fontsize = 14,c='w')
plt.gca().set_facecolor('darkgray')
fig = plt.gcf()
fig.patch.set_facecolor('black')
plt.show()
