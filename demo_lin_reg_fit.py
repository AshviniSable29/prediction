import pickle
from sklearn.linear_model import LinearRegression

cgpa = [[8], [5], [3], [9], [10]]
salary= [200000, 30000, 20000, 400000, 1100000]

model = LinearRegression()
model.fit(cgpa, salary)

# Save the trained model using pickle
with open('model1.pkl', 'wb') as file:
    pickle.dump(model, file)
