import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load data (using a sample dataset)
data = {'YearsExperience': [1.1, 1.3, 2.0, 3.0, 5.0, 7.0], 'Salary': [39000, 46000, 43000, 60000, 80000, 95000]}
df = pd.DataFrame(data)

# Split data
X = df[['YearsExperience']]
y = df['Salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions and Results
y_pred = model.predict(X_test)
print(f"Coefficients: {model.coef_}, Intercept: {model.intercept_}")

# Visualization
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.title('Salary vs Experience')
plt.show()
