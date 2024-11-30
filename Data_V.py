import pandas as pd
data = {'Name': ['Mxo', 'Gee', 'Sjijo'],
        'Age': [25, 30, 35],
        'City': ['Kagiso', 'Randfontein', 'Swanevillle']}

df = pd.DataFrame(data)
print(df)

df_filtered = df[df['Age'] > 30]


import matplotlib.pyplot as plt

plt.plot(df['Name'], df['Age'])
plt.xlabel('Name')
plt.title('Name vs Age')
plt.show()


df.groupby('City')['Age'].mean().plot(kind='bar')
plt.xlabel('City')
plt.ylabel('Average Age')
plt.title('Average Age by City')
plt.show()


df['Age'].plot(kind='hist', bins=10)
plt.xlabel('Age')
plt.title('Age Distribution')
plt.show()


df.plot(kind='scatter', x='City', y='Age')
plt.title('City vs Age')
plt.show()