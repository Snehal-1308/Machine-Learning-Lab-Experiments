# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


data = pd.DataFrame({
    'size': [1500, 1800, 2400, 3000, 3500, 1200, 2000, 2700],
    'bedrooms': [3, 4, 3, 5, 4, 2, 3, 4],
    'age': [10, 5, 8, 2, 1, 20, 7, 3],
    'price': [300000, 400000, 500000, 650000, 700000, 200000, 450000, 600000]
})

print("Dataset:\n", data)

X = data[['size', 'bedrooms', 'age']]
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nModel Evaluation:")
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

plt.figure(figsize=(12, 4))

# Plot 1: Actual vs Predicted
plt.subplot(1, 3, 1)
plt.scatter(y_test, y_pred)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual vs Predicted")

# Plot 2: Residual Plot
plt.subplot(1, 3, 2)
residuals = y_test - y_pred
plt.scatter(y_pred, residuals)
plt.axhline(y=0)
plt.xlabel("Predicted")
plt.ylabel("Residuals")
plt.title("Residual Plot")

# Plot 3: Size vs Price
plt.subplot(1, 3, 3)
plt.scatter(data['size'], data['price'])
plt.xlabel("Size")
plt.ylabel("Price")
plt.title("Size vs Price")

plt.tight_layout()
plt.show()
