from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
Y = [2, 4, 5, 4.5, 4.5]

model = LinearRegression()
model.fit(X, Y)

slope = model.coef_[0]
intercept = model.intercept_
prediction = model.predict([[6]])

print("Slope: ", slope)
print("Intercept: ", intercept)
print("Regression Equation: ")
print(f"y = {slope:.2f}x + {intercept:.2f}")
print("Predicted value for X = 6: ", round(prediction[0], 2))