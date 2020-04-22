import pandas as pd
import numpy as np

# Sostoitsya li koncert?
# Pevec bil v golose pel, pevec bil ne v golose pel ili ne pel
data = {'health': ['in_voice', 'out_voice', 'out_voice', 'in_voice', 'in_voice', 'out_voice'],
        'concert': ['yes', 'yes', 'no', 'yes', 'yes', 'no']}

df = pd.DataFrame(data)
print(df)

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
df['health'] = le.fit_transform(df['health'])
print("Health encoded \n", df['health'])

df['concert'] = le.fit_transform(df['concert'])
print("Concert encoded \n", df['concert'])

X = df['health']
X = np.array(X)
X = X.reshape(-1, 1)
y = df['concert']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=101)

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train, y_train)
prediction = model.predict(X_test)
#print('Concert :', prediction)
print('Concert  : ', model.predict([[0],[1]])) #  (health - 0, health-1)

from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
print('Accuracy score is : ', accuracy_score(y_test, prediction))
print('Precision score is : ', precision_score(y_test, prediction))
print('Recall score is : ', recall_score(y_test, prediction))
print('Confusion matrix: ', confusion_matrix(y_test, prediction))