import pandas as pd

# Ahxatoxi xndirneri lucelu makardak@
job_data = pd.read_csv("jobclassinfo2.csv")
print(job_data.columns)
print(job_data.shape)
print(job_data.head(10))
print(job_data.tail(7))
print(job_data.isna().sum())
print(job_data.describe())
print(job_data.dtypes)
print(job_data.info())
print(job_data['ProblemSolving'].head(10)) # Sa y-na: Ashxatoxi xndirneri lucelu makardak@

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
job_data['FinancialBudget'] = le.fit_transform(job_data['FinancialBudget'])
job_data['ContactLevel'] = le.fit_transform(job_data['ContactLevel'])
job_data['Supervision'] = le.fit_transform(job_data['Supervision'])
job_data['EducationLevel'] = le.fit_transform(job_data['EducationLevel'])
job_data['PayGrade'] = le.fit_transform(job_data['PayGrade'])
#print(job_data.info())

X = job_data[['FinancialBudget', 'ContactLevel', 'Supervision', 'EducationLevel', 'PayGrade']]
y = job_data['ProblemSolving']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40, random_state=100, stratify=y)

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, max_depth=10)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

from sklearn.metrics import max_error
print('Max error is : ', max_error(y_test, y_pred)) # hashvarkum e anpetq tvyalneri maximal sxal@

feature_imp = pd.Series(model.feature_importances_)
print('Feature importance\n', feature_imp)

import matplotlib.pyplot as plt
plt.matshow(job_data[['FinancialBudget', 'ContactLevel', 'Supervision', 'EducationLevel', 'PayGrade']].corr())
plt.xticks(range(job_data[['FinancialBudget', 'ContactLevel', 'Supervision', 'EducationLevel', 'PayGrade']].shape[1]), job_data[['FinancialBudget', 'ContactLevel', 'Supervision', 'EducationLevel', 'PayGrade']].columns, fontsize=12, rotation=90)
plt.yticks(range(job_data[['FinancialBudget', 'ContactLevel', 'Supervision', 'EducationLevel', 'PayGrade']].shape[1]), job_data[['FinancialBudget', 'ContactLevel', 'Supervision', 'EducationLevel', 'PayGrade']], fontsize=12)
clb = plt.colorbar()
clb.ax.tick_params(labelsize=12)
plt.show()