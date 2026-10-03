from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [4], [5], [6]]
Y = [0, 0, 0, 1, 1, 1]

model = LogisticRegression()
model.fit(X, Y)

new_data = [[4.5]]
prediction = model.predict(new_data)
probability = model.predict_proba(new_data)

print("Predicted Class: ", prediction[0])
print("Probability of class 0:", round(probability[0][0], 2))
print("Probability of class 1:", round(probability[0][1], 2))
