import numpy as np

class Perceptron:
    def __init__(self, input_size, lr=1, epochs=10):
        self.W = np.zeros(input_size+1)
        self.epochs = epochs
        self.lr = lr

    # Step function
    def activation_fn(self, x):
        return 1 if x >= 0 else 0

    # Prediction function
    def predict(self, x):
        x = np.insert(x, 0, 1)
        z = self.W.T.dot(x)
        a = self.activation_fn(z)
        return a

    # Training function
    def fit(self, X, d):
        for _ in range(self.epochs):
            for i in range(d.shape[0]):
                x = np.insert(X[i], 0, 1)
                y = self.predict(X[i])
                e = d[i] - y
                self.W = self.W + self.lr * e * x

# Example usage
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

d = np.array([0, 0, 0, 1])

perceptron = Perceptron(input_size=2)
perceptron.fit(X, d)

print("Weights:", perceptron.W)
print("Predictions:")
for i in range(len(X)):
    print("Input:", X[i], "Predicted Output:", perceptron.predict(X[i]))