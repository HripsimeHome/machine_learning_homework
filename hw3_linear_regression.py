import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([5, 30, 45, 59]).reshape(-1, 1)
y = np.array([20, 25, 40, 52])

model = LinearRegression().fit(x, y)
print("R squared", model.score(x, y))
print("Intercept: ", model.intercept_)
print("Slope: ", model.coef_)
y_pred = model.intercept_ + model.coef_ * x
print('Predicted response:', y_pred)

plt.scatter(x, y, color="r")
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x, model.predict(x))
plt.show()
