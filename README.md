🔍 **Understanding Linear Regression with Gradient Descent in Python!**

I recently explored a simple but powerful implementation of **Linear Regression** using **Gradient Descent**, written from scratch using Python and `matplotlib` for visualization.

### 📌 What this code does:

✅ Takes sample data:
x = [1,2,3], y = [2, 3, 4] (a clear linear pattern)

✅ Initializes:

* Weights `w = 0`, bias `b = 0`
* Learning rate `eta = 0.1`
* Iterates over 10 epochs to update parameters using **gradient descent**

✅ Performs:

* Forward pass: calculates predicted `y_pred = w*x + b`
* Backpropagation: computes gradients `dw` and `db`
* Updates model: adjusts `w` and `b` to reduce error
* Logs loss (MSE) and weights per epoch

✅ Finally:

* Prints the final linear equation
* Visualizes the result with a **scatter plot** of original data and the fitted **regression line** in red

### 📉 Output:

The model learns a simple line close to `y = x + 1` with very low loss — demonstrating how gradient descent can fit a linear model even with just a few data points.

### 📊 Visualization:

* Blue dots = actual data points
* Red line = model prediction after training



