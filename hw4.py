import pandas as pd

# Math operations

print("Math operations:")
df = pd.DataFrame({'Col1': [10, 20, 30, 40], 'Col2': [2, 3, 4, 5], 'Col3': [5, 10, 3, 4]})
df['Multiplication'] = 4 * df['Col1'] # bazmapatkel 4-ov miayn col1 kolonkan
df['Total 1'] = df['Col1'] / df['Col2']
df['Total 2'] = df['Col1'] // df['Col3']
df['Pow'] = 2 ** df['Col2']
print(df)
print("Specific value is: ",  4 * df.iloc[2, 1])
print("Specific value are: ",  100 - df.iloc[[1, 3], 2])

print("Sum:")
df = pd.DataFrame({'First': [100, 20, 32], 'Second': [78, 53, 10], 'Third':[50, 90, 10]})
df['Total'] = df.sum(axis=1)
print(df)

print('Subtraction:')
df1 = pd.DataFrame({"A": [10, 50, 30, 40, 20],
                    "B": [30, 2, 40, 30, 40],
                    "C": [200, 102, 70, 30, 104],
                    "D": [4, 308, 64, 12, 50]})

df2 = pd.DataFrame({"A": [5, 10, 7, 8, 5],
                    "B": [20, 1, 32, 4, 6],
                    "C": [11, 21, 23, 7, 9],
                    "D": [1, 5, 3, 8, 6]})
sub = df1.subtract(df2)
print(sub)



# Logistic Regression

# Kupit li klient produkt?
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

sale_data = {'PrevSale': [150, 230, 100, 130, 110, 120, 130, 90], 'Week': [1, 2, 3, 4, 5, 2, 3, 5], 'isPaying': [0, 0, 1, 1, 0, 1, 1, 0]}
sale = pd.DataFrame(sale_data)
print(sale)

X = sale[['PrevSale', 'Week']]
y = sale['isPaying']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)

logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)

prediction = logmodel.predict(X_test)
print(prediction)

from sklearn.metrics import classification_report
print('Classification report: ', classification_report(y_test, prediction)) # Inchqanova chisht

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, prediction))



