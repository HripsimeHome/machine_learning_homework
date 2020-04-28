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
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], df['petal length (cm)'], df['petal width (cm)'])
plt.show()