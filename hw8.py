import pandas as pd

# Ginin karmir e te voch
wine_data = pd.read_csv("winequalityN.csv")
print(wine_data.columns)
print(wine_data.shape)
print(wine_data.head(10))
print(wine_data.tail(7))
print(wine_data.isna().sum())
print(wine_data.describe())
print(wine_data.dtypes)
print(wine_data.info())

wine_data.fillna(wine_data.mean(), inplace=True)
print(wine_data.isna().sum())
print(wine_data.dtypes)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
wine_data['type'] = le.fit_transform(wine_data['type']) # Sa y-na:  Ginin karmir e te voch

from sklearn.preprocessing import StandardScaler
model_scaler = StandardScaler()
wine_data[['chlorides', 'free sulfur dioxide', 'total sulfur dioxide']] = model_scaler.fit_transform(wine_data[['chlorides', 'free sulfur dioxide', 'total sulfur dioxide']])

X = wine_data.drop(['type'], axis=1)
y = wine_data['type']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.50, random_state=100)

from sklearn.svm import SVC
model = SVC(kernel='linear')
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score, confusion_matrix
print("Accuracy score is: ", accuracy_score (y_pred, y_test))
print("Confusion matrix is: ", confusion_matrix (y_pred, y_test))