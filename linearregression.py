import matplotlib.pyplot as plt
# Data
x = [1, 2, 3]
y = [2, 3, 4]

# Initialize parameters
w = 0
b = 0
eta = 0.1
epochs = 10

# Gradient Descent with logging
for epoch in range(epochs):
    dw = 0
    db = 0
    loss = 0
    n = len(x)

    for i in range(n):
        y_pred = w * x[i] + b
        error = y_pred - y[i]
        dw += error * x[i]
        db += error
        loss += error ** 2

    w -= eta * dw / n
    b -= eta * db / n
    mse = loss / n

    print(f"Epoch {epoch+1:3d}: w = {w:.4f}, b = {b:.4f}, loss = {mse:.4f}")

# Final equation
print(f"\nFinal equation: y = {w:.4f}x + {b:.4f}")

# Plotting
plt.scatter(x, y, color='blue')  # data points
y_pred_line = [w * xi + b for xi in x]
plt.plot(x, y_pred_line, color='red')  # regression line
plt.show()




