import pandas as pd

# Sunk@ tunavor e te voch
mashrooms_data= pd.read_csv('mushrooms.csv')
print(mashrooms_data.shape)
print(mashrooms_data.columns)
print(mashrooms_data.isna().sum())
print(mashrooms_data.head(10))
print (mashrooms_data.tail(10))
print(mashrooms_data.info())

print(mashrooms_data['class'].head(10)) # Sa y-na: Tunavora, tunavor chi

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
mashrooms_data['class'] = le.fit_transform (mashrooms_data['class'])

mashrooms_data['cap-shape'] = le.fit_transform(mashrooms_data['cap-shape'])
mashrooms_data['cap-color'] = le.fit_transform(mashrooms_data['cap-color'])
mashrooms_data['ring-number'] = le.fit_transform(mashrooms_data['ring-number'])
mashrooms_data['gill-size'] = le.fit_transform(mashrooms_data['gill-size'])
mashrooms_data['gill-color'] = le.fit_transform(mashrooms_data['gill-color'])
#print(mashrooms_data.info())

X = mashrooms_data[['cap-shape', 'cap-color', 'ring-number', 'gill-size', 'gill-color']]
y = mashrooms_data['class']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=100, stratify=y)

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion = "gini", max_depth=10)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score
print("Accuracy score is :", accuracy_score(y_pred, y_test))

from sklearn import tree
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(4, 4), dpi=1000)
fn = ['cap-shape', 'cap-color', 'ring-number', 'gill-size', 'gill-color']
cn = ['poisonous', 'edible']

tree.plot_tree(model,
               feature_names=fn,
               class_names=cn,
               filled=True)

fig.savefig('tree.png')