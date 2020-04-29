import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

print(df.columns)
print(df.shape)
print(df.head(10))
print(df.tail(7))
print(df.isna().sum())
print(df.describe())
print(df.dtypes)
print(df.info())
print(df['sepal length (cm)'].value_counts())

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['sepal length (cm)'] = le.fit_transform(df['sepal length (cm)'])
df['sepal width (cm)'] = le.fit_transform(df['sepal width (cm)'])
df['petal length (cm)'] = le.fit_transform(df['petal length (cm)'])
df['petal width (cm)'] = le.fit_transform(df['petal width (cm)'])

X = df[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']]

from sklearn.cluster import KMeans
model = KMeans(n_clusters=4)
model.fit(X)
print(model.predict(X))

import matplotlib.pyplot as plt
data = [[[1] * len(df['sepal length (cm)']), df['sepal length (cm)']],
        [[2] * len(df['sepal width (cm)']) , df['sepal width (cm)']],
        [[3] * len(df['petal length (cm)']) , df['petal length (cm)']],
        [[4] * len(df['petal width (cm)']) , df['petal width (cm)']]]
plt.scatter(data[0][0], data[0][1], color = 'blue')
plt.scatter(data[1][0], data[1][1], color = "yellow")
plt.scatter(data[2][0], data[2][1], color = "brown")
plt.scatter(data[3][0], data[3][1], color = "green")
plt.show()